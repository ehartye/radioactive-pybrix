"""
Simple test program to verify all motors are working correctly
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from robot_config import Ports, Directions, Specifications

# Set up all devices using robot_config
hub = PrimeHub()
left_wheel = Motor(Ports.LEFT_WHEEL, Directions.LEFT_WHEEL)
right_wheel = Motor(Ports.RIGHT_WHEEL, Directions.RIGHT_WHEEL)
left_attachment = Motor(Ports.LEFT_ATTACHMENT, Directions.LEFT_ATTACHMENT)
right_attachment = Motor(Ports.RIGHT_ATTACHMENT, Directions.RIGHT_ATTACHMENT)

# Create drivebase using specifications from config
drivebase = DriveBase(left_wheel, right_wheel, Specifications.WHEEL_DIAMETER, Specifications.AXLE_TRACK)

def test_drive_motors():
    """Test drive motors"""
    print("Testing drive motors...")
    hub.light.on(Color.YELLOW)
    
    # Test forward
    print("Moving forward...")
    drivebase.straight(100)
    wait(1000)
    
    # Test backward  
    print("Moving backward...")
    drivebase.straight(-100)
    wait(1000)
    
    print("Drive motors test complete")

def test_attachment_motors():
    """Test attachment motors"""
    print("Testing attachment motors...")
    hub.light.on(Color.CYAN)
    
    # Test left attachment
    print("Testing left attachment...")
    left_attachment.run_angle(200, 180)
    wait(500)
    left_attachment.run_angle(200, -180)
    wait(500)
    
    # Test right attachment
    print("Testing right attachment...")
    right_attachment.run_angle(200, 180)
    wait(500)
    right_attachment.run_angle(200, -180)
    wait(500)
    
    print("Attachment motors test complete")

def main():
    """Main test program"""
    hub.light.on(Color.GREEN)
    print("Motor Test Program")
    print("Press center button to start drive motor test")
    
    # Wait for button press
    while True:
        if Button.CENTER in hub.buttons.pressed():
            break
        wait(10)
    
    test_drive_motors()
    
    print("Press center button to start attachment motor test")
    
    # Wait for button press
    while True:
        if Button.CENTER in hub.buttons.pressed():
            break
        wait(10)
    
    test_attachment_motors()
    
    hub.light.on(Color.GREEN)
    print("All tests complete!")

if __name__ == "__main__":
    main()
