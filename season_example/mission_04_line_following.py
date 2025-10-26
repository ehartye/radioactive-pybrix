"""
Mission 04: Line Following
Demonstrates using color sensors and LineMovements for precision positioning
This shows a common FLL pattern: Navigate → Find line → Square on line → Complete task
"""

from pybricks.tools import wait
from line_movements import LineMovements

# Mission-specific configuration
MISSION_CONFIG = {
    "drive_speed": 150,           # Slower for line detection
    "turn_rate": 50,              # Slower turns for precision
    "navigation_distance": 250,   # Distance before line detection
    "line_speed": 80,             # Slower speed when approaching line
    "black_threshold": 20,        # Reflection % considered black
    "final_approach": 100,        # Distance after squaring on line
}

def run(robot):
    """
    Navigate to line, square on it, continue mission

    This mission demonstrates:
    - Checking if sensors exist before using
    - Using LineMovements for precision positioning
    - Squaring on a line for accurate alignment
    - Handling cases where sensors aren't available

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Mission 04: Line Following ===")

    # Check if we have color sensors
    if not (robot.left_color_sensor or robot.right_color_sensor):
        print("⚠️  WARNING: No color sensors detected!")
        print("This mission requires color sensors on Ports A/B")
        print("Falling back to basic navigation...")
        robot.hub.display.text("NO SENS")
        wait(2000)

        # Fallback: just drive without line following
        run_without_sensors(robot)
        return

    # We have sensors - use line following
    robot.display.show_countdown(3)

    # Create line movements helper
    line_moves = LineMovements(robot)

    # STEP 1: Navigate toward line
    print(f"Step 1: Driving toward line ({MISSION_CONFIG['navigation_distance']}mm)")
    robot.hub.display.number(1)
    robot.drivebase.straight(MISSION_CONFIG['navigation_distance'])
    wait(500)

    # STEP 2: Square on line (both sensors detect black)
    print("Step 2: Squaring on line...")
    robot.hub.display.text("SQUARE")

    line_moves.square_on_line(
        drive_speed=MISSION_CONFIG['line_speed'],
        black_threshold=MISSION_CONFIG['black_threshold']
    )

    print("✓ Squared on line!")
    wait(500)

    # STEP 3: Continue mission after squaring
    print(f"Step 3: Continuing mission ({MISSION_CONFIG['final_approach']}mm)")
    robot.hub.display.number(3)
    robot.drivebase.straight(MISSION_CONFIG['final_approach'])
    wait(1000)  # Pause at task location

    # STEP 4: Return (back away, turn around, return)
    print("Step 4: Returning to start")
    robot.hub.display.number(4)
    robot.drivebase.straight(-(MISSION_CONFIG['final_approach'] + MISSION_CONFIG['navigation_distance']))

    # Show completion
    robot.display.show_completion_checkmark()
    print("Mission 04 completed successfully!")

def run_without_sensors(robot):
    """
    Fallback mission when sensors aren't available

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Running without sensors (fallback mode) ===")

    robot.display.show_countdown(3)

    # Just drive forward and back
    robot.drivebase.straight(MISSION_CONFIG['navigation_distance'] + MISSION_CONFIG['final_approach'])
    wait(1000)
    robot.drivebase.straight(-(MISSION_CONFIG['navigation_distance'] + MISSION_CONFIG['final_approach']))

    robot.display.show_completion_checkmark()
    print("Fallback mission completed!")

def run_follow_line_demo(robot):
    """
    Demonstrate following a line edge

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Follow Line Edge Demo ===")

    if not robot.left_color_sensor:
        print("No left sensor - cannot demo line following")
        return

    robot.display.show_countdown(3)

    # Create line movements helper
    line_moves = LineMovements(robot)

    print("Following line edge for 500mm...")
    robot.hub.display.text("FOLLOW")

    # Follow line edge (sensor sees boundary between black and white)
    line_moves.follow_line_edge(
        distance=500,
        speed=80,
        sensor='left',
        target_reflection=30  # Reflection at edge of black line
    )

    print("Line following complete!")
    robot.display.show_completion_checkmark()

def run_find_line_demo(robot):
    """
    Demonstrate finding a line

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Find Line Demo ===")

    if not (robot.left_color_sensor and robot.right_color_sensor):
        print("Need both sensors for this demo")
        return

    robot.display.show_countdown(3)

    # Create line movements helper
    line_moves = LineMovements(robot)

    # Drive forward until we find a black line
    print("Driving until line detected...")
    robot.hub.display.text("SEARCH")

    # Start driving
    robot.drivebase.drive(100, 0)

    # Wait until both sensors see black
    while True:
        left_reflection = robot.left_color_sensor.reflection()
        right_reflection = robot.right_color_sensor.reflection()

        # Debug output
        print(f"Left: {left_reflection}%, Right: {right_reflection}%")

        # Check if both sensors see black
        if left_reflection < MISSION_CONFIG['black_threshold'] and \
           right_reflection < MISSION_CONFIG['black_threshold']:
            print("✓ Line found!")
            robot.hub.display.text("FOUND")
            robot.drivebase.stop()
            break

        wait(50)  # Check every 50ms

    # Celebration
    robot.hub.speaker.beep(800, 200)
    wait(500)
    robot.hub.speaker.beep(1000, 200)

    robot.display.show_completion_checkmark()
    print("Find line demo completed!")

def run_sensor_calibration(robot):
    """
    Help calibrate sensor thresholds

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Sensor Calibration Demo ===")

    if not robot.left_color_sensor:
        print("No sensors to calibrate")
        return

    print("\nPlace robot on WHITE surface and press center button...")
    from pybricks.parameters import Button
    while Button.CENTER not in robot.hub.buttons.pressed():
        wait(100)

    # Measure white
    white_values = []
    for i in range(10):
        white_values.append(robot.left_color_sensor.reflection())
        wait(100)
    white_avg = sum(white_values) / len(white_values)
    print(f"White average: {white_avg:.1f}%")

    robot.hub.speaker.beep()
    wait(1000)

    print("\nPlace robot on BLACK line and press center button...")
    while Button.CENTER not in robot.hub.buttons.pressed():
        wait(100)

    # Measure black
    black_values = []
    for i in range(10):
        black_values.append(robot.left_color_sensor.reflection())
        wait(100)
    black_avg = sum(black_values) / len(black_values)
    print(f"Black average: {black_avg:.1f}%")

    robot.hub.speaker.beep()
    wait(500)

    # Calculate threshold
    threshold = (white_avg + black_avg) / 2
    print(f"\nRecommended threshold: {threshold:.1f}%")
    print(f"Use this in MISSION_CONFIG: black_threshold = {int(threshold)}")

    robot.hub.display.number(int(threshold))
    wait(3000)

    robot.display.show_completion_checkmark()
    print("Calibration complete!")

# Standalone testing support
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
