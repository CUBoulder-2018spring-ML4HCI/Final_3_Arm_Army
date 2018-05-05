# Final_3_Arm_Army

## Run the Arm 
 In order to run the arm a few python packages need to be installed:
 ```sudo apt-get -y install python-rpi.gpio``` and
 ```pip3 install python-osc```
 
 We also set the Raspberry Pi to have a static IP of 192.168.2.9. Clone this git repo to the Pi. Cd in to the armDriver code with:
 ```cd Final_3_Arm_Army/armDriver/```
 
 Next start the arm driver code with.
 ```python3 demoArm.py```
 
 Currently the ```arm.py``` has an issue with not updating the location of the motor causing the step program from running correctly. This is why we need to run the ```demoArm.py``` script. This scrip receives a signal from Wekinator and then updates the state. Both of these scripts has a game loop that change the motors actions depending on the state.
 
 ## Setting Up Wekinator
 1. Open Wekinator 
 2. Start a New project
 3. Change the ```# inputs``` to 3
 4. Change the ```Host (IP address or name)``` to the IP if the Pi. In our case 192.168.2.9
 5. Change the ```type``` to All Dynamic Time Warping (default settings)
 6. Change the number of gestures to 4
 7. Click Next
 
 
 ## Starting Up GUI
 On the same computer as wekinator you need to open up the GUI. Go in to the Electron directory that contains the GUI: ```cd Final_3_Arm_Army/Electron/ArmGUI/``` 
 
 Once in this folder we need to install the dependencies with ```npm install```
 
 Also go into the app directory and run ```npm install```
 
 Then go back into the ArmGUI directory and start the GUI with: ```npm run dev``` you can close the debug window once the GUI opens.
 
 Now a user can train their mappings and start the project with the GUI. Before training Wekinator must be open. 
 
 
 ## MicroBit
 

## [Video Demonstration](https://www.youtube.com/watch?v=2I-ou1PnAPc&feature=youtu.be)
## [Final Report](https://github.com/CUBoulder-2018spring-ML4HCI/Final_3_Arm_Army/blob/master/ML%20Project%20Report.pdf)
