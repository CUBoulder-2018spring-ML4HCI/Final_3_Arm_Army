#!/usr/bin/env python

#Bring in required imports
import time
import signal
import threading
import RPi.GPIO as GPIO
from multiprocessing import Value
from motor import motorDriver
from motor import motor

#osc imports
import argparse
import random
import sys
from pythonosc import osc_message_builder
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client



'''
' Code needed to hangle ctrl+c exit
' GPIO pins need to be freed or else resarting takes minutes
'''
def sigint_handler(signum, frame):
    print("Cleaning Up GPIO pins")
    GPIO.cleanup()
    stopServer()
    sys.exit()

signal.signal(signal.SIGINT, sigint_handler)


'''
' OSC Set up
' The arm right now is set up to only receive
'''
server_ip = "0.0.0.0"
server_port = 12000
server_thread = None
server = None
client = udp_client.SimpleUDPClient("localhost", server_port)
motion = "stop"

#Used for the 2 motor drivers
global lowerDriver
global higherDriver
global num
#Used For motor Names
BASE = "base"
CENTER = "center"
PIVOT = "pivot"
CLAW = "claw"

def setupMotors():
    #Declare The GPIO Settings
    GPIO.setmode(GPIO.BOARD)
    '''
    ' Setup first motor driver
    '   1) init motor driver class
    '   2) add motor A
    '   3) add motor B
    '''
    global lowerDriver
    lowerDriver = motorDriver("lowerMotors", 13)
    lowerDriver.addMotor(BASE, 7, 12, 11)
    lowerDriver.addMotor(CENTER,29,15,16)

    global higherDriver
    higherDriver = motorDriver("higherMotors", 22)
    higherDriver.addMotor(PIVOT, 37,35,33)
    higherDriver.addMotor(CLAW, 36,38,40)

def mix(addr,test):
    global state
    state.changeState("mix")

def scoop(addr, test):
    global state
    state.changeState("scoop")

def move(addr):
    global state
    state.changeState("move")

#Function given by Ben
#Modified by Ryan
def handle_tick(message, ignore_this):
    global state
    print("State inside tick: " + state.getCurrentState())
    #print("{:f}: Tick!".format(time.time()))


#Function given by Ben
#Modified by Ryan
def start_server_in_separate_thread():
    global server_thread, server_ip, server_port, server
    dis = dispatcher.Dispatcher()
    dis.map("/tick", handle_tick)
    dis.map("/output_1", mix)
    dis.map("/output_2", scoop)
    dis.map("/output_3", move)

    # add other dispatcher hooks here

    server = osc_server.BlockingOSCUDPServer((server_ip, server_port), dis)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()

#Function given by Ben
def stopServer():
    global server_thread
    server.shutdown()

#Function given by Ben
def sendTick():
    global client
    client.send_message("/tick", 42)

'''
' Based off code osc-threaded-example-threadingVariable.py that was provided by Ben
' Class State allows us to handle the state of the motor
'''
class State:
    def __init__(self):
        self.motion = "stop"
        self.lock = threading.RLock()

    def changeState(self, updatedMotion):
        with self.lock:
            self.motion = updatedMotion

    def getCurrentState(self):
        with self.lock:
            return self.motion

    def printCurrentState(self):
        print("counter = {:d}".format(self.get_current_counter()), flush=True)

state = State()

def main():
    global state
    print("Before starting server, the state is: " + state.getCurrentState())
    start_server_in_separate_thread()
    #setupMotors()
    while True:
        print("Before tick, state: " + state.getCurrentState())
        sendTick()
        time.sleep(1)

if __name__ == "__main__":
    main()
