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

def run(robot, display):
    """
    Main mission execution function

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Mission 2: mission2Test ===")

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

    print("Mission 2 completed successfully!")

# This lets you test the mission by running this file directly
if __name__ == "__main__":
    # Standalone testing mode - initialize robot here
    robot = RobotController(SeasonDefaults, MISSION_CONFIG)
    try:
        robot.initialize()
        display = DisplayPatterns(robot.hub)
        robot.mission_start_signal()
        run(robot, display)
        robot.mission_success_signal()
    except Exception as e:
        print(f"Mission failed: {e}")
        robot.mission_error_signal()
        raise e
    finally:
        robot.cleanup()
