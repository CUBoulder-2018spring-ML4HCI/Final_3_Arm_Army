#!/usr/bin/env python

#Bring in required imports
import time
import signal
import _thread
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



'''
' Code needed to hangle ctrl+c exit
' GPIO pins need to be freed or else resarting takes minutes
'''
def sigint_handler(signum, frame):
    print("Cleaning Up GPIO pins")
    GPIO.cleanup()
    sys.exit()

signal.signal(signal.SIGINT, sigint_handler)


'''
' OSC Set up
' The arm right now is set up to only receive not
'''
input_host = "0.0.0.0"
input_port = 12000


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

def getNum(addr,args):
    global num
    #if args is not list: args = (args, )
    num = int(args)
    print("Received: " + str(args))

    if num == 1.0:
        lowerDriver.clockwise(BASE)
        lowerDriver.clockwise(CENTER)
    elif num == 2.0:
        lowerDriver.counterClockwise(BASE)
        lowerDriver.counterClockwise(CENTER)
    elif num == 3.0:
        lowerDriver.stopMotor(BASE)
        lowerDriver.stopMotor(CENTER)
        higherDriver.stopMotor(PIVOT)
        higherDriver.stopMotor(CLAW)
    elif num == 4.0:
        higherDriver.clockwise(PIVOT)
        higherDriver.clockwise(CLAW)
    elif num == 5.0:
        higherDriver.counterClockwise(PIVOT)
        higherDriver.counterClockwise(CLAW)
    else:
        print("number not recognised")

def output1(addr,args):
    lowerDriver.stopMotor(BASE)
    lowerDriver.stopMotor(CENTER)

def output2(addr,args):
    lowerDriver.counterClockwise(BASE)
    lowerDriver.counterClockwise(CENTER)

def output3(addr,args):
    lowerDriver.clockwise(BASE)
    lowerDriver.clockwise(CENTER)

def mix(addr,test):
    global motion
    print(test)
    motion = "mix"
    print("Start Mixing")

def scoop(addr):
    global motion
    motion = "scoop"
    print("Start Scoop")

def move(addr):
    global motion
    motion = "move"
    print("Starting Move")


'''
def startServer():
    global motion
    motion = "start"
    dis = dispatcher.Dispatcher()
    dis.map("/output_1", mix)
    dis.map("/output_2", scoop)
    dis.map("/output_3", move)
    server = osc_server.ForkingOSCUDPServer((input_host, input_port), dis)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
''' 
    
def main():
    global motion
    motion = "start" 
    dis = dispatcher.Dispatcher()
    dis.map("/output_1", mix)
    dis.map("/output_2", scoop)
    dis.map("/output_3", move)
    server = osc_server.ForkingOSCUDPServer((input_host, input_port), dis)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    
    #some code
    setupMotors()
    while True:
        print(motion)



if __name__ == "__main__":
    main()
