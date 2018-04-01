#!/usr/bin/env python

#Bring in required imports
import time
import signal
import RPi.GPIO as GPIO
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
    lowerDriver.addMotor("base", 7, 12, 11)

def getNum(addr,args):
    global num
    #if args is not list: args = (args, )
    num = int(args)
    print("Received: " + str(args))

    if num == 1.0:
        lowerDriver.clockwise(BASE, .75)
    elif num == 2.0:
        lowerDriver.counterClockwise(BASE, .75)
    else:
        print("number not changed")
    num = 0


def main():
    #some code
    setupMotors()

    dis = dispatcher.Dispatcher()
    dis.map("/wek/outputs", getNum)
    server = osc_server.ThreadingOSCUDPServer((input_host, input_port), dis)
    server.serve_forever()
    

if __name__ == "__main__":
    main()
