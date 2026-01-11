"""
Motor Warm-Up Utilities
Helps get consistent motor performance by warming up before missions
"""

from pybricks.tools import wait, StopWatch


def warm_up_until_stable(robot, target_speed=200, readings_needed=5, timeout_ms=3000):
    """
    Run motors until speed is consistent.

    Args:
        robot: RobotController object (already initialized)
        target_speed: Target drive speed in mm/s (default 200)
        readings_needed: How many stable readings in a row (default 5)
        timeout_ms: Maximum warm-up time in milliseconds (default 3000)

    Returns:
        True if stable, False if timed out
    """
    print("=== Motor Warm-Up Starting ===")
    timer = StopWatch()
    stable_readings = 0

    # Start driving forward
    robot.drivebase.drive(target_speed, 0)

    # Calculate expected motor speed in deg/s
    # Formula: speed_deg_s = speed_mm_s * 360 / (pi * wheel_diameter)
    from season_config import Specifications
    wheel_diameter = Specifications.WHEEL_DIAMETER
    expected_deg_s = target_speed * 360 / (3.14159 * wheel_diameter)

    print(f"Target: {target_speed} mm/s = {expected_deg_s:.0f} deg/s at wheels")

    while stable_readings < readings_needed:
        wait(50)  # Check every 50ms

        # Get actual motor speeds
        left_speed = robot.left_wheel.speed()
        right_speed = robot.right_wheel.speed()
        avg_speed = (abs(left_speed) + abs(right_speed)) / 2

        # Check if we're close to target (within 5%)
        tolerance = expected_deg_s * 0.05

        if abs(avg_speed - expected_deg_s) < tolerance:
            stable_readings += 1
            print(f"Stable: {stable_readings}/{readings_needed} ({avg_speed:.0f} deg/s)")
        else:
            stable_readings = 0  # Reset if not stable
            print(f"Warming: {avg_speed:.0f} deg/s (need {expected_deg_s:.0f})")

        # Safety timeout
        if timer.time() > timeout_ms:
            print("Timeout reached - proceeding anyway")
            robot.drivebase.stop()
            wait(200)
            print("=== Warm-Up Complete (timed out) ===")
            return False

    robot.drivebase.stop()
    wait(200)
    print("=== Warm-Up Complete (stable!) ===")
    return True


def quick_warm_up(robot, duration_ms=1000):
    """
    Simple warm-up: drive forward and backward briefly.

    Args:
        robot: RobotController object (already initialized)
        duration_ms: Total warm-up time in milliseconds (default 1000)

    This is simpler than warm_up_until_stable() but usually works well!
    """
    print("=== Quick Warm-Up ===")
    half_time = duration_ms // 2

    # Drive forward
    robot.drivebase.drive(150, 0)
    wait(half_time)

    # Drive backward
    robot.drivebase.drive(-150, 0)
    wait(half_time)

    # Stop and settle
    robot.drivebase.stop()
    wait(200)
    print("=== Warm-Up Complete ===")


# Example usage (when running this file directly)
if __name__ == "__main__":
    from robot_controller import RobotController
    from season_config import SeasonDefaults

    robot = RobotController(SeasonDefaults)
    try:
        robot.initialize()

        # Try the advanced warm-up
        print("\nTesting advanced warm-up...")
        was_stable = warm_up_until_stable(robot)
        print(f"Result: {'Stable' if was_stable else 'Timed out'}")

        wait(1000)

        # Try the quick warm-up
        print("\nTesting quick warm-up...")
        quick_warm_up(robot)

        robot.mission_success_signal()
    except Exception as e:
        print(f"Error: {e}")
        robot.mission_error_signal()
    finally:
        robot.cleanup()
