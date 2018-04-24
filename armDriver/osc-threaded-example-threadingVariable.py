import time
import threading
import sys

from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = threading.RLock()

    def increment(self):
        with self.lock:
            self.count += 1
    
    def decrement(self):
        with self.lock:
            self.count += 1

    def get_current_counter(self):
        with self.lock:
            return self.count
    
    def print_current_counter(self):
        print("counter = {:d}".format(self.get_current_counter()), flush=True)
     
server_ip = "0.0.0.0"
server_port = 4242
server_thread = None
server = None

client = udp_client.SimpleUDPClient("localhost", server_port)

def handle_tick(message, ignore_this):
    global counter
    counter.increment()
    print("\t{:f}: Tick! counter = {:d}".format(time.time(), counter.get_current_counter()), flush=True)

def start_server_in_separate_thread(counter):
    global server_thread, server_ip, server_port, server
    our_dispatcher = dispatcher.Dispatcher()
    our_dispatcher.map("/tick", handle_tick)
    # add other dispatcher hooks here

    server = osc_server.BlockingOSCUDPServer((server_ip, server_port), our_dispatcher)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()

def stop_server():
    global server_thread
    server.shutdown()

def send_tick():
    global client
    client.send_message("/tick", 42)

###### Main ######

counter = Counter()
print("Before starting server, the count is {:d}", counter.get_current_counter())

start_server_in_separate_thread(counter)

for i in range(42):
    print("Before tick, counter = {:d}".format(counter.get_current_counter()), flush=True)
    send_tick()
    time.sleep(.1)
    print("After tick, counter = {:d}".format(counter.get_current_counter()), flush=True)
    print("--")
    time.sleep(.1)

stop_server()