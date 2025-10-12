"""
Mission 2: mission2Test
mission2Test
"""

from robot_controller import RobotController
from display_patterns import DisplayPatterns
from season_config import SeasonDefaults
from line_movements import LineMovements

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
        # MISSION LOGIC: Square on Line Test
        # ============================================================

        # This mission demonstrates the square_on_line function
        # It drives forward until both color sensors detect a black line, then stops

        print("Starting square on line test...")

        # Show countdown so you have time to get ready
        display.show_countdown(3)

        # Create line movements helper
        line_moves = LineMovements(robot)

        # Drive forward until both sensors see the black line
        # This uses the robot's built-in color sensors automatically!
        print("Driving to line...")
        line_moves.square_on_line(drive_speed=100, black_threshold=9)

        # Success! Show checkmark
        display.show_completion_checkmark()

        print("✓ Successfully stopped on line!")

        # Optional: You can also customize the behavior
        # Examples you can try:

        # Slower approach for more precision:
        # line_moves.square_on_line(drive_speed=80)

        # More sensitive to black (useful if line is faded):
        # line_moves.square_on_line(black_threshold=25)

        # Both custom settings:
        # line_moves.square_on_line(drive_speed=100, black_threshold=30)

        # ============================================================
        # END OF MISSION LOGIC
        # ============================================================

        # Step 4: Signal success (beep + green light)
        robot.mission_success_signal()
        print("Mission 2 completed successfully!")

    except Exception as e:
        # If something goes wrong, show error
        print("Mission 2 failed:", e)
        robot.mission_error_signal()
        raise e

    finally:
        # Always clean up (stop motors, turn off lights)
        robot.cleanup()

# This lets you test the mission by running this file directly
if __name__ == "__main__":
    run()
