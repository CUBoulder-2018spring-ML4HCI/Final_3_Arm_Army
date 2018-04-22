import time
import threading

from pythonosc import osc_message_builder
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

server_ip = "0.0.0.0"
server_port = 4242
server_thread = None
server = None

client = udp_client.SimpleUDPClient("localhost", server_port)

def handle_tick(message, ignore_this):
    print("{:f}: Tick!".format(time.time()))

def start_server_in_separate_thread():
    global server_thread, server_ip, server_port, server
    our_dispatcher = dispatcher.Dispatcher()
    our_dispatcher.map("/tick", handle_tick)
    # add other dispatcher hooks here

    server = osc_server.ForkingOSCUDPServer((server_ip, server_port), our_dispatcher)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()

def stop_server():
    global server_thread
    server.shutdown()

def send_tick():
    global client
    client.send_message("/tick", 42)

###### Main ######
start_server_in_separate_thread()
for i in range(10):
    send_tick()
    time.sleep(.01)

stop_server()