"""
Mission {MISSION_NUM}: {MISSION_NAME}
{MISSION_DESCRIPTION}
"""

from robot_controller import RobotController
from display_patterns import DisplayPatterns
from shape_movements import ShapeMovements
from season_config import SeasonDefaults

# Mission-specific configuration
# You can override any settings from SeasonDefaults here
MISSION_CONFIG = {
    "drive_speed": {DRIVE_SPEED},      # Speed in mm/s
    "turn_rate": {TURN_RATE},          # Turn speed in degrees/s
    # Add more custom settings as needed, like:
    # "target_distance": 500,
    # "pause_time": 1000,
}

def run():
    """Main mission execution function"""
    print("=== Mission {MISSION_NUM}: {MISSION_NAME} ===")

    robot = RobotController(SeasonDefaults, MISSION_CONFIG)

    try:
        # Step 1: Initialize the robot
        robot.initialize()

        # Step 2: Set up your utilities
        display = DisplayPatterns(robot.hub)
        movements = ShapeMovements(robot)

        # Step 3: Signal mission start (beep + light)
        robot.mission_start_signal()

        # ============================================================
        # TODO: ADD YOUR MISSION LOGIC HERE
        # ============================================================

        # HELPFUL EXAMPLES - Delete these comments when you're ready!

        # --- DRIVING EXAMPLES ---
        # Drive straight forward 300mm:
        #   movements.drivebase.straight(300)
        #
        # Drive backward 200mm:
        #   movements.drivebase.straight(-200)
        #
        # Turn right 90 degrees:
        #   movements.drivebase.turn(90)
        #
        # Turn left 90 degrees:
        #   movements.drivebase.turn(-90)
        #
        # Drive in a square:
        #   movements.drive_square(side_length=300)
        #
        # Drive in a circle:
        #   movements.drive_circle(radius=200)
        #
        # Drive in a triangle:
        #   movements.drive_triangle(side_length=300)

        # --- DISPLAY EXAMPLES ---
        # Show a number on the display:
        #   robot.hub.display.number(5)
        #
        # Show scrolling text:
        #   robot.hub.display.text("GO!")
        #
        # Show countdown:
        #   display.show_countdown(3)
        #
        # Animate a square pattern:
        #   display.animate_square(cycles=3)
        #
        # Show checkmark when done:
        #   display.show_completion_checkmark()

        # --- WAITING ---
        # Wait 2 seconds (2000 milliseconds):
        #   from pybricks.tools import wait
        #   wait(2000)

        # --- ATTACHMENTS (if you have them) ---
        # Run attachment motor at 500 deg/s:
        #   if robot.left_attachment:
        #       robot.left_attachment.run(500)
        #       wait(1000)  # Run for 1 second
        #       robot.left_attachment.stop()
        #
        # Move attachment to specific angle:
        #   if robot.right_attachment:
        #       robot.right_attachment.run_angle(500, 90)  # Turn 90 degrees

        # --- SENSORS (if you have them) ---
        # Check which side is facing up:
        #   up_side = robot.hub.imu.up()
        #   print(f"Up side: {up_side}")
        #
        # Get tilt angles:
        #   pitch, roll = robot.hub.imu.tilt()
        #   print(f"Pitch: {pitch}, Roll: {roll}")

        # --- COMBINING ACTIONS ---
        # You can do multiple things in sequence:
        #   display.show_countdown(3)
        #   movements.drivebase.straight(500)
        #   movements.drivebase.turn(90)
        #   movements.drivebase.straight(500)
        #   display.show_completion_checkmark()

        # DELETE THIS when you add your code:
        print("Mission logic not implemented yet!")
        print("Edit this file and add your robot movements above.")

        # ============================================================
        # END OF MISSION LOGIC
        # ============================================================

        # Step 4: Signal success (beep + green light)
        robot.mission_success_signal()
        print("Mission {MISSION_NUM} completed successfully!")

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
