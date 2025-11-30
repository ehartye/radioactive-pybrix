"""
Example: Drive Forward Until Squaring on a Line

This example shows how to use the LineMovements class to drive forward
until the robot squares on a black line using both color sensors.
"""

from robot_controller import RobotController
from display_patterns import DisplayPatterns
from season_config import SeasonDefaults
from pybricks.tools import wait
from line_movements import LineMovements

MISSION_CONFIG = {
    "drive_speed": 200,      # Speed in mm/s (slower for precision)
    "turn_rate": 60,         # Turn speed in deg/s
    "black_threshold": 20,   # Reflection % below which is considered black
}

def run(robot, display):
    """
    Example mission that drives forward until squaring on a line

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Example: Square on Line ===")

    # Method 1: SIMPLE - Just square on line with default settings
    print("\n--- Method 1: Simple (uses mission config settings) ---")
    line_moves = LineMovements(robot)
    line_moves.square_on_line()

    print("✓ Robot squared on line!")
    wait(1000)

    # Back up to try again
    robot.drivebase.straight(-100)
    wait(500)

    # Method 2: CUSTOM SPEED - Square on line with slower speed for precision
    print("\n--- Method 2: Custom Speed (slower = more precise) ---")
    line_moves.square_on_line(drive_speed=100)  # Half speed

    print("✓ Robot squared on line with custom speed!")
    wait(1000)

    # Back up to try again
    robot.drivebase.straight(-100)
    wait(500)

    # Method 3: CUSTOM THRESHOLD - More sensitive to darker surfaces
    print("\n--- Method 3: Custom Threshold (more sensitive) ---")
    line_moves.square_on_line(
        drive_speed=150,
        black_threshold=25  # Higher = triggers on lighter surfaces
    )

    print("✓ Robot squared on line with custom threshold!")


# ==============================================================================
# COMMON PATTERNS FOR YOUR SILO MISSION
# ==============================================================================

def example_pattern_1(robot):
    """
    Pattern 1: Drive to position, then square on line
    (Most common FLL pattern!)
    """
    print("\n=== Pattern 1: Navigate then Square ===")

    # 1. Drive to approximate position
    robot.drivebase.straight(300)
    robot.drivebase.turn(45)

    # 2. Drive forward until squared on line
    line_moves = LineMovements(robot)
    line_moves.square_on_line()

    # 3. Now you're perfectly aligned - do your task!
    print("Ready to perform task with precise positioning!")


def example_pattern_2(robot):
    """
    Pattern 2: Square on line, then drive exact distance
    (Use line as a reference point!)
    """
    print("\n=== Pattern 2: Line as Reference Point ===")

    # 1. Square on the line
    line_moves = LineMovements(robot)
    line_moves.square_on_line()

    # 2. Now drive exact distance from the line
    robot.drivebase.straight(427)  # Precise distance to target!

    # 3. Do your task
    print("Arrived at exact target!")


def example_pattern_3(robot):
    """
    Pattern 3: Square, do task, square again to return
    (Use line for both alignment and return path!)
    """
    print("\n=== Pattern 3: Square Twice ===")

    line_moves = LineMovements(robot)

    # 1. Square on first line
    line_moves.square_on_line()

    # 2. Drive to target and do task
    robot.drivebase.straight(500)
    print("Task completed!")

    # 3. Turn around
    robot.drivebase.turn(180)

    # 4. Square on line again for return alignment
    line_moves.square_on_line()

    # 5. Drive back to base
    robot.drivebase.straight(500)


# ==============================================================================
# HOW TO ADD THIS TO YOUR SILO.PY
# ==============================================================================
"""
In your silo.py, around line 36-37, replace this:

    # Forward until robot squares on a line


With this:

    # Forward until robot squares on a line
    line_moves = LineMovements(robot)
    line_moves.square_on_line()

That's it! The robot will drive forward until BOTH color sensors detect
the black line, then stop perfectly squared.

TIPS:
- Make sure your color sensors are plugged in (Ports A and B in your config)
- Test on a mat with a black line
- If it doesn't detect the line, try adjusting black_threshold:
  line_moves.square_on_line(black_threshold=25)  # More sensitive
  line_moves.square_on_line(black_threshold=15)  # Less sensitive
- If it goes too fast, slow it down:
  line_moves.square_on_line(drive_speed=100)
"""


if __name__ == "__main__":
    # Standalone testing mode - initialize robot here
    robot = RobotController(SeasonDefaults, MISSION_CONFIG)
    try:
        robot.initialize()
        display = DisplayPatterns(robot.hub)
        robot.mission_start_signal()

        # Run the example
        run(robot, display)

        robot.mission_success_signal()
    except Exception as e:
        print(f"Mission failed: {e}")
        robot.mission_error_signal()
        raise e
    finally:
        robot.cleanup()
