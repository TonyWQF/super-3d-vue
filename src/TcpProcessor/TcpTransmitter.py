import socket
from threading import Thread
import time


class TcpTransmiter:
  def __init__(self):
    self.pack_queue = []
    self.__recv_buffer = b''
    self.__recv_thread_handle = Thread(target=self.__receive_thread, daemon=True)
    self.__recv_thread_handle.start()
    self.__connect_retry = False

  def fetch_data(self):
    retval = b''
    if(len(self.__recv_buffer) > 0):
      retval = self.__recv_buffer
      self.__recv_buffer = b''
    return retval

  def peek_length(self):
    return len(self.__recv_buffer)

  def __receive_thread(self):
    while(True):
      try:
        datas = self.tcp_client.recv(10240)
        self.__recv_buffer = self.__recv_buffer + datas
        if(len(self.__recv_buffer) > 40960):
          self.__recv_buffer = b''
      except:
        time.sleep(1)

  def connect_check(self):
    print("Connect after 1s")
    time.sleep(1)
    while(True):
      try:
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_client.connect(("127.0.0.1", 7777))
        if(len(self.pack_queue) > 0):
          self.tcp_client.send(self.pack_queue[0])
          self.pack_queue = self.pack_queue[1:]
        print('connect ok')
        break
      except:
        print('connect fail')
        time.sleep(1)
        continue
      self.__connect_retry = False

  def send_pack(self, data):
    try:
      self.tcp_client.send(data)
      return True
    except:
      if(self.__connect_retry == False):
        self.__connect_retry = True
        self.pack_queue.append(data)
        self.connection_thread = Thread(target=self.connect_check, daemon=True)
        self.connection_thread.start()
      return False
