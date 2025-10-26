"""
Mission 03: Square Display
Display animated square patterns on the robot's screen without driving
"""

from pybricks.tools import wait

# Mission-specific configuration overrides
MISSION_CONFIG = {
    "display_delay": 400,      # Time between display updates (ms)
    "animation_cycles": 5,     # Number of complete animation cycles
    "show_variants": True,     # Show different square variants
    "final_display_time": 2000, # Time to show final pattern (ms)
}

def run(robot):
    """
    Main mission execution function
    Display animated square patterns on screen

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Mission 03: Square Display ===")

    # Update display delay
    robot.display.delay = MISSION_CONFIG["display_delay"]

    # Show countdown
    robot.display.show_countdown(3)

    print(f"Starting square display animation with {MISSION_CONFIG['animation_cycles']} cycles")

    # Main square animation
    robot.display.animate_square(cycles=MISSION_CONFIG["animation_cycles"])

    # Show variants if enabled
    if MISSION_CONFIG["show_variants"]:
        print("Showing square pattern variants...")

        # Static square patterns
        patterns = [
            # Filled square
            [
                [100, 100, 100, 100, 100],
                [100, 100, 100, 100, 100],
                [100, 100, 100, 100, 100],
                [100, 100, 100, 100, 100],
                [100, 100, 100, 100, 100]
            ],
            # Corner squares
            [
                [100, 0, 0, 0, 100],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [100, 0, 0, 0, 100]
            ],
            # Cross pattern
            [
                [0, 0, 100, 0, 0],
                [0, 0, 100, 0, 0],
                [100, 100, 100, 100, 100],
                [0, 0, 100, 0, 0],
                [0, 0, 100, 0, 0]
            ],
            # Diagonal squares
            [
                [100, 0, 0, 0, 0],
                [0, 100, 0, 0, 0],
                [0, 0, 100, 0, 0],
                [0, 0, 0, 100, 0],
                [0, 0, 0, 0, 100]
            ]
        ]

        for i, pattern in enumerate(patterns):
            print(f"Showing pattern variant {i+1}")
            robot.hub.display.icon(pattern)
            wait(MISSION_CONFIG["display_delay"] * 2)

    # Final display
    print("Showing final square pattern")
    robot.display.animate_square(cycles=1)
    wait(MISSION_CONFIG["final_display_time"])

    # Show completion
    robot.display.show_completion_checkmark()

    print("Mission 03 completed successfully!")

def run_with_custom_timing(robot, delay_ms, cycles):
    """
    Run mission with custom timing and cycle count

    Args:
        robot: RobotController object (already initialized)
        delay_ms: Delay between display updates in milliseconds
        cycles: Number of animation cycles
    """
    print(f"=== Mission 03: Square Display (Custom {delay_ms}ms delay, {cycles} cycles) ===")

    # Override the display parameters
    custom_config = MISSION_CONFIG.copy()
    custom_config["display_delay"] = delay_ms
    custom_config["animation_cycles"] = cycles

    robot.display.delay = delay_ms
    robot.display.show_countdown(3)

    robot.display.animate_square(cycles=cycles)

    if custom_config["show_variants"]:
        # Show one variant pattern
        variant_pattern = [
            [100, 100, 100, 100, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 100, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 100, 100]
        ]
        robot.hub.display.icon(variant_pattern)
        wait(custom_config["final_display_time"])

    robot.display.show_completion_checkmark()
    print(f"Custom square display ({delay_ms}ms, {cycles} cycles) completed successfully!")

def run_interactive_display(robot):
    """
    Run an interactive display that shows progress through different square patterns

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Mission 03: Interactive Square Display ===")

    # Show progress through different stages
    stages = [
        "Outer square",
        "Inner square",
        "Center dot",
        "Filled square",
        "Corner pattern"
    ]

    patterns = [
        [
            [100, 100, 100, 100, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 100, 100]
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 100, 100, 100, 0],
            [0, 100, 0, 100, 0],
            [0, 100, 100, 100, 0],
            [0, 0, 0, 0, 0]
        ],
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 100, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],
        [
            [100, 100, 100, 100, 100],
            [100, 100, 100, 100, 100],
            [100, 100, 100, 100, 100],
            [100, 100, 100, 100, 100],
            [100, 100, 100, 100, 100]
        ],
        [
            [100, 0, 0, 0, 100],
            [0, 0, 0, 0, 0],
            [0, 0, 100, 0, 0],
            [0, 0, 0, 0, 0],
            [100, 0, 0, 0, 100]
        ]
    ]

    for i, (stage, pattern) in enumerate(zip(stages, patterns)):
        print(f"Stage {i+1}: {stage}")
        robot.display.show_progress_bar((i+1) * 20)  # Show progress
        wait(1000)
        robot.hub.display.icon(pattern)
        wait(2000)

    robot.display.show_completion_checkmark()
    print("Interactive square display completed successfully!")

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
