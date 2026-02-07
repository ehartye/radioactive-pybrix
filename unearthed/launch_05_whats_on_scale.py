
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
    robot.drivebase.turn(-39)
    robot.drivebase.straight(800)
    robot.drivebase.turn(-25)
    robot.drivebase.straight(70)
    robot.drivebase.turn(25)
    robot.drivebase.straight(-330)
    robot.drivebase.straight(120)
    robot.drivebase.turn(-72)
    robot.left_attachment.run_angle(1000,200)
    wait(250)
    robot.left_attachment.run_angle(1000,-100)
    wait(500)
    robot.drivebase.turn(25)
    robot.right_attachment.run_angle(1000,-210)
    robot.drivebase.straight(500)
    robot.drivebase.turn(20)
    robot.right_attachment.run_angle(750,150)
    robot.drivebase.straight(-200)



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