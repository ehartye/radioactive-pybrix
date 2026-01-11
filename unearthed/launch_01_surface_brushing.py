"""
Mission 1: test_mission
a mission to test stuff
"""

from robot_controller import RobotController
from display_patterns import DisplayPatterns
from season_config import SeasonDefaults
from pybricks.tools import wait

# Mission-specific configuration
# You can override any settings from SeasonDefaults here
MISSION_CONFIG = {
    "drive_speed": 250,      # Speed in mm/s
    "turn_rate": 60,          # Turn speed in degrees/s
    # Add more custom settings as needed, like:
    # "target_distance": 500,
    # "pause_time": 1000,
}

def run(robot, display):
    """
    Main mission execution function

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Mission 1: test_mission ===")
    robot.left_attachment.run_angle(200, -105)
    wait(500)
    robot.drivebase.straight(500)
    #Left attachment: turn 180 degrees right, then 180 degrees left          
    robot.left_attachment.run_angle(200, 105)  # speed 180 deg/s, turn 180 degrees  
    robot.drivebase.turn(-2)
    robot.drivebase.straight(210)
    robot.right_attachment.run_angle(200,  -160)  # speed 180 deg/s, turn 180 degrees
    wait(250)
    robot.drivebase.straight(20)
    wait(250)
    robot.drivebase.turn(-40)
    wait(250)
    robot.drivebase.straight(150)
    wait(250)
    robot.drivebase.straight(-250)
    wait(250)
    robot.drivebase.turn(155)
    wait(250)
    robot.drivebase.straight(90)
    robot.right_attachment.run_angle(400,165)
    wait(250)
    robot.drivebase.straight(-110)
    wait(250)
    robot.drivebase.turn(70)
    wait(250)
    robot.drivebase.settings(straight_speed=500)
    wait(250)
    robot.drivebase.straight(525)

    print("Mission 1 completed successfully!")

# This lets you test the mission by running this file directly
if __name__ == "__main__":
    # Standalone testing mode - initialize robot here
    robot = RobotController(SeasonDefaults, MISSION_CONFIG)
    try:
        robot.initialize()
        display = DisplayPatterns(robot.hub)
        robot.mission_start_signal()
        run(robot, display)
        robot.mission_success_signal()
    except Exception as e:
        print(f"Mission failed: {e}")
        robot.mission_error_signal()
        raise e
    finally:
        robot.cleanup()
