"""
Mission 1: drive and lift
drive and lift
"""

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

def run(robot):
    """
    Main mission execution function

    Args:
        robot: RobotController object (already initialized and ready to use!)

    The robot is already initialized with your MISSION_CONFIG settings above.
    Just write your robot movements and logic below!

    Access display helper through robot.display for visual feedback.
    """
    print("=== Mission 1: drive and lift ===")

def run(robot: RobotController):
    """
    Mission: Drive forward 500mm while lifting left attachment 45 degrees

    The key to doing two things at once:
    - Use .drive() instead of .straight() (doesn't wait)
    - Use .run_angle(..., wait=False) for attachment (doesn't wait)
    """
    from pybricks.tools import wait

    # Show countdown on display
    robot.display.show_countdown(3)

    # Start driving forward continuously
    robot.drivebase.drive(200, 0)  # 200 mm/s forward, 0 turn

    # Start lifting attachment at the SAME TIME (wait=False means don't wait!)
    if robot.left_attachment:
        robot.left_attachment.run_angle(300, 145, wait=False)  # 300 deg/s, 145 degrees, don't wait

    # Now both are running together!
    # Wait for the drive to complete (500mm at 200mm/s = 2.5 seconds)
    wait(2500)

    # Stop driving (attachment already stopped at 45 degrees)
    robot.drivebase.stop()

    # Success!
    robot.display.show_completion_checkmark()

    print("Mission complete! Drove 500mm and lifted 45 degrees together!")


    # ============================================================
    # END OF MISSION LOGIC
    # ============================================================

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
        print("Mission 1 completed successfully!")

    except Exception as e:
        print("Mission 1 failed:", e)
        robot.mission_error_signal()
        raise e

    finally:
        robot.cleanup()
