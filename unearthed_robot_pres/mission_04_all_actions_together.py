"""
Mission 4: all actions together
all actions together
"""

from mission_01_forward_backward import forward_backward
from mission_02_spinning import spinning
from mission_03_use_attachments import use_attachments

# Mission-specific configuration
# You can override any settings from SeasonDefaults here
# The menu system will use these settings when initializing the robot
MISSION_CONFIG = {
    "drive_speed": 200,      # Speed in mm/s
    "turn_rate": 60,          # Turn speed in degrees/s
    # Add more custom settings as needed, like:
    # "target_distance": 500,
    # "pause_time": 1000,
}

def all_actions_together(robot):
    """Combine driving, turning, and attachments - a complete mission!"""
    forward_backward(robot)
    spinning(robot)
    use_attachments(robot)
    robot.display.show_completion_checkmark()


def run(robot):
    """Main mission execution function"""
    print("=== Mission 4: All actions together ===")
    all_actions_together(robot)

# This lets you test the mission by running this file directly
if __name__ == "__main__":
    # For standalone testing, we need to set up the robot ourselves
    from robot_controller import RobotController
    from season_config import SeasonDefaults

    robot = RobotController(SeasonDefaults, MISSION_CONFIG)

    try:
        robot.initialize()
        robot.mission_start_signal()

        # Run the mission (display is accessible via robot.display)
        run(robot)

        robot.mission_success_signal()
        print("Mission 4 completed successfully!")

    except Exception as e:
        print("Mission 4 failed:", e)
        robot.mission_error_signal()
        raise e

    finally:
        robot.cleanup()
