from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Button
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Initialize the Hub
hub = PrimeHub()

# Initialize both motors.
# The motor on the left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

# Initialize the drive base.
# Wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 80mm.
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)

# Set initial speed
speed = 200
drive_base.drive(speed, 0)

# Run until the program is stopped
while True:
    # Check which buttons are pressed
    pressed = hub.buttons.pressed()

    # If right button is pressed, increase speed
    if Button.RIGHT in pressed:
        speed += 50
        drive_base.drive(speed, 0)
        # Wait until button is released
        while Button.RIGHT in hub.buttons.pressed():
            wait(10)

    # If left button is pressed, decrease speed
    if Button.LEFT in pressed:
        speed -= 50
        if speed < 0:
            speed = 0
        drive_base.drive(speed, 0)
        # Wait until button is released
        while Button.LEFT in hub.buttons.pressed():
            wait(10)
    
    # If speed is 0, stop the robot
    if speed == 0:
        drive_base.stop()

    wait(10)
