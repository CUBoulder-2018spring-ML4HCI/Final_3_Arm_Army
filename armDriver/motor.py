#!/usr/bin/env python

#Bring in required imports
import time
import RPi.GPIO as GPIO

class motorDriver:
    def __init__(self, name, stby):
        self.motors = []
        self.name = name
        self.stby = stby
        GPIO.setup(self.stby, GPIO.OUT)

    def addMotor(self, name, pwm, in1,in2):
        self.motors.append(motor(name, pwm, in1, in2))

    '''
    ' The Stby pin on the motor driver when set to high
    ' allows the motors to turn.
    '''
    def disableStby(self):
        GPIO.output(self.stby, GPIO.HIGH)

    '''
    ' The Stby pin on the motor driver when set to low
    ' stops both motors. Like a fail safe
    '''
    def enableStby(self):
        GPIO.output(self.stby, GPIO.LOW)

    def getMotorByName(self, motorName):
        for motor in self.motors:
            if motor.name == motorName:
                return motor
        return None

    def clockwise(self, motorName, sleepTime):
        self.disableStby()
        motor = self.getMotorByName(motorName)
        if motor != None:
            motor.clockwise(sleepTime)

    def counterClockwise(self, motorName, sleepTime):
        self.disableStby()
        motor = self.getMotorByName(motorName)
        if motor != None:
            motor.counterClockwise(sleepTime)


class motor:
    def __init__(self, name, pwm, in1, in2):
        #store variables
        self.name = name
        self.pwm = pwm
        self.in1 = in1
        self.in2 = in2

        #initialise pins
        GPIO.setup(self.pwm, GPIO.OUT) # conected to PWMA
        GPIO.setup(self.in1, GPIO.OUT) # IN1
        GPIO.setup(self.in2, GPIO.OUT) # IN2

    def clockwise(self, sleepTime):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.pwm, GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(self.pwm, GPIO.LOW)


    def counterClockwise(self, sleepTime):
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.pwm, GPIO.HIGH)
        time.sleep(sleepTime)
        GPIO.output(self.pwm, GPIO.LOW)
