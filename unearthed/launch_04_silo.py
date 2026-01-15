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
    robot.right_attachment.run_angle(3000, -240)
    wait(200)
    robot.right_attachment.run_angle(300, 240)
    wait(200)
    robot.right_attachment.run_angle(3000, -240)
    wait(200)
    robot.right_attachment.run_angle(300, 235)
    wait(200)
    robot.right_attachment.run_angle(3000, -240)
    wait(200)
    robot.right_attachment.run_angle(300, 235)
    robot.drivebase.straight(-50)
    robot.drivebase.turn(-25)
    wait(250)
    robot.drivebase.straight(345)
    robot.drivebase.turn(70)
    robot.drivebase.straight(135)
    robot.left_attachment.run_angle(200, 200)
    robot.drivebase.straight(-50)
    robot.left_attachment.run_angle(200, -65)
    robot.drivebase.turn(-35)
    wait(250)
    robot.drivebase.straight(70)
    robot.drivebase.turn(-40)
    wait(250)
    robot.drivebase.turn(10)
    wait(100)
    robot.drivebase.settings(straight_speed=400)
    robot.drivebase.straight(-1000)

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






