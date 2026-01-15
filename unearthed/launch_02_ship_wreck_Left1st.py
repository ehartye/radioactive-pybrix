from robot_controller import RobotController
from display_patterns import DisplayPatterns
from season_config import SeasonDefaults
from pybricks.tools import wait

MISSION_CONFIG = {
    "drive_speed": 300,      # Speed in mm/s
    "turn_rate": 60,  }

def run(robot, display):
    """
    Main mission execution function

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Mission 1: test_mission ===")

    #robot run forward 15 cm
    wait(500)
    robot.drivebase.straight(280)

    robot.right_attachment.run_angle(200, -220)
    #
    robot.drivebase.straight(-125)
    #
    robot.right_attachment.run_angle(200, 220)
    #
    robot.drivebase.turn(-60)
    #
    robot.drivebase.straight(170)
    #
    robot.drivebase.turn(60)
    #
    robot.drivebase.straight(320)
    #
    robot.drivebase.straight(-175)
    #
    robot.drivebase.turn(50)
    #
    robot.left_attachment.run_angle(200,-170)
    #
    robot.drivebase.straight(-100)
    robot.left_attachment.run_angle(250,90)
    #
    robot.drivebase.turn(-45)
    robot.drivebase.settings(straight_speed=500)
    #Jan 15 M09 addition
    robot.drivebase.straight(705)
    robot.drivebase.turn(-45)
    wait(250)
    robot.drivebase.straight(70)
    robot.left_attachment.run_angle(250, -145)
    robot.drivebase.turn(60)
    robot.drivebase.straight(400)

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
