from robot_controller import RobotController
from display_patterns import DisplayPatterns
from season_config import SeasonDefaults
from pybricks.tools import wait
from line_movements import LineMovements

MISSION_CONFIG = {
    "drive_speed": 300,      # Speed in mm/s
    "turn_rate": 60,
    "black threshold": 20,  } #this is the reflection percentage for black [TRIAL AND ERROR] higher=triggers on lighter surfaces

def run(robot, display):
    """
    Main mission execution function

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== MISSION 08, 05, 06 ===")


    line_moves = LineMovements(robot)
    line_moves.square_on_line(drive_speed=100) #should drive forward until is senses a black line

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