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
    print("=== MISSION 08, 05, 06 ===")

    robot.drivebase.straight(400)
    robot.right_attachment.run_angle(3000, -230)#Not strong enough to push down the lever (maybe use a wedge/slope???)
    wait(250)
    robot.right_attachment.run_angle(300, 230)
    wait(250)
    robot.right_attachment.run_angle(2000, -230)#still not strong enough
    wait(250)
    robot.right_attachment.run_angle(300, 230)
    robot.drivebase.straight(-50)
    robot.drivebase.turn(-25)
    wait(250)
    robot.drivebase.straight(345)
    robot.drivebase.turn(70)
    robot.drivebase.straight(160)
    # Forward until robot squares on a line
    line_moves = LineMovements(robot) 
    line_moves.square_on_line(drive_speed=100) #should drive forward until is senses a black line
    wait(250)
    robot.left_attachment.run_angle(200, 120)

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