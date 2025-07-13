
from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Button, Color, Direction, Port, Stop
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from supportcode import launch_LegoRemote, launch_XBOX, next_program, prior_program

# Set up all devices.
HUB = PrimeHub(top_side=-Axis.X, front_side=Axis.Z, broadcast_channel=0, observe_channels=[1])
Left_Color_Sensor = ColorSensor(Port.E)
Right_Color_Sensor = ColorSensor(Port.F)
Left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Right_Motor = Motor(Port.B, Direction.CLOCKWISE)
DRIVE_BASE = DriveBase(Left_motor, Right_Motor, 88, 128)
LEFT_ATTACHMENT = Motor(Port.C, Direction.CLOCKWISE)
RIGHT_ATTACHMENT = Motor(Port.D, Direction.CLOCKWISE)

# Initialize variables.
ACTIVEPROGRAM = 0
SPEED = 620
ACELLERATION = 500
TURN_SPEED = 300
TURN_ACCELERATION = 500
PROGRAM_LIST = ['C', 'S', 'T', 'R', '1']

def Circle():
    # Turn button yellow; and beep/wait so hands are out of the way
    HUB.light.on(Color.YELLOW)
    HUB.speaker.beep(500, 300)
    # Turn on Gyro, drive forward
    DRIVE_BASE.use_gyro(True)
    DRIVE_BASE.straight(250)
    # Drive in a circle using the curve command
    DRIVE_BASE.curve(200, 360)
    # Turn off Gyro and drive/coast back home
    DRIVE_BASE.use_gyro(False)
    DRIVE_BASE.straight(-245, Stop.COAST)

def Square():
    # Turn button yellow; and beep/wait so hands are out of the way
    HUB.light.on(Color.YELLOW)
    HUB.speaker.beep(500, 300)
    # Turn on Gyro, drive forward
    DRIVE_BASE.use_gyro(True)
    DRIVE_BASE.straight(150)
    # Drive in a square
    for count in range(4):
        DRIVE_BASE.straight(300)
        DRIVE_BASE.turn(90)
    # Turn off Gyro and drive/coast back home
    DRIVE_BASE.use_gyro(False)
    DRIVE_BASE.straight(-145, Stop.COAST)

def Triangle():
    # Turn button yellow; and beep/wait so hands are out of the way
    HUB.light.on(Color.YELLOW)
    HUB.speaker.beep(500, 300)
    # Turn on Gyro, drive forward
    DRIVE_BASE.use_gyro(True)
    DRIVE_BASE.straight(150)
    # Drive in a triangle
    for count2 in range(3):
        DRIVE_BASE.straight(300)
        DRIVE_BASE.turn(120)
    # Turn off Gyro and drive back home
    DRIVE_BASE.use_gyro(False)
    DRIVE_BASE.straight(-145, Stop.COAST)


# The main program starts here.
# To use this code you will have to change the setup blocks to fit your
# Robot's configuration. You will likely have a different hub orietation
# as the hub in this code is oriented vertically facing backward
# (very atypical for FLL) as well as the wheel diameter and spacing in mm
# First make it so the robot does not stop when center button is pressed instead it will have to be held down
HUB.system.set_stop_button(None)
# Override default drivebase settings. The default pybricks settings
#  tend to have too little max speed (slower than necessary)
#  and too high of an acceleration (wheels slip/inacurate movements)
DRIVE_BASE.settings(straight_speed=SPEED)
DRIVE_BASE.settings(straight_acceleration=ACELLERATION)
DRIVE_BASE.settings(turn_rate=TURN_SPEED)
DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
# Main loop/interface that allows for selecting and launching programs
while True:
    # Display the active program
    HUB.display.char(PROGRAM_LIST[ACTIVEPROGRAM])
    # Turn the light green
    HUB.light.on(Color.GREEN)
    if Button.LEFT in HUB.buttons.pressed():
        # The left button goes back to the previous program
        ACTIVEPROGRAM = prior_program(ACTIVEPROGRAM, PROGRAM_LIST)
        HUB.speaker.beep(500, 200)
    elif Button.RIGHT in HUB.buttons.pressed():
        # The right button advances to the next program
        ACTIVEPROGRAM = next_program(ACTIVEPROGRAM, PROGRAM_LIST)
        HUB.speaker.beep(500, 200)
    elif Button.CENTER in HUB.buttons.pressed():
        # The center button launches the currently selected program
        # Note you can also have this be the bluetooth button/other buttons do this as well
        if 'R' in PROGRAM_LIST[ACTIVEPROGRAM]:
            # XBOX Mode
            launch_XBOX(HUB, DRIVE_BASE, LEFT_ATTACHMENT, RIGHT_ATTACHMENT)
            DRIVE_BASE.settings(straight_speed=SPEED)
            DRIVE_BASE.settings(straight_acceleration=ACELLERATION)
            DRIVE_BASE.settings(turn_rate=TURN_SPEED)
            DRIVE_BASE.settings(turn_acceleration=TURN_ACCELERATION)
        elif 'S' in PROGRAM_LIST[ACTIVEPROGRAM]:
            # Drive in Square
            Square()
        elif 'T' in PROGRAM_LIST[ACTIVEPROGRAM]:
            # Drive in Triangle
            Triangle()
        elif 'C' in PROGRAM_LIST[ACTIVEPROGRAM]:
            # Drive in Circle
            Circle()
        elif '1' in PROGRAM_LIST[ACTIVEPROGRAM]:
            # Empty program  cslot an add as many additional
            # conditionals/slots as needed.
            pass
        else:
            pass
    else:
        wait(10)