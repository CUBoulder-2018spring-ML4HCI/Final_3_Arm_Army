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
global startTime
global step
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
    #addMotor(self, name, pwm, in1,in2,minLimit, maxLimit, travelSpeed, startLocation):
    global lowerDriver
    lowerDriver = motorDriver("lowerMotors", 13)
    lowerDriver.addMotor(BASE, 7, 12, 11, 0,180, 0.064, 0)
    lowerDriver.addMotor(CENTER,29,15,16, 0,165, 0.033, 0)

    global higherDriver
    higherDriver = motorDriver("higherMotors", 22)
    higherDriver.addMotor(PIVOT, 37,35,33, 0,180, 0.031, 0)
    higherDriver.addMotor(CLAW, 36,38,40, 0,180, 0.0, 0)

def mix(addr,test):
    global state
    state.changeState("mix")

def scoop(addr, test):
    global state
    state.changeState("scoop")

def move(addr):
    global state
    state.changeState("move")

#square motion for mix
mixSteps = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#scoop goes to center and picks up
scoopSteps = [[90,100,135,0], [90,90,90,0]]

#move moves it to end of plate
moveSteps = [[175, 90,90, 0]]

#Function given by Ben
#Modified by Ryan
def handle_tick(message, ignore_this):
    global state, lowerDriver, higherDriver, startTime, step
    deltaTime = time.time() - startTime
    lowerDriver.update(deltaTime)
    if state.sameState():
        step = 0

    #check if motors all at location
    if(lowerDriver.getTargetReachedMotor(BASE) and lowerDriver.getTargetReachedMotor(CENTER) and higherDriver.getTargetReachedMotor(PIVOT)):
        step = step + 1

    if state.getCurrentState() == 'mix':
        #mix logic
        if(step < len(mixStep)-1):
            lowerDriver.updateMotorTargetLocation(BASE, mixStep[step][0])
            lowerDriver.updateMotorTargetLocation(CENTER, mixStep[step][1])
            higherDriver.updateMotorTargetLocation(PIVOT, mixStep[step][2])
        else:
            step = len(mixStep) - 1
    elif state.getCurrentState() == 'scoop':
        #scoop logic
        lowerDriver.updateMotorTargetLocation(BASE, scoopStep[step][0])
        lowerDriver.updateMotorTargetLocation(CENTER, scoopStep[step][1])
        higherDriver.updateMotorTargetLocation(PIVOT, scoopStep[step][2])

    elif state.getCurrentState() == 'move':
        #move logic
        lowerDriver.updateMotorTargetLocation(BASE, moveStep[step][0])
        lowerDriver.updateMotorTargetLocation(CENTER, moveStep[step][1])
        higherDriver.updateMotorTargetLocation(PIVOT, moveStep[step][2])
    else:
        lowerDriver.stopMotor(BASE)
        lowerDriver.stopMotor(CENTER)
        higherDriver.stopMotor(PIVOT)
        higherDriver.stopMotor(CLAW)


    print("State inside tick: " + state.getCurrentState())


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
        self.lastMotion = "stop"
        self.lock = threading.RLock()

    def changeState(self, updatedMotion):
        with self.lock:
            self.lastMotion = self.motion
            self.motion = updatedMotion

    def getCurrentState(self):
        with self.lock:
            return self.motion

    def sameState(self):
        with self.lock:
            if self.motion == self.motion:
                return True
            else:
                return False

    def printCurrentState(self):
        print("counter = {:d}".format(self.get_current_counter()), flush=True)

state = State()

def main():
    global state, startTime, step, higherDriver, lowerDriver
    step = 0
    start_server_in_separate_thread()
    setupMotors()
    startTime = time.time()
    while True:
        sendTick()
        time.sleep(.001)

if __name__ == "__main__":
    main()
