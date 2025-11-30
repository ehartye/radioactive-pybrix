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

    robot.drivebase.straight(300) 
    robot.drivebase.turn(-65)
    robot.right_attachment
