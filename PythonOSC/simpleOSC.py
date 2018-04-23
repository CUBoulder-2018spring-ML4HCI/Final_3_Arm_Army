import argparse
import random
import time
import sys

from pythonosc import osc_message_builder
from pythonosc import udp_client

IP = "192.168.2.9"
PORT = 12000
OSC_MESSAGE = "/output_1"

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default=IP)
  parser.add_argument("--port", type=int, default=12000)
  parser.add_argument("--classification", default=1)
  args = parser.parse_args()
  print(str(args.classification))

  print("Sending message to /wek/outputs: " + str(float(args.classification)))

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  client = udp_client.SimpleUDPClient(args.ip, args.port)
  client.send_message(OSC_MESSAGE, OSC_MESSAGE)
  #client.send_message(OSC_MESSAGE, float(args.classification))
