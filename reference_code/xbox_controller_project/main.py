"""
Xbox Controller Robot Control Program
Controls drive and attachment motors with distance measurement

Controls:
- D-pad Up/Down: Forward/Backward movement
- L1/L2 (LB/LT): Left attachment movement  
- R1/R2 (RB/RT): Right attachment movement
- A button: Print distances and reset measurements
- X button: Exit controller mode
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Axis, Button, Color, Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.iodevices import XboxController

from robot_config import Ports, Directions, Specifications, ControllerSettings

# Set up all devices using robot_config
hub = PrimeHub()
left_wheel = Motor(Ports.LEFT_WHEEL, Directions.LEFT_WHEEL)
right_wheel = Motor(Ports.RIGHT_WHEEL, Directions.RIGHT_WHEEL)
left_attachment = Motor(Ports.LEFT_ATTACHMENT, Directions.LEFT_ATTACHMENT)
right_attachment = Motor(Ports.RIGHT_ATTACHMENT, Directions.RIGHT_ATTACHMENT)

# Create drivebase using specifications from config
drivebase = DriveBase(left_wheel, right_wheel, Specifications.WHEEL_DIAMETER, Specifications.AXLE_TRACK)

# Global controller variable
controller = None

def setup_controller():
    """Initialize Xbox controller connection"""
    global controller
    hub.light.blink(Color.RED, [200, 200])
    hub.speaker.beep(500, 100)
    print("Connecting to Xbox controller...")
    
    try:
        controller = XboxController()
        hub.light.on(Color.GREEN)
        hub.speaker.beep(800, 200)
        print("Controller connected successfully!")
        return True
    except Exception as e:
        hub.light.on(Color.RED)
        hub.speaker.beep(200, 500)
        print(f"Failed to connect controller: {e}")
        return False

def reset_measurements():
    """Reset all distance measurements"""
    drivebase.reset()
    left_attachment.reset_angle(0)
    right_attachment.reset_angle(0)
    print("Measurements reset")

def print_distances():
    """Print current distance measurements"""
    print(f"Drive distance: {drivebase.distance()} mm")
    print(f"Drive angle: {drivebase.angle()} degrees")
    print(f"Left attachment: {left_attachment.angle()} degrees")
    print(f"Right attachment: {right_attachment.angle()} degrees")

def controller_loop():
    """Main controller loop"""
    # Use controller settings from config
    drive_speed = ControllerSettings.DRIVE_SPEED
    attachment_speed = ControllerSettings.ATTACHMENT_SPEED
    
    # Set drivebase settings using config values
    drivebase.settings(
        straight_speed=drive_speed,
        straight_acceleration=ControllerSettings.DRIVE_ACCELERATION,
        turn_rate=ControllerSettings.TURN_RATE,
        turn_acceleration=ControllerSettings.TURN_ACCELERATION
    )
    drivebase.use_gyro(True)
    
    # Reset measurements at start
    reset_measurements()
    
    print("Controller active! Use D-pad for movement, L1/L2 and R1/R2 for attachments")
    print("Press A to print distances, X to exit")
    
    while True:
        hub.light.on(Color.BLUE)
        
        # Get button presses
        buttons = controller.buttons.pressed()
        
        # Check for special buttons first
        if Button.A in buttons:
            print_distances()
            reset_measurements()
            controller.rumble(50, 200)
            hub.speaker.beep(500, 100)
            wait(300)  # Prevent multiple rapid presses
            
        elif Button.X in buttons:
            print("Exiting controller mode")
            drivebase.use_gyro(False)
            drivebase.brake()
            left_attachment.brake()
            right_attachment.brake()
            controller.rumble(50, 200)
            hub.speaker.beep(500, 100)
            break
        
        # Drive control using D-pad (no turning)
        drive_active = False
        if Button.UP in buttons:
            drivebase.drive(drive_speed, 0)  # Forward
            drive_active = True
        elif Button.DOWN in buttons:
            drivebase.drive(-drive_speed, 0)  # Backward
            drive_active = True
        
        if not drive_active:
            drivebase.brake()
        
        # Get trigger values (analog inputs)
        left_trigger, right_trigger = controller.triggers()
        
        # Left attachment control using L1/L2
        left_attachment_active = False
        if Button.LB in buttons:  # L1 - Left bumper
            left_attachment.run(attachment_speed)
            left_attachment_active = True
        elif left_trigger > 10:  # L2 - Left trigger (analog threshold)
            left_attachment.run(-attachment_speed)
            left_attachment_active = True
        
        if not left_attachment_active:
            left_attachment.brake()
        
        # Right attachment control using R1/R2
        right_attachment_active = False
        if Button.RB in buttons:  # R1 - Right bumper
            right_attachment.run(attachment_speed)
            right_attachment_active = True
        elif right_trigger > 10:  # R2 - Right trigger (analog threshold)
            right_attachment.run(-attachment_speed)
            right_attachment_active = True
        
        if not right_attachment_active:
            right_attachment.brake()
        
        wait(10)  # Small delay for smooth operation

def main():
    """Main program"""
    hub.light.on(Color.ORANGE)
    print("Xbox Controller Robot Control Starting...")
    
    # Try to connect to controller
    if setup_controller():
        controller_loop()
    else:
        print("Failed to connect to controller. Exiting.")
        hub.light.on(Color.RED)
        return
    
    # Cleanup
    hub.light.on(Color.GREEN)
    print("Program ended")

if __name__ == "__main__":
    main()
