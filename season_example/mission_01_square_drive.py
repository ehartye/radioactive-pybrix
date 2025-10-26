"""
Mission 01: Square Drive
Drive robot in a square pattern with configurable size and speed
"""

from shape_movements import ShapeMovements

# Mission-specific configuration overrides
MISSION_CONFIG = {
    "drive_speed": 150,        # Slower speed for precise turns
    "turn_rate": 45,           # Slower turn rate for accuracy
    "square_size": 300,        # Size of square in mm
    "pause_at_corners": True,  # Pause at each corner
    "show_progress": True,     # Show progress on display
}

def run(robot, display):
    """
    Main mission execution function
    Drive robot in a square pattern

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Mission 01: Square Drive ===")

    # Initialize movement controller
    movements = ShapeMovements(robot)

    # Show countdown if progress display is enabled
    if MISSION_CONFIG["show_progress"]:
        display.show_countdown(3)

    # Execute the square drive
    print(f"Starting square drive with {MISSION_CONFIG['square_size']}mm sides")
    movements.drive_square(
        side_length=MISSION_CONFIG["square_size"],
        pause_at_corners=MISSION_CONFIG["pause_at_corners"]
    )

    # Show completion
    if MISSION_CONFIG["show_progress"]:
        display.show_completion_checkmark()

    print("Mission 01 completed successfully!")

def run_with_custom_size(robot, display, size_mm):
    """
    Run mission with custom square size

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
        size_mm: Square size in millimeters
    """
    print(f"=== Mission 01: Square Drive (Custom {size_mm}mm) ===")

    # Initialize movement controller
    movements = ShapeMovements(robot)

    # Override the square size
    custom_config = MISSION_CONFIG.copy()
    custom_config["square_size"] = size_mm

    if custom_config["show_progress"]:
        display.show_countdown(3)

    movements.drive_square(
        side_length=size_mm,
        pause_at_corners=custom_config["pause_at_corners"]
    )

    if custom_config["show_progress"]:
        display.show_completion_checkmark()

    print(f"Custom square drive ({size_mm}mm) completed successfully!")

# Allow direct execution for testing
if __name__ == "__main__":
    from robot_controller import RobotController
    from display_patterns import DisplayPatterns
    from season_config import SeasonDefaults

    robot = RobotController(SeasonDefaults, MISSION_CONFIG)

    try:
        robot.initialize()
        display = DisplayPatterns(robot.hub)
        robot.mission_start_signal()

        run(robot, display)

        robot.mission_success_signal()
        print("Mission completed successfully!")

    except Exception as e:
        print(f"Mission failed: {e}")
        robot.mission_error_signal()
        raise e

    finally:
        robot.cleanup()
