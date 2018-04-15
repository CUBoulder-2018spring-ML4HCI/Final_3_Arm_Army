# Step 1
If you haven't used the code before go into the Microbit directory and open up the xcode project. This will just get xcode to 
install some of the packages that you need and it helped my microbit to stop disconnecting from my computer after a couple
of minutes.

# Step 2
Run the executable in the parent directory where 57120 is the port that you want to use. Probably 57120 if you don't want to 
change the python file code.
./CBMicroBit 57120 true

# Step 3
Connect the Microbit to your computer with a micro-usb cable. Drag the hex file from the same directory onto the microbit to 
get the microbit connected. 

# Step 4 
At this point, the microbit should be connected to the computer and running. Now you can run the ConvertOSC.py file from the 
PythonOSC folder. This will convert the OSC messages that are being received to an array that only has [x, y, z] accelerometer
values. 
