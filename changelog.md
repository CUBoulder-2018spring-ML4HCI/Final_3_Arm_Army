# Changelog

## Week 1 - 3/19

### Finalized idea
We decided we will be creating a robotic arm that has a set of pre made motions that will be triggered by the users trained gesture. We submitted our revised project proposal.

### Research and Design
- Added example code for motor driver
  - Added classes for motorDriver, motor
  - Outline for armDriver class
  - Tested Kinect functionality with Processing
  - Wrote Python Script to send OSC


## Week 2 - 3/26
### Arm Development
  - Fixed classes to drive the motor constantly
    - Will add OSC next to allow us to drive the motor from a different program
  - Added basic OSC forwarding to the arm driver ```armDriver/arm.py```
    - Pushing to test on Raspberry Pi
    - Got OSC messages to be received from computer
### Python OSC
  - Created a simple Python OSC Client that forwards messages to Wekinator

Cleaned up demo to work correctly with the Raspberry Pi and OSC messages. Currently one motor is being driven, and now the rest of the motors will be boostrapped forward with the classes we already wrote.
