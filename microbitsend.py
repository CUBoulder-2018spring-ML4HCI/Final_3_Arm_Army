from microbit import *
import radio

radio.on()

radio.config(channel=19)
radio.config(power=7)

while True:
        acc_x=accelerometer.get_x()
        acc_y=accelerometer.get_y()
        acc_z=accelerometer.get_z()
        radio.send(str(acc_x) + ", " + str(acc_y) + ", " + str(acc_z) + "\n")
