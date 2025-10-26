"""
Mission 01: Drive to Target
Navigate to a precise position using straight drives and turns
This demonstrates the basic FLL pattern: Drive → Align → Approach → Complete → Return
"""

from pybricks.tools import wait

# Mission-specific configuration
MISSION_CONFIG = {
    "drive_speed": 200,        # Medium speed for reliable navigation
    "turn_rate": 60,           # Moderate turn rate for accuracy
    "target_distance": 450,    # Distance to target in mm
    "alignment_angle": -23,    # Angle to align with target
    "approach_distance": 120,  # Final approach distance
}

def run(robot):
    """
    Navigate to target position and return home

    This mission demonstrates:
    - Precise straight-line driving
    - Accurate angle turns
    - Multi-step navigation
    - Return to starting position

    Args:
        robot: RobotController object (already initialized)
    """
    print("=== Mission 01: Drive to Target ===")

    # Show countdown
    robot.display.show_countdown(3)

    # STEP 1: Drive to navigation point
    print(f"Step 1: Driving {MISSION_CONFIG['target_distance']}mm to navigation point")
    robot.hub.display.number(1)
    robot.drivebase.straight(MISSION_CONFIG['target_distance'])
    wait(500)

    # STEP 2: Turn to align with target
    print(f"Step 2: Turning {MISSION_CONFIG['alignment_angle']}° to align with target")
    robot.hub.display.number(2)
    robot.drivebase.turn(MISSION_CONFIG['alignment_angle'])
    wait(500)

    # STEP 3: Approach target
    print(f"Step 3: Approaching target ({MISSION_CONFIG['approach_distance']}mm)")
    robot.hub.display.number(3)
    robot.drivebase.straight(MISSION_CONFIG['approach_distance'])
    wait(1000)  # Pause at target

    # STEP 4: Back away from target
    print("Step 4: Backing away from target")
    robot.hub.display.number(4)
    robot.drivebase.straight(-MISSION_CONFIG['approach_distance'])
    wait(500)

    # STEP 5: Turn back to original heading
    print("Step 5: Turning back to original heading")
    robot.hub.display.number(5)
    robot.drivebase.turn(-MISSION_CONFIG['alignment_angle'])
    wait(500)

    # STEP 6: Return to start
    print("Step 6: Returning to start position")
    robot.hub.display.number(6)
    robot.drivebase.straight(-MISSION_CONFIG['target_distance'])

    # Show completion
    robot.display.show_completion_checkmark()
    print("Mission 01 completed successfully!")

def run_custom_navigation(robot, distance, angle, approach):
    """
    Navigate to target with custom parameters

    Args:
        robot: RobotController object (already initialized)
        distance: Distance to navigation point (mm)
        angle: Alignment angle (degrees)
        approach: Approach distance (mm)
    """
    print(f"=== Custom Navigation: {distance}mm, {angle}°, {approach}mm approach ===")

    robot.display.show_countdown(3)

    # Navigate
    robot.drivebase.straight(distance)
    wait(500)
    robot.drivebase.turn(angle)
    wait(500)
    robot.drivebase.straight(approach)
    wait(1000)

    # Return
    robot.drivebase.straight(-approach)
    wait(500)
    robot.drivebase.turn(-angle)
    wait(500)
    robot.drivebase.straight(-distance)

    robot.display.show_completion_checkmark()
    print("Custom navigation completed!")

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
