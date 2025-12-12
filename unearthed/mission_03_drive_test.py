"""
Mission 3: drive_test
forward_backwards
"""

# Mission-specific configuration
# You can override any settings from SeasonDefaults here
# The menu system will use these settings when initializing the robot
MISSION_CONFIG = {
    "drive_speed": 300,      # Speed in mm/s
    "turn_rate": 60,          # Turn speed in degrees/s
    # Add more custom settings as needed, like:
    # "target_distance": 500,
    # "pause_time": 1000,
}

def run(robot):
    """
    Main mission execution function

    Args:
        robot: RobotController object (already initialized and ready to use!)

    The robot is already initialized with your MISSION_CONFIG settings above.
    Just write your robot movements and logic below!

    Access display helper through robot.display for visual feedback.
    """
    print("=== Mission 3: drive_test ===")

    robot.drivebase.straight(400)
    robot.drivebase.straight(-400)
    
      
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
        print("Mission 3 completed successfully!")

    except Exception as e:
        print("Mission 3 failed:", e)
        robot.mission_error_signal()
        raise e

    finally:
        robot.cleanup()
