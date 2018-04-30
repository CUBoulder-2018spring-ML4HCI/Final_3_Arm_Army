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

    def addMotor(self, name, pwm, in1,in2,minLimit, maxLimit, travelSpeed, startLocation):
        self.motors.append(motor(name, pwm, in1, in2, minLimit, maxLimit, travelSpeed, startLocation))

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

    def clockwise(self, motorName):
        self.disableStby()
        motor = self.getMotorByName(motorName)
        if motor != None:
            motor.clockwise()

    def counterClockwise(self, motorName):
        self.disableStby()
        motor = self.getMotorByName(motorName)
        if motor != None:
            motor.counterClockwise()

    def stopMotor(self, motorName):
        motor = self.getMotorByName(motorName)
        if motor != None:
            motor.stopMotor()

    def updateMotorTargetLocation(self, motorName, newTarget):
        motor = self.getMotorByName(motorName)
        if motor != None:
            motor.updateTargetLocation(newTarget)

    def getTargetReachedMotor(self, motorName):
        motor = self.getMotorByName(motorName)
        if motor != None:
            return motor.getTargetReached()

    def update(self, time):
        for motor in self.motors:
            motor.update(time)

class motor:
    def __init__(self, name, pwm, in1, in2, minLimit, maxLimit, travelSpeed, startLocation):
        #store variables
        self.name = name
        self.pwm = pwm
        self.in1 = in1
        self.in2 = in2
        self.location = startLocation
        self.maxLimit = maxLimit
        self.minLimit = minLimit
        self.travelSpeed = travelSpeed
        self.target = 0
        self.direction = 0
        self.targetReached = False

        #initialise pins
        GPIO.setup(self.pwm, GPIO.OUT) # conected to PWMA
        GPIO.setup(self.in1, GPIO.OUT) # IN1
        GPIO.setup(self.in2, GPIO.OUT) # IN2

    def clockwise(self):
        self.direction = 1
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)
        GPIO.output(self.pwm, GPIO.HIGH)

    def counterClockwise(self):
        self.direction = -1
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.pwm, GPIO.HIGH)

    def stopMotor(self):
        self.direction = 0
        GPIO.output(self.pwm, GPIO.LOW)

    def updateTargetLocation(self, newTarget):
        self.target = newTarget
        self.targetReached = False

    def getTargetReached(self):
        return self.targetReached

    def update(self, time):
        print( "travelSpeed: "+str(self.travelSpeed))
        print("direction: " + str(self.direction))
        print("time: " + str(time))
        print( "add: "+str(float(self.travelSpeed * self.direction * time)))

        self.location = self.location + self.travelSpeed * self.direction * time
        #check if value is within 1 degree of target. If it is stop motors
        if(self.location < self.target - .001 or self.location > self.target + .001):
            if(self.location - self.target > 0):
                print("clockwise")
                self.clockwise()
            else:
                print("counter clockwise")
                self.counterClockwise()
        else:
            
            self.targetReached = True
            self.stopMotor()
        # If location is out of limits stop motors
        if(self.location > self.maxLimit or self.location < self.minLimit):
            self.stopMotor()
