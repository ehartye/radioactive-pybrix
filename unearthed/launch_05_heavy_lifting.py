from robot_controller import RobotController
from display_patterns import DisplayPatterns
from season_config import SeasonDefaults
from pybricks.tools import wait
from line_movements import LineMovements


MISSION_CONFIG = {
    "drive_speed": 300,      # Speed in mm/s
    "turn_rate": 60,
    "black threshold": 10,  } #this is the reflection percentage for black [TRIAL AND ERROR] higher=triggers on lighter surfaces

def run(robot, display):
    """
    Main mission execution function

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== MISSION 07 ===")

    robot.drivebase.straight(355) 
    robot.drivebase.turn(-36)
    robot.right_attachment.run_angle(1000,-175)
    robot.drivebase.straight(350)
    robot.drivebase.turn(-58)
    robot.right_attachment.run_angle(200,175)
    robot.drivebase.turn(70)

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
