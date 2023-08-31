from simple_http_server import request_map, controller, route, server
from simple_http_server import Response, Request, PathValue
from simple_http_server import MultipartFile
from simple_http_server import Parameter
from simple_http_server import Parameters
from simple_http_server import Header
from simple_http_server import JSONBody
from simple_http_server import HttpError
from simple_http_server import StaticFile
from simple_http_server import Headers
from simple_http_server import Cookies
from simple_http_server import Cookie
from simple_http_server import Redirect
from simple_http_server import ModelDict
import simple_http_server.logger as logger
import base64
from io import BytesIO
import os
import sys


gcode_file_path = ""
route_path = ""


@controller
@route("/status")
class status_manager:
  def __init__(self):
    self.name="status manager"

  @request_map("/machine")
  def get_machine_status(self):
    return 200, machine.status.to_string_array()

@controller
@route("/ctrl")
class control_manage:
  def __init__(self):
    self.name="control manager"

  @request_map("/move", method=("POST"))
  def move_axis(self, axis=Parameter('axis'), distance=Parameter('distance')):
    machine.move_axis(int(axis), float(distance))
    return 200
  
  @request_map("/extrude", method=("POST"))
  def extrude(self, nozzle=Parameter('axis'), distance=Parameter('distance')):
    machine.extrude(int(nozzle), float(distance))
    return 200
  
  @request_map("/retract", method=("POST"))
  def retract(self, nozzle=Parameter('axis'), distance=Parameter('distance')):
    machine.retract(int(nozzle), float(distance))
    return 200
  
  @request_map("/quick_stop", method=("GET"))
  def quick_stop(self):
    machine.quick_stop()
    return 200
  
  @request_map('/heat')
  def heat_up(self, target=Parameter('target'), temp=Parameter('temp')):
    machine.heatup(int(target), int(temp))
    return 200

  @request_map('/fan')
  def heat_up(self, fan=Parameter('fan'), speed=Parameter('speed')):
    machine.set_fan(int(fan), int(speed))
    return 200

  @request_map('/homeall')
  def homeall(self):
    machine.home_all()
    return 200

  @request_map('/homeaxis')
  def homeall(self, axis=Parameter('axis')):
    machine.home_axis(int(axis))
    return 200

@controller
@route("/files")
class file_manager:
  def __init__(self):
    self.name="file manager"

  def __get_file_preview(self, file_name):
    param_search = {";estimated_time(s):": "0", ";nozzle_temperature(°C):": "0", ";build_plate_temperature(°C):": "0", ";layer_height:": "0", ";matierial_weight:": "0", ";LAYER_COUNT:": "0", ";thumbnail: data:image/png;base64,": ""}
    keys = list(param_search.keys())
    with open(gcode_file_path + file_name, encoding='utf-8') as f:
      for i in range(100):
        tmpline = f.readline()
        for item_key in keys:
          if item_key in tmpline:
            param_search[item_key] = tmpline.replace(item_key, '').strip()
    retval = ','.join(param_search.values())
    return retval


  @request_map("/upload", method=("GET","POST"))
  def upload(self, file=MultipartFile("file")):
    file.save_to_file(gcode_file_path + file.filename)
    return 200
  
  @request_map("/list", method=("GET"))
  def listitem(self, pageindex=Parameter('page'),page_per_count=Parameter('page_per_count')):
    pageindex = int(pageindex)
    page_per_count = int(page_per_count)

    dir = os.listdir(gcode_file_path)
    files = []
    for item in dir:
      if os.path.isdir(gcode_file_path + item):
        continue
      if(item[-5:] != 'gcode'):
        continue
      files.append(item)
    
    total_page = int(len(files) / (page_per_count))
    if(len(files) % page_per_count != 0): total_page = total_page + 1

    if(pageindex > (total_page-1)):
      pageindex = total_page - 1
    
    start_index = pageindex * page_per_count
    end_index = start_index + page_per_count
    
    if(start_index > len(files) - 1): return 200, '[' + str(total_page-1) + ']'
    if(end_index > (len(files)-1)): end_index = len(files) - 1
    return 200, '[' + str(pageindex) + ']' + '//'.join(files[start_index:end_index + 1])
  
  @request_map("/delete", method=("POST"))
  def delete_file(self, file_name=Parameter("file_name")):
    os.remove(gcode_file_path + str(file_name))
    return 200

  @request_map("/preview", method=("POST"))
  def delete_file(self, file_name=Parameter("file_name")):
    retval = self.__get_file_preview(file_name)
    return 200, retval
  
  @request_map("/print", method=("POST"))
  def start_print(self, file_name=Parameter("file_name")):
    machine.start_print(str(file_name))

  @request_map("/pause", method=("GET"))
  def pause_print(self):
    machine.pause_print()

  @request_map("/resume", method=("GET"))
  def resume_print(self):
    machine.resume_print()

  @request_map("/stop", method=("GET"))
  def stop_print(self):
    machine.stop_print()


if __name__ == '__main__':
    sys.path.append('./TcpProcessor')
    if(os.name == 'nt'):
      gcode_file_path = './local/test/'
      route_path = '/'
    else:
      gcode_file_path = '/home/wqf/gcode/'
      route_path = '/api'
      sys.path.append('/home/wqf/html/TcpProcessor')
      
    logger.set_level("ERROR")
    print(sys.path)

    from TcpProcessor.ProtocalV30 import TcpTransmiter, MachineControler

    machine = MachineControler()

    print('Gcode path:' + gcode_file_path)
    print('Router path' + route_path)
    server.start(port=8888)