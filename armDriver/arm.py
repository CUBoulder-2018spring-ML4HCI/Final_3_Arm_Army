#!/usr/bin/env python

#Bring in required imports
import time
import signal
import RPi.GPIO as GPIO
from motor import motorDriver
from motor import motor



'''
' Code needed to hangle ctrl+c exit
' GPIO pins need to be freed or else resarting takes minutes
'''
def sigint_handler(signum, frame):
    print("Cleaning Up GPIO pins")
    GPIO.cleanup()

signal.signal(signal.SIGINT, sigint_handler)


#Used for the 2 motor drivers
global lowerDriver
higherDriver = None


#Used For motor Names
BASE = "base"


def setup():
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



def main():
    #some code
    setup()

    while True:
        lowerDriver.clockwise(BASE, .75)
        time.sleep(.75)


if __name__ == "__main__":
    main()
