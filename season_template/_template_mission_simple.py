"""
Mission {MISSION_NUM}: {MISSION_NAME}
{MISSION_DESCRIPTION}
"""

# Mission-specific configuration
# The menu system will use these settings when initializing the robot
MISSION_CONFIG = {{
    "drive_speed": {DRIVE_SPEED},      # Speed in mm/s
    "turn_rate": {TURN_RATE},          # Turn speed in degrees/s
    # Add more custom settings as needed:
    # "target_distance": 500,
    # "pause_time": 1000,
}}

def run(robot):
    """
    Main mission execution function

    Args:
        robot: RobotController object (already initialized and ready to use!)

    The robot is already initialized with your MISSION_CONFIG settings above.
    Just write your robot movements and logic below!

    Access display helper through robot.display for visual feedback.
    """
    print("=== Mission {MISSION_NUM}: {MISSION_NAME} ===")

    # ========================================
    # QUICK START - Common commands:
    # ========================================
    #   robot.drivebase.straight(500)    # Drive forward 500mm
    #   robot.drivebase.straight(-300)   # Drive backward 300mm
    #   robot.drivebase.turn(90)         # Turn right 90 degrees
    #   robot.drivebase.turn(-90)        # Turn left 90 degrees
    #
    #   robot.display.show_countdown(3)              # Show 3-2-1 countdown
    #   robot.display.show_completion_checkmark()    # Show success checkmark
    #
    # 💡 TIP: Check the season_example/ folder for complete working missions!
    # ========================================

    # TODO: Add your mission logic here
    print("Mission logic not implemented yet!")
    print("Edit this file and add your robot movements above.")

# Standalone testing support - allows running this mission directly
if __name__ == "__main__":
    # Import required classes for standalone testing
    from robot_controller import RobotController
    from season_config import SeasonDefaults

    robot = RobotController(SeasonDefaults, MISSION_CONFIG)

    try:
        robot.initialize()
        robot.mission_start_signal()

        # Run the mission (display is accessible via robot.display)
        run(robot)

        robot.mission_success_signal()
        print("Mission {MISSION_NUM} completed successfully!")

    except Exception as e:
        print("Mission {MISSION_NUM} failed:", e)
        robot.mission_error_signal()
        raise e

    finally:
        robot.cleanup()
