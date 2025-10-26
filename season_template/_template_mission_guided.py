"""
Mission {MISSION_NUM}: {MISSION_NAME}
{MISSION_DESCRIPTION}
"""

# Mission-specific configuration
# You can override any settings from SeasonDefaults here
# The menu system will use these settings when initializing the robot
MISSION_CONFIG = {{
    "drive_speed": {DRIVE_SPEED},      # Speed in mm/s
    "turn_rate": {TURN_RATE},          # Turn speed in degrees/s
    # Add more custom settings as needed, like:
    # "target_distance": 500,
    # "pause_time": 1000,
}}

def run(robot):
    """
    Main mission execution function

    Args:
        robot: RobotController object (already initialized and ready to use!)

    The robot is already initialized with your MISSION_CONFIG settings above.
    Just write your robot movements and logic below!

    Access display helper through robot.display for visual feedback.
    """
    print("=== Mission {MISSION_NUM}: {MISSION_NAME} ===")

    # ========================================
    # QUICK START - Copy one to begin:
    # ========================================
    #   robot.drivebase.straight(500)    # Drive forward 500mm
    #   robot.drivebase.straight(-300)   # Drive backward 300mm
    #   robot.drivebase.turn(90)         # Turn right 90 degrees
    #   robot.drivebase.turn(-90)        # Turn left 90 degrees

    # TODO: ADD YOUR MISSION LOGIC HERE

    # ========================================
    # MORE EXAMPLES BELOW (scroll down):
    # ========================================

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
        #   robot.display.show_countdown(3)
        #
        # Show checkmark when done:
        #   robot.display.show_completion_checkmark()

        # --- SENSORS (if you have them) ---
        # Check which side is facing up:
        #   up_side = robot.hub.imu.up()
        #   print(f"Up side: {{up_side}}")
        #
        # Get tilt angles:
        #   pitch, roll = robot.hub.imu.tilt()
        #   print(f"Pitch: {{pitch}}, Roll: {{roll}}")

        # --- COMPLETE MISSION EXAMPLE ---
        # Here's a complete mission - drive forward, turn, and come back:
        #   from pybricks.tools import wait
        #   robot.display.show_countdown(3)         # Count down 3-2-1
        #   robot.drivebase.straight(500)           # Drive forward 500mm
        #   robot.drivebase.turn(90)                # Turn right 90 degrees
        #   robot.drivebase.straight(300)           # Drive forward 300mm
        #   wait(1000)                               # Pause 1 second
        #   robot.drivebase.turn(180)               # Turn around
        #   robot.drivebase.straight(300)           # Drive back 300mm
        #   robot.drivebase.turn(90)                # Turn left 90 degrees
        #   robot.drivebase.straight(500)           # Return to start
        #   robot.display.show_completion_checkmark()    # Show success!

        # --- ADVANCED: LINE FOLLOWING (if you have color sensors) ---
        # Drive forward until both sensors detect a black line:
        #   from line_movements import LineMovements
        #
        #   # Create line movements helper
        #   line_moves = LineMovements(robot)
        #
        #   # Drive until both sensors see black line (uses robot's sensors automatically!)
        #   line_moves.square_on_line()
        #
        #   # With custom speed (slower for precision)
        #   line_moves.square_on_line(drive_speed=80)
        #
        #   # With custom threshold (more sensitive to black)
        #   line_moves.square_on_line(black_threshold=25)

    # DELETE THIS when you add your code:
    print("Mission logic not implemented yet!")
    print("Edit this file and add your robot movements above.")

    # ============================================================
    # END OF MISSION LOGIC
    # ============================================================

# This lets you test the mission by running this file directly
if __name__ == "__main__":
    # For standalone testing, we need to set up the robot ourselves
    from robot_controller import RobotController
    from season_config import SeasonDefaults

    robot = RobotController(SeasonDefaults, MISSION_CONFIG)

    try:
        robot.initialize()
        robot.mission_start_signal()

        # Run the mission (display is accessible via robot.display)
        run(robot)

        robot.mission_success_signal()
        print("Mission {MISSION_NUM} completed successfully!")

    except Exception as e:
        print("Mission {MISSION_NUM} failed:", e)
        robot.mission_error_signal()
        raise e

    finally:
        robot.cleanup()
