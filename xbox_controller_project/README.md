# Xbox Controller Robot Control

This program allows you to control your robot using an Xbox controller and measure the distance traveled by both drive and attachment motors.

## Robot Configuration

Based on `robot_info.md`:
- **Left wheel motor:** Port C
- **Right wheel motor:** Port D  
- **Left attachment motor:** Port E
- **Right attachment motor:** Port F
- **Wheel diameter:** 5.6 cm
- **Axle track:** 8 cm

## Controls

### Movement
- **D-pad Up:** Move forward
- **D-pad Down:** Move backward
- **No turning controls** (as requested)

### Attachment Motors
- **L1 (Left Bumper):** Run left attachment motor forward
- **L2 (Left Trigger):** Run left attachment motor backward (analog trigger, activates when pressed > 10%)
- **R1 (Right Bumper):** Run right attachment motor forward
- **R2 (Right Trigger):** Run right attachment motor backward (analog trigger, activates when pressed > 10%)

### Measurement Controls
- **A Button:** Print current distances and reset all measurements
- **X Button:** Exit controller mode

## Features

- **Distance Tracking:** Measures distance traveled by drive motors in millimeters
- **Angle Tracking:** Measures rotation of drive base in degrees
- **Attachment Tracking:** Measures rotation of both attachment motors in degrees
- **Reset Function:** Easy reset of all measurements with A button
- **Visual Feedback:** Hub LED indicates connection status and operation mode
- **Audio Feedback:** Beeps for connection status and button presses
- **Controller Feedback:** Rumble feedback for button presses

## LED Status Indicators

- **Red Blinking:** Attempting to connect to controller
- **Red Solid:** Connection failed
- **Green:** Controller connected successfully  
- **Blue:** Controller active and ready
- **Orange:** Program starting

## Usage

1. Run the program on your robot
2. The program will attempt to connect to an Xbox controller
3. Once connected, use the controls as described above
4. Press A at any time to see current measurements and reset them
5. Press X to exit the program

## Configuration

All robot settings are now centralized in `robot_config.py`:

### Speed Settings
- **Drive Speed:** 300 mm/s
- **Attachment Speed:** 500 degrees/s
- **Drive Acceleration:** 1000 mm/s²
- **Turn Rate:** 60 degrees/s (reasonable default, not used for D-pad control)
- **Turn Acceleration:** 120 degrees/s² (reasonable default, not used for D-pad control)

### Robot Specifications
- **Wheel Diameter:** 56 mm (5.6 cm)
- **Axle Track:** 80 mm (8 cm)

### Motor Ports and Directions
- **Left Wheel:** Port C (Counterclockwise)
- **Right Wheel:** Port D (Clockwise)
- **Left Attachment:** Port E (Clockwise)
- **Right Attachment:** Port F (Clockwise)

You can modify these values in `robot_config.py` to customize the robot behavior without touching the main program logic.
