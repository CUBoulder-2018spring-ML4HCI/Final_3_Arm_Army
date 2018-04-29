import serial
import time
import OSC

send_address = '127.0.0.1', 6448

PORT="/dev/cu.usbmodem1412"
BAUD = 115200

c = OSC.OSCClient()
c.connect( send_address )

while True:
    s= serial.Serial(PORT)
    s.baudrate= BAUD
    datax = s.readline()
    #print(datax)
    intx = datax.split(", ")
    str(intx[2]).replace("\r\n","")
    #print(intx)
    if (len(intx)==3):
        try:
            #check if values can be converted to float
            x=float(intx[0])
            y=float(intx[1])
            z=float(intx[2])
            print (x, y, z)
            rNum = OSC.OSCMessage()
            rNum.setAddress("/wek/inputs")
            #append values to osc message
            rNum.append(x)
            rNum.append(y)
            rNum.append(z)
            c.send(rNum)
        except ValueError:
            #if they cant be flaots than skip over to the next value 
            continue

    #print(x)
    

#    datax = str(datax[0:3])
#    datay = s.readline()
#    datay = str(datay[5:8])
#    dataz = s.readline()
#    dataz = str(dataz[9:12])
#print(datax)
#    time.sleep(.01)

