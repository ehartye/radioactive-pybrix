"""
Mission 1: Forward Backward
"""

# Mission-specific configuration
# The menu system will use these settings when initializing the robot
MISSION_CONFIG = {
    "drive_speed": 200,      # Speed in mm/s
    "turn_rate": 60,          # Turn speed in degrees/s
    # Add more custom settings as needed:
    # "target_distance": 500,
    # "pause_time": 1000,
}

def forward_backward(robot):
    """Drive forward then backward - the simplest robot movement!"""
    robot.display.animate_square(cycles=2)
    robot.drivebase.straight(500)
    robot.drivebase.straight(-500)


def run(robot):
    """Main mission execution function"""
    print("=== Mission 1: Forward Backward ===")
    forward_backward(robot)

# Standalone testing support - allows running this mission directly
if __name__ == "__main__":
    # Import required classes for standalone testing
    from robot_controller import RobotController
    from season_config import SeasonDefaults

    robot = RobotController(SeasonDefaults, MISSION_CONFIG)

    try:
        robot.initialize()
        robot.mission_start_signal()

        # Run the mission (display is accessible via robot.display)


        robot.mission_success_signal()
        print("Mission 1 completed successfully!")

    except Exception as e:
        print("Mission 1 failed:", e)
        robot.mission_error_signal()
        raise e

    finally:
        robot.cleanup()
