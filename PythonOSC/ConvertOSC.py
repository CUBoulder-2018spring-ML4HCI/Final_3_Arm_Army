import argparse
import math

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import osc_message_builder
from pythonosc import udp_client

SEND_IP = "10.0.0.88"
SEND_PORT = 8000
SEND_MESSAGE = "/wek/outputs"



def print_volume_handler(unused_addr, args, volume):
  print("[{0}] ~ {1}".format(args[0], volume))

# def test_handler(unused_addr, x, y, z, a, b, p1, p2, p3):
#         print(str(x) + "!!!")
#         print(str(y) + "!!!")
#         print(str(z) + "!!!")

def send_edited(unused_addr, x, y, z, a, b, p1, p2, p3):
    list_acc = [x, y, x]
    print(list_acc)
    client = udp_client.SimpleUDPClient(SEND_IP, SEND_PORT)
    client.send_message(SEND_MESSAGE, list_acc)

# def print_compute_handler(unused_addr, args, volume):
#   try:
#     print("[{0}] ~ {1}".format(args[0], args[1](volume)))
#   except ValueError: pass
#
# def print_handler(unused_addr, args, volume):
#   try:
#     print("[{0}] ~ {1}".format(args[0], args[1](volume)))
#   except ValueError: pass

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=57120, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/wek/inputs", send_edited)
  # dispatcher.map("/wek/inputs", print_volume_handler, "Volume")
  # dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)

  server = osc_server.ThreadingOSCUDPServer(
      (args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()
