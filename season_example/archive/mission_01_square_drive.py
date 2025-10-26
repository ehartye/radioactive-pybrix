"""
Mission 01: Square Drive
Drive robot in a square pattern with configurable size and speed
"""

from pybricks.tools import wait

# Mission-specific configuration overrides
MISSION_CONFIG = {
    "drive_speed": 150,        # Slower speed for precise turns
    "turn_rate": 45,           # Slower turn rate for accuracy
    "square_size": 300,        # Size of square in mm
    "pause_at_corners": True,  # Pause at each corner
    "show_progress": True,     # Show progress on display
}

def run(robot):
    """
    Main mission execution function
    Drive robot in a square pattern

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Mission 01: Square Drive ===")

    # Show countdown if progress display is enabled
    if MISSION_CONFIG["show_progress"]:
        robot.display.show_countdown(3)

    # Execute the square drive
    print(f"Starting square drive with {MISSION_CONFIG['square_size']}mm sides")
    side_length = MISSION_CONFIG["square_size"]
    pause_at_corners = MISSION_CONFIG["pause_at_corners"]

    # Drive square pattern using direct drivebase commands
    for i in range(4):
        robot.hub.display.number(i + 1)
        robot.drivebase.straight(side_length)
        if pause_at_corners:
            wait(500)
        robot.drivebase.turn(90)
        if pause_at_corners:
            wait(500)

    # Show completion
    if MISSION_CONFIG["show_progress"]:
        robot.display.show_completion_checkmark()

    print("Mission 01 completed successfully!")

def run_with_custom_size(robot, size_mm):
    """
    Run mission with custom square size

    Args:
        robot: RobotController object (already initialized)
        size_mm: Square size in millimeters
    """
    print(f"=== Mission 01: Square Drive (Custom {size_mm}mm) ===")

    # Override the square size
    custom_config = MISSION_CONFIG.copy()
    custom_config["square_size"] = size_mm

    if custom_config["show_progress"]:
        robot.display.show_countdown(3)

    # Drive square pattern using direct drivebase commands
    for i in range(4):
        robot.hub.display.number(i + 1)
        robot.drivebase.straight(size_mm)
        if custom_config["pause_at_corners"]:
            wait(500)
        robot.drivebase.turn(90)
        if custom_config["pause_at_corners"]:
            wait(500)

    if custom_config["show_progress"]:
        robot.display.show_completion_checkmark()

    print(f"Custom square drive ({size_mm}mm) completed successfully!")

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
