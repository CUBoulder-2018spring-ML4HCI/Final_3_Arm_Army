#!/usr/bin/env python

#Import needed items
import time 
import RPi.GPIO as GPIO


#Declare the GPIO Settings 
GPIO.setmode(GPIO.BOARD)

#set up GPIO pins 
GPIO.setup(7, GPIO.OUT)  #conected to PWMA
GPIO.setup(11, GPIO.OUT) # AIN2
GPIO.setup(12, GPIO.OUT) # AIN1
GPIO.setup(13, GPIO.OUT)

# Drive Motor Clockwise
GPIO.output(12,GPIO.LOW)
GPIO.output(11, GPIO.HIGH)


GPIO.output(7, GPIO.HIGH)


GPIO.output(13, GPIO.HIGH)

time.sleep(.75)

#Counter Clockwise
GPIO.output(12,GPIO.HIGH)
GPIO.output(11, GPIO.LOW)
time.sleep(.5)

#Free up pins
GPIO.cleanup()
