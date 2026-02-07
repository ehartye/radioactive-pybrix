from robot_controller import RobotController
from display_patterns import DisplayPatterns
from season_config import SeasonDefaults
from pybricks.tools import wait


MISSION_CONFIG = {
    "drive_speed": 400,      # Speed in mm/s
    "turn_rate": 100,
}

def run(robot, display):
    """
    Main mission execution function

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== MISSION 11 - Angler Artifacts ===")

    robot.drivebase.straight(290)
    robot.left_attachment.run_angle(200, 100)
    robot.right_attachment.run_angle(-200, 800)
    robot.drivebase.straight(15)
    robot.drivebase.turn(180)
    robot.drivebase.straight(700)

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
