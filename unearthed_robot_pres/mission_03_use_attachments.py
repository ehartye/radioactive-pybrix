"""
Mission 3: Use attachments
Now we can use attachments!
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

def use_attachments(robot):
    """Use the attachment motors - now we can grab things!"""
    robot.display.animate_triangle(cycles=2)
    if robot.left_attachment:
        robot.left_attachment.run_angle(500, 90)
        robot.left_attachment.run_angle(500, -90)


def run(robot):
    """Main mission execution function"""
    print("=== Mission 3: Use attachments ===")
    use_attachments(robot)

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
        use_attachments(robot)

        robot.mission_success_signal()
        print("Mission 3 completed successfully!")

    except Exception as e:
        print("Mission 3 failed:", e)
        robot.mission_error_signal()
        raise e

    finally:
        robot.cleanup()
