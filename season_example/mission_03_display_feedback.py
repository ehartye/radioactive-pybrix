"""
Mission 03: Display Feedback
Demonstrates using the hub display for mission feedback and debugging
This mission doesn't drive - perfect for testing without a robot assembled!
"""

from pybricks.tools import wait
from pybricks.parameters import Color

# Mission-specific configuration
MISSION_CONFIG = {
    "display_delay": 500,       # Time between display updates (ms)
    "step_count": 6,            # Number of mission steps to simulate
    "show_progress_bar": True,  # Show progress bar
    "show_icons": True,         # Show status icons
}

def run(robot, display):
    """
    Simulate a mission using only display feedback

    This mission demonstrates:
    - Showing mission progress to the driver
    - Using different display patterns for feedback
    - Hub light status indicators
    - Sounds for feedback
    - Testing mission logic without driving

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Mission 03: Display Feedback ===")
    print("This mission uses only display/sound - no robot movement needed!")

    # Show countdown
    display.show_countdown(3)

    # Simulate mission steps with visual feedback
    steps = [
        {"name": "Navigate to area", "number": 1},
        {"name": "Align with target", "number": 2},
        {"name": "Deploy mechanism", "number": 3},
        {"name": "Complete task", "number": 4},
        {"name": "Retract mechanism", "number": 5},
        {"name": "Return to base", "number": 6},
    ]

    for i, step in enumerate(steps):
        print(f"\n{step['name']}...")

        # Show step number on display
        robot.hub.display.number(step['number'])

        # Change hub light color based on progress
        if i < 2:
            robot.hub.light.on(Color.BLUE)      # Early steps = blue
        elif i < 4:
            robot.hub.light.on(Color.YELLOW)    # Middle steps = yellow
        else:
            robot.hub.light.on(Color.GREEN)     # Final steps = green

        # Play a quick beep for feedback
        robot.hub.speaker.beep(frequency=600 + (i * 100), duration=100)

        # Show progress bar if enabled
        if MISSION_CONFIG["show_progress_bar"]:
            progress_percent = int(((i + 1) / len(steps)) * 100)
            display.show_progress_bar(progress_percent)
            wait(MISSION_CONFIG['display_delay'])

        # Simulate step execution time
        wait(MISSION_CONFIG['display_delay'])

    # Show completion
    robot.hub.light.on(Color.GREEN)
    display.show_completion_checkmark()

    print("\nMission 03 completed successfully!")

def run_status_display_demo(robot, display):
    """
    Demonstrate different status displays

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Status Display Demo ===")

    statuses = [
        {"text": "READY", "light": Color.BLUE, "desc": "Robot ready"},
        {"text": "DRIVE", "light": Color.YELLOW, "desc": "Driving"},
        {"text": "TASK", "light": Color.ORANGE, "desc": "Executing task"},
        {"text": "DONE", "light": Color.GREEN, "desc": "Task complete"},
    ]

    for status in statuses:
        print(f"{status['desc']}...")
        robot.hub.display.text(status['text'])
        robot.hub.light.on(status['light'])
        robot.hub.speaker.beep()
        wait(1500)

    display.show_completion_checkmark()
    print("Status display demo completed!")

def run_debug_display_demo(robot, display):
    """
    Demonstrate using display for debugging

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Debug Display Demo ===")

    # Simulate checking robot state and showing on display
    print("\nChecking robot components...")

    # Check drivebase
    robot.hub.display.text("CHK DB")
    wait(500)
    if robot.drivebase:
        print("✓ DriveBase OK")
        robot.hub.display.icon([[0, 100, 0, 100, 0],
                                [0, 100, 0, 100, 0],
                                [100, 100, 100, 100, 100],
                                [0, 100, 100, 100, 0],
                                [0, 0, 100, 0, 0]])  # Checkmark
        robot.hub.light.on(Color.GREEN)
    else:
        print("✗ DriveBase ERROR")
        display.show_error_x()
        robot.hub.light.on(Color.RED)
    wait(1000)

    # Check left attachment
    robot.hub.display.text("CHK L")
    wait(500)
    if robot.left_attachment:
        print("✓ Left attachment OK")
        robot.hub.display.text("L OK")
        robot.hub.light.on(Color.GREEN)
    else:
        print("⚠ Left attachment not found")
        robot.hub.display.text("L --")
        robot.hub.light.on(Color.ORANGE)
    wait(1000)

    # Check right attachment
    robot.hub.display.text("CHK R")
    wait(500)
    if robot.right_attachment:
        print("✓ Right attachment OK")
        robot.hub.display.text("R OK")
        robot.hub.light.on(Color.GREEN)
    else:
        print("⚠ Right attachment not found")
        robot.hub.display.text("R --")
        robot.hub.light.on(Color.ORANGE)
    wait(1000)

    # Check sensors
    robot.hub.display.text("CHK S")
    wait(500)
    sensor_count = 0
    if robot.left_color_sensor:
        sensor_count += 1
    if robot.right_color_sensor:
        sensor_count += 1

    robot.hub.display.number(sensor_count)
    print(f"Found {sensor_count} color sensor(s)")
    wait(1000)

    # Summary
    robot.hub.display.text("READY")
    robot.hub.light.on(Color.BLUE)
    print("\nDiagnostics complete - robot ready!")
    wait(1000)

    display.show_completion_checkmark()

def run_animated_feedback(robot, display):
    """
    Demonstrate animated display patterns

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Animated Feedback Demo ===")

    print("Running animations...")

    # Circle animation (like a progress spinner)
    robot.hub.display.text("LOAD")
    display.animate_circle(cycles=2)

    # Square animation
    robot.hub.display.text("PROC")
    display.animate_square(cycles=2)

    # Arrows showing direction
    robot.hub.display.text("FWD")
    display.show_arrow("up")
    wait(1000)

    robot.hub.display.text("BACK")
    display.show_arrow("down")
    wait(1000)

    robot.hub.display.text("LEFT")
    display.show_arrow("left")
    wait(1000)

    robot.hub.display.text("RIGHT")
    display.show_arrow("right")
    wait(1000)

    display.show_completion_checkmark()
    print("Animation demo completed!")

# Standalone testing support
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
