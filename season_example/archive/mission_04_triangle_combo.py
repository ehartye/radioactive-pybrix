"""
Mission 04: Triangle Combo
Combine triangle driving with triangle display patterns on screen
"""

from pybricks.tools import wait

# Mission-specific configuration overrides
MISSION_CONFIG = {
    "drive_speed": 100,        # Slower speed for coordinated movement
    "turn_rate": 40,           # Slower turns for precision
    "triangle_size": 250,      # Size of triangle in mm
    "display_delay": 300,      # Time between display updates (ms)
    "pause_at_corners": True,  # Pause at each corner
    "sync_display": True,      # Synchronize display with movement
    "show_progress": True,     # Show progress indicators
}

def run(robot):
    """
    Main mission execution function
    Drive robot in triangle while displaying triangle patterns

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Mission 04: Triangle Combo ===")

    # Show countdown
    if MISSION_CONFIG["show_progress"]:
        robot.display.show_countdown(3)

    print(f"Starting triangle combo with {MISSION_CONFIG['triangle_size']}mm triangle")

    if MISSION_CONFIG["sync_display"]:
        # Synchronized version: display changes with movement
        run_synchronized_triangle(robot)
    else:
        # Parallel version: display animates independently
        run_parallel_triangle(robot)

    # Show completion
    if MISSION_CONFIG["show_progress"]:
        robot.display.show_completion_checkmark()

    print("Mission 04 completed successfully!")

def run_synchronized_triangle(robot):
    """
    Run triangle drive with synchronized display updates
    """
    print("Running synchronized triangle combo...")

    # Triangle display patterns for each side
    side_patterns = [
        # Side 1 pattern
        [
            [0, 0, 100, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],
        # Side 2 pattern
        [
            [0, 0, 100, 0, 0],
            [0, 100, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],
        # Side 3 pattern (complete triangle)
        [
            [0, 0, 100, 0, 0],
            [0, 100, 0, 100, 0],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 100, 100],
            [0, 0, 0, 0, 0]
        ]
    ]

    for side in range(3):
        print(f"Driving triangle side {side + 1}")

        # Show pattern for current side
        robot.hub.display.icon(side_patterns[side])

        # Drive one side of the triangle
        robot.drivebase.straight(MISSION_CONFIG["triangle_size"])

        if MISSION_CONFIG["pause_at_corners"]:
            wait(500)

        # Show turn indicator
        turn_pattern = [
            [0, 0, 0, 0, 100],
            [0, 0, 0, 100, 0],
            [0, 0, 100, 0, 0],
            [0, 100, 0, 0, 0],
            [100, 0, 0, 0, 0]
        ]
        robot.hub.display.icon(turn_pattern)

        # Turn 120 degrees (for equilateral triangle)
        robot.drivebase.turn(-120)

        if MISSION_CONFIG["pause_at_corners"]:
            wait(500)

    # Final triangle display animation
    print("Showing final triangle animation...")
    robot.display.animate_triangle(cycles=2)

def run_parallel_triangle(robot):
    """
    Run triangle drive with parallel display animation
    """
    print("Running parallel triangle combo...")

    # Start triangle animation
    robot.display.animate_triangle(cycles=1)

    # Drive the triangle (3 sides with 120-degree turns)
    for side in range(3):
        robot.drivebase.straight(MISSION_CONFIG["triangle_size"])
        if MISSION_CONFIG["pause_at_corners"]:
            wait(500)
        robot.drivebase.turn(-120)
        if MISSION_CONFIG["pause_at_corners"]:
            wait(500)

    # Continue animation while robot finishes
    robot.display.animate_triangle(cycles=1)

def run_with_custom_size(robot, size_mm):
    """
    Run mission with custom triangle size

    Args:
        robot: RobotController object (already initialized)
        size_mm: Triangle size in millimeters
    """
    # Override the triangle size
    custom_config = MISSION_CONFIG.copy()
    custom_config["triangle_size"] = size_mm

    print(f"=== Mission 04: Triangle Combo (Custom {size_mm}mm) ===")

    if custom_config["show_progress"]:
        robot.display.show_countdown(3)

    # Temporarily update config for this run
    original_size = MISSION_CONFIG["triangle_size"]
    MISSION_CONFIG["triangle_size"] = size_mm

    # Run synchronized version for custom size
    run_synchronized_triangle(robot)

    # Restore original size
    MISSION_CONFIG["triangle_size"] = original_size

    if custom_config["show_progress"]:
        robot.display.show_completion_checkmark()

    print(f"Custom triangle combo ({size_mm}mm) completed successfully!")

def run_multi_triangle_combo(robot):
    """
    Run multiple triangles with different display patterns

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Mission 04: Multi-Triangle Combo ===")

    custom_config = MISSION_CONFIG.copy()
    custom_config["triangle_size"] = 200  # Smaller triangles

    if custom_config["show_progress"]:
        robot.display.show_countdown(3)

    # Drive 3 triangles with different orientations
    for triangle_num in range(3):
        print(f"Triangle {triangle_num + 1} of 3")

        # Show progress
        if custom_config["show_progress"]:
            robot.display.show_progress_bar((triangle_num + 1) * 33)
            wait(1000)

        # Animate triangle for this iteration
        robot.display.animate_triangle(cycles=1)

        # Drive triangle (3 sides with 120-degree turns)
        for side in range(3):
            robot.drivebase.straight(custom_config["triangle_size"])
            if custom_config["pause_at_corners"]:
                wait(500)
            robot.drivebase.turn(-120)
            if custom_config["pause_at_corners"]:
                wait(500)

        # Brief pause between triangles
        if triangle_num < 2:
            wait(1000)

    # Final animation
    robot.display.animate_triangle(cycles=2)

    if custom_config["show_progress"]:
        robot.display.show_completion_checkmark()

    print("Multi-triangle combo completed successfully!")

def run_triangle_with_return(robot):
    """
    Run triangle combo and return to starting position

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Mission 04: Triangle Combo with Return ===")

    if MISSION_CONFIG["show_progress"]:
        robot.display.show_countdown(3)

    # Execute triangle combo
    run_synchronized_triangle(robot)

    # Return to start
    print("Returning to starting position...")
    return_pattern = [
        [0, 100, 0, 100, 0],
        [100, 0, 0, 0, 100],
        [0, 0, 0, 0, 0],
        [100, 0, 0, 0, 100],
        [0, 100, 0, 100, 0]
    ]
    robot.hub.display.icon(return_pattern)

    if MISSION_CONFIG["show_progress"]:
        robot.display.show_completion_checkmark()

    print("Triangle combo with return completed successfully!")

# Allow direct execution for testing
if __name__ == "__main__":
    from robot_controller import RobotController
    from season_config import SeasonDefaults

    # Standalone testing mode - initialize robot here
    robot = RobotController(SeasonDefaults, MISSION_CONFIG)
    try:
        robot.initialize()
        # Update display delay for this mission
        robot.display.delay = MISSION_CONFIG["display_delay"]
        robot.mission_start_signal()
        run(robot)
        robot.mission_success_signal()
    except Exception as e:
        print(f"Mission failed: {e}")
        robot.mission_error_signal()
        robot.display.show_error_x()
        raise e
    finally:
        robot.cleanup()
