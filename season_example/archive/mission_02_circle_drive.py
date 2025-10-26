"""
Mission 02: Circle Drive
Drive robot in a circle pattern with configurable radius and direction
"""

from pybricks.tools import wait
import math

# Mission-specific configuration overrides
MISSION_CONFIG = {
    "drive_speed": 120,        # Slower speed for smooth circle
    "circle_radius": 400,      # Circle radius in mm
    "clockwise": True,         # Direction of circle
    "show_progress": True,     # Show progress on display
}

def run(robot):
    """
    Main mission execution function
    Drive robot in a circle pattern

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Mission 02: Circle Drive ===")

    # Show countdown if progress display is enabled
    if MISSION_CONFIG["show_progress"]:
        robot.display.show_countdown(3)

    # Start circle animation on display
    if MISSION_CONFIG["show_progress"]:
        robot.display.animate_circle(cycles=1)

    # Execute the circle drive
    direction_text = "clockwise" if MISSION_CONFIG["clockwise"] else "counter-clockwise"
    print(f"Starting circle drive with {MISSION_CONFIG['circle_radius']}mm radius ({direction_text})")

    # Calculate circle circumference
    radius = MISSION_CONFIG["circle_radius"]
    circumference = 2 * math.pi * radius

    # Drive in circle using turn angle (negative for counter-clockwise)
    turn_direction = 360 if MISSION_CONFIG["clockwise"] else -360

    # Use curve to drive in a circle
    # curve(radius, angle) - radius in mm, angle in degrees
    robot.drivebase.curve(radius, turn_direction)

    # Show completion
    if MISSION_CONFIG["show_progress"]:
        robot.display.show_completion_checkmark()

    print("Mission 02 completed successfully!")

def run_with_custom_radius(robot, radius_mm, clockwise=True):
    """
    Run mission with custom circle radius and direction

    Args:
        robot: RobotController object (already initialized)
        radius_mm: Circle radius in millimeters
        clockwise: Direction of circle (True for clockwise, False for counter-clockwise)
    """
    direction_text = "clockwise" if clockwise else "counter-clockwise"
    print(f"=== Mission 02: Circle Drive (Custom {radius_mm}mm {direction_text}) ===")

    # Override the circle parameters
    custom_config = MISSION_CONFIG.copy()
    custom_config["circle_radius"] = radius_mm
    custom_config["clockwise"] = clockwise

    if custom_config["show_progress"]:
        robot.display.show_countdown(3)
        robot.display.animate_circle(cycles=1)

    # Drive in circle using curve
    turn_direction = 360 if clockwise else -360
    robot.drivebase.curve(radius_mm, turn_direction)

    if custom_config["show_progress"]:
        robot.display.show_completion_checkmark()

    print(f"Custom circle drive ({radius_mm}mm {direction_text}) completed successfully!")

def run_figure_eight(robot):
    """
    Run a figure-eight pattern using two circles

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Mission 02: Figure Eight Drive ===")

    # Use smaller radius for figure eight
    custom_config = MISSION_CONFIG.copy()
    custom_config["circle_radius"] = 150

    if custom_config["show_progress"]:
        robot.display.show_countdown(3)

    # Execute figure eight - one circle clockwise, one counter-clockwise
    radius = custom_config["circle_radius"]
    robot.drivebase.curve(radius, 360)   # First circle clockwise
    robot.drivebase.curve(radius, -360)  # Second circle counter-clockwise

    if custom_config["show_progress"]:
        robot.display.show_completion_checkmark()

    print("Figure eight drive completed successfully!")

# Allow direct execution for testing
if __name__ == "__main__":
    from robot_controller import RobotController
    from season_config import SeasonDefaults

    robot = RobotController(SeasonDefaults, MISSION_CONFIG)

    try:
        robot.initialize()
        robot.mission_start_signal()

        run(robot)

        robot.mission_success_signal()
        print("Mission completed successfully!")

    except Exception as e:
        print(f"Mission failed: {e}")
        robot.mission_error_signal()
        raise e

    finally:
        robot.cleanup()
