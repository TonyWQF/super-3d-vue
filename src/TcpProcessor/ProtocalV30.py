from threading import Thread, Lock
import time
from V30Commands import Commands, MachineStatus
from TcpTransmitter import TcpTransmiter

class MachineControler:
  def __init__(self):
    self.__recv_buffer = b''
    self.__protocal = ProtocalV30()
    self.__transmiter = TcpTransmiter()
    self.__commands = Commands()

    self.__heart_thread_handle = Thread(target=self.__auto_request_status, daemon=True)
    self.__heart_thread_handle.start()
  
    self.__data_thread_handle = Thread(target=self.__data_process, daemon=True)
    self.__data_thread_handle.start()
    self.__wait_queue = []
    self.__lock = Lock()
    

    self.status = MachineStatus()
    
    print('machine inited')

  def __data_process(self):
    while(True):
      new_data = self.__transmiter.fetch_data()
      self.__recv_buffer = self.__recv_buffer + new_data
      parse_data = self.__protocal.parse(self.__recv_buffer)
      if(parse_data is not None):
        self.__recv_buffer = parse_data[0]
        result = self.__commands.analize(parse_data[1])
        self.__check_wait(parse_data)
      self.status = self.__commands.machine_status
      time.sleep(0.01)

  def __auto_request_status(self):
    while(True):
      src_datas = self.__commands.req_status()
      datas_to_send = self.__protocal.setup_pack(src_datas)
      self.__transmiter.send_pack(datas_to_send)
      time.sleep(1)
  
  def __check_wait(self, data):
    if(len(self.__wait_queue) > 0):
      with self.__lock:
        for item in self.__wait_queue:
          if (item[0] == data[0] and item[1] == data[1]):
            item[2] = True
            item[3] = data
  
  def __wait_replay(self, Command, SubCommand, TimeOut):
    new_wait = [Command, SubCommand, False, None]
    self.__wait_queue.append(new_wait)
    time_counter = TimeOut * 10
    while(True):
      if(new_wait[2] == True):
        break
      if(TimeOut > 0): 
        time_counter = time_counter - 1
        if(time_counter == 0):
          with self.__lock:
            self.__wait_queue.remove(new_wait)
          return new_wait
      time.sleep(0.1)

    with self.__lock:
      self.__wait_queue.remove(new_wait)
    return new_wait
  
  def get_status(self):
    return self.status
  
  #发送数据，不等待应答
  def __send_command(self, data):
    datas_to_send = self.__protocal.setup_pack(data)
    self.__transmiter.send_pack(datas_to_send)

  #发送数据，并等待应答
  #返回数据为数组，[主命令，子命令，结果，应答数据]
  #结果为True，应答数据有效
  def __send_command_check_reply(self, data, TimeOut=5):
    datas_to_send = self.__protocal.setup_pack(data)
    self.__transmiter.send_pack(datas_to_send)
    return self.__wait_replay(data[0], data[1], TimeOut)

  def heatup(self, Target, Temp):
    src_datas = self.__commands.req_heatup(int(Target), int(Temp))
    self.__send_command(src_datas)

  def set_fan(self, Fan, Speed):
    src_datas = self.__commands.req_fan(Fan, Speed)
    self.__send_command(src_datas)

  def move_axis(self, Axis, Distance):
    src_datas = self.__commands.req_move_axis(Axis, Distance)
    self.__send_command(src_datas)

  def extrude(self, Nozzle, Distance):
    src_datas = self.__commands.req_extrude(Nozzle, Distance)
    self.__send_command(src_datas)

  def retract(self, Nozzle, Distance):
    src_datas = self.__commands.req_retract(Nozzle, Distance)
    self.__send_command(src_datas)

  def quick_stop(self):
    src_datas = self.__commands.req_quick_stop()
    self.__send_command(src_datas)

  def home_axis(self, Axis):
    src_datas = self.__commands.req_home_axis(Axis)
    self.__send_command(src_datas)

  def home_all(self):
    src_datas = self.__commands.req_home()
    self.__send_command(src_datas)

  def start_print(self,FileName):
    src_datas = self.__commands.req_remote_print(FileName)
    reply = self.__send_command_check_reply(src_datas, 5)
    if(reply[2] == True): return 200, ['success']
    else: return 200, ['fail']

  def stop_print(self):
    src_datas = self.__commands.req_remote_stop()
    reply = self.__send_command_check_reply(src_datas, 5)
    if(reply[2] == True): return 200, ['success']
    else: return 200, ['fail']

  def pause_print(self):
    src_datas = self.__commands.req_remote_pause()
    reply = self.__send_command_check_reply(src_datas, 5)
    if(reply[2] == True): return 200, ['success']
    else: return 200, ['fail']

  def resume_print(self):
    src_datas = self.__commands.req_remote_resume()
    reply = self.__send_command_check_reply(src_datas, 5)
    if(reply[2] == True): return 200, ['success']
    else: return 200, ['fail']

class ProtocalV30:
  def __init__(self):
    self.name="V40"
    self.version = '40'
  
  def setup_pack(self, source):
    packed_data = b'\xa5\x5a\x40'
    packed_data += int.to_bytes(len(source), 4, byteorder='little', signed=False)
    len_check = packed_data[3] ^ packed_data[4] ^ packed_data[5] ^ packed_data[6]
    packed_data += int.to_bytes(len_check, 1, byteorder='little',signed=False)
    checksum = 0
    for i in source:
      checksum = checksum + i
    checksum = checksum & 0xffff
    packed_data += int.to_bytes(checksum, 2, byteorder='little', signed=False)
    packed_data += source
    return packed_data

  def parse(self, source):
    while(len(source) >= 12):
      if(source[0] != 0xa5): 
        source = source[1:]
        continue
      if(source[1] != 0x5a): 
        source = source[2:]
        continue

      # Version

      #Pack len check
      if(source[3] ^ source[4] ^ source[5] ^ source[6] != source[7]):
        source = source[2:]
        print('Len Verify fail')
        continue

      pack_len = (source[3]) | (source[4] << 8) | (source[5] << 16) | (source[6] << 24)

      if(pack_len + 10) > len(source): 
        return None

      # Verify datas
      src_checksum = source[8] | (source[9] << 8)
      pack_data = source[10:10 + pack_len]
      cal_check = 0
      for i in pack_data:
        cal_check = cal_check + i
      cal_check = cal_check & 0xffff

      if(src_checksum != cal_check):
        source = source[2:]
        print('Check fail:' + str(src_checksum) + str(cal_check))
        continue

      source = source[pack_len + 10:]
      return [source, pack_data]
    return None


