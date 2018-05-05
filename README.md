# Final_3_Arm_Army

## Run the Arm 
 In order to run the arm a few python packages need to be installed:
 ```sudo apt-get -y install python-rpi.gpio```
 ```pip3 install python-osc```
 
 We also set the Raspberry Pi to have a static IP of 192.168.2.9. Clone this git repo to the Pi. Cd in to the armDriver code with:
 ```cd Final_3_Arm_Army/armDriver/```
 
 Next start the arm driver code with.
 ```python3 demoArm.py```
 
 Currently the ```arm.py``` has an issue with not updating the location of the motor causing the step program from running correctly. This is why we need to run the ```demoArm.py``` script. This scrip receives a signal from Wekinator and then up dates the state. Both of these scripts has a game loop that change the motors actions depending on the state.
 
 
