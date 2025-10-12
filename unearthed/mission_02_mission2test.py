"""
Mission 2: mission2Test
mission2Test
"""

from robot_controller import RobotController
from display_patterns import DisplayPatterns
from season_config import SeasonDefaults

# Mission-specific configuration
# You can override any settings from SeasonDefaults here
MISSION_CONFIG = {
    "drive_speed": 200,      # Speed in mm/s
    "turn_rate": 60,          # Turn speed in degrees/s
    # Add more custom settings as needed, like:
    # "target_distance": 500,
    # "pause_time": 1000,
}

def run():
    """Main mission execution function"""
    print("=== Mission 2: mission2Test ===")

    robot = RobotController(SeasonDefaults, MISSION_CONFIG)

    try:
        # Step 1: Initialize the robot
        robot.initialize()

        # Step 2: Set up display (optional)
        display = DisplayPatterns(robot.hub)

        # Step 3: Signal mission start (beep + light)
        robot.mission_start_signal()

        # ============================================================
        # TODO: ADD YOUR MISSION LOGIC HERE
        # ============================================================

        # HELPFUL EXAMPLES - Delete these comments when you're ready!

        # --- BASIC DRIVING ---
        # Most missions just need these simple movements:

        # Drive straight forward 300mm:
        #   robot.drivebase.straight(300)
        #
        # Drive backward 200mm (use negative number):
        #   robot.drivebase.straight(-200)
        #
        # Turn right 90 degrees:
        #   robot.drivebase.turn(90)
        #
        # Turn left 90 degrees (use negative number):
        #   robot.drivebase.turn(-90)
        #
        # Example mission - drive to target and back:
        #   robot.drivebase.straight(500)    # Drive forward 500mm
        #   robot.drivebase.turn(180)        # Turn around
        #   robot.drivebase.straight(500)    # Drive back 500mm

        # --- WAITING ---
        # Wait 2 seconds (2000 milliseconds):
        #   from pybricks.tools import wait
        #   wait(2000)

        # --- ATTACHMENTS (if you have them) ---
        # Run attachment motor at 500 deg/s:
        #   if robot.left_attachment:
        #       robot.left_attachment.run(500)
        #       from pybricks.tools import wait
        #       wait(1000)  # Run for 1 second
        #       robot.left_attachment.stop()
        #
        # Move attachment to specific angle:
        #   if robot.right_attachment:
        #       robot.right_attachment.run_angle(500, 90)  # Turn 90 degrees

        # --- DISPLAY (optional) ---
        # Show a number on the display:
        #   robot.hub.display.number(5)
        #
        # Show scrolling text:
        #   robot.hub.display.text("GO!")
        #
        # Show countdown before starting:
        #   display.show_countdown(3)
        #
        # Show checkmark when done:
        #   display.show_completion_checkmark()

        # --- SENSORS (if you have them) ---
        # Check which side is facing up:
        #   up_side = robot.hub.imu.up()
        #   print(f"Up side: {up_side}")
        #
        # Get tilt angles:
        #   pitch, roll = robot.hub.imu.tilt()
        #   print(f"Pitch: {pitch}, Roll: {roll}")

        # --- COMPLETE MISSION EXAMPLE ---
        # Here's a complete mission - drive forward, turn, and come back:
        #   from pybricks.tools import wait
        #   display.show_countdown(3)               # Count down 3-2-1
        #   robot.drivebase.straight(500)           # Drive forward 500mm
        #   robot.drivebase.turn(90)                # Turn right 90 degrees
        #   robot.drivebase.straight(300)           # Drive forward 300mm
        #   wait(1000)                               # Pause 1 second
        #   robot.drivebase.turn(180)               # Turn around
        #   robot.drivebase.straight(300)           # Drive back 300mm
        #   robot.drivebase.turn(90)                # Turn left 90 degrees
        #   robot.drivebase.straight(500)           # Return to start
        #   display.show_completion_checkmark()     # Show success!

        # --- ADVANCED: PREDEFINED SHAPES (optional) ---
        # If you want to drive in shapes, you can use ShapeMovements:
        #   from shape_movements import ShapeMovements
        #   movements = ShapeMovements(robot)
        #   movements.drive_square(side_length=300)
        #   movements.drive_circle(radius=200)
        #   movements.drive_triangle(side_length=300)

        # DELETE THIS when you add your code:
        print("Mission logic not implemented yet!")
        print("Edit this file and add your robot movements above.")

        # ============================================================
        # END OF MISSION LOGIC
        # ============================================================

        # Step 4: Signal success (beep + green light)
        robot.mission_success_signal()
        print("Mission 2 completed successfully!")

    except Exception as e:
        # If something goes wrong, show error
        print(f"Mission {MISSION_NUM} failed: {e}")
        robot.mission_error_signal()
        raise e

    finally:
        # Always clean up (stop motors, turn off lights)
        robot.cleanup()

# This lets you test the mission by running this file directly
if __name__ == "__main__":
    run()
