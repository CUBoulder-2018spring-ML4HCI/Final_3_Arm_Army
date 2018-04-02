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
    - Pushing to teopest on Raspberry Pi
    - Got OSC messages to be received from computer

### Python OSC
  - Created a simple Python OSC Client that forwards messages to Wekinator

### Kinect & Processing
  We created a 2 class classifier that detects if the user's left arm is reaching up towards his or her left shoulder.
  - Experimented with inputs from Kinect and used [SimpleOpenNI](https://github.com/wexstorm/simple-openni), a library that tracks body joints and angles.
  - Used Processing to get Kinect Data and forwarded info to Wekinator
    - Planning to forward classification Wekinator provides to our Python OSC component to drive the motors

We experimented with Kinect because we thought that our robotic helper hand would fit perfectly on one's shoulder. Kinect would allow us to sense when a user is reaching for a the arm sitting on his or her shoulder by measuring the angle of the elbow.

Cleaned up demo to work correctly with the Raspberry Pi and OSC messages. Currently one motor is being driven, and now the rest of the motors will be bootstrapped forward with the classes we already wrote.

[Kinect Classification Video](https://www.youtube.com/watch?v=aPeoNjqThVM)
