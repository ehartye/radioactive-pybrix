"""
Mission 02: Circle Drive
Drive robot in a circle pattern with configurable radius and direction
"""

from shape_movements import ShapeMovements

# Mission-specific configuration overrides
MISSION_CONFIG = {
    "drive_speed": 120,        # Slower speed for smooth circle
    "circle_radius": 400,      # Circle radius in mm
    "clockwise": True,         # Direction of circle
    "show_progress": True,     # Show progress on display
}

def run(robot, display):
    """
    Main mission execution function
    Drive robot in a circle pattern

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Mission 02: Circle Drive ===")

    # Initialize movement controller
    movements = ShapeMovements(robot)

    # Show countdown if progress display is enabled
    if MISSION_CONFIG["show_progress"]:
        display.show_countdown(3)

    # Start circle animation on display
    if MISSION_CONFIG["show_progress"]:
        display.animate_circle(cycles=1)

    # Execute the circle drive
    direction_text = "clockwise" if MISSION_CONFIG["clockwise"] else "counter-clockwise"
    print(f"Starting circle drive with {MISSION_CONFIG['circle_radius']}mm radius ({direction_text})")

    movements.drive_circle(
        radius=MISSION_CONFIG["circle_radius"],
        clockwise=MISSION_CONFIG["clockwise"]
    )

    # Show completion
    if MISSION_CONFIG["show_progress"]:
        display.show_completion_checkmark()

    print("Mission 02 completed successfully!")

def run_with_custom_radius(robot, display, radius_mm, clockwise=True):
    """
    Run mission with custom circle radius and direction

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
        radius_mm: Circle radius in millimeters
        clockwise: Direction of circle (True for clockwise, False for counter-clockwise)
    """
    direction_text = "clockwise" if clockwise else "counter-clockwise"
    print(f"=== Mission 02: Circle Drive (Custom {radius_mm}mm {direction_text}) ===")

    # Initialize movement controller
    movements = ShapeMovements(robot)

    # Override the circle parameters
    custom_config = MISSION_CONFIG.copy()
    custom_config["circle_radius"] = radius_mm
    custom_config["clockwise"] = clockwise

    if custom_config["show_progress"]:
        display.show_countdown(3)
        display.animate_circle(cycles=1)

    movements.drive_circle(
        radius=radius_mm,
        clockwise=clockwise
    )

    if custom_config["show_progress"]:
        display.show_completion_checkmark()

    print(f"Custom circle drive ({radius_mm}mm {direction_text}) completed successfully!")

def run_figure_eight(robot, display):
    """
    Run a figure-eight pattern using two circles

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Mission 02: Figure Eight Drive ===")

    # Initialize movement controller
    movements = ShapeMovements(robot)

    # Use smaller radius for figure eight
    custom_config = MISSION_CONFIG.copy()
    custom_config["circle_radius"] = 150

    if custom_config["show_progress"]:
        display.show_countdown(3)

    # Execute figure eight
    movements.drive_figure_eight(radius=custom_config["circle_radius"])

    if custom_config["show_progress"]:
        display.show_completion_checkmark()

    print("Figure eight drive completed successfully!")

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
