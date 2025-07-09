"""
Mission 01: Square Drive
Drive robot in a square pattern with configurable size and speed
"""

from shared import RobotController
from shared import ShapeMovements
from shared import DisplayPatterns
from season_config import SeasonDefaults

# Mission-specific configuration overrides
MISSION_CONFIG = {
    "drive_speed": 150,        # Slower speed for precise turns
    "turn_rate": 45,           # Slower turn rate for accuracy
    "square_size": 300,        # Size of square in mm
    "pause_at_corners": True,  # Pause at each corner
    "show_progress": True,     # Show progress on display
}

def run():
    """
    Main mission execution function
    Drive robot in a square pattern
    """
    print("=== Mission 01: Square Drive ===")
    
    # Initialize robot with mission-specific config
    robot = RobotController(SeasonDefaults, MISSION_CONFIG)
    
    try:
        # Initialize robot systems
        robot.initialize()
        
        # Initialize movement and display controllers
        movements = ShapeMovements(robot)
        display = DisplayPatterns(robot.hub)
        
        # Signal mission start
        robot.mission_start_signal()
        
        # Show countdown if progress display is enabled
        if MISSION_CONFIG["show_progress"]:
            display.show_countdown(3)
        
        # Execute the square drive
        print(f"Starting square drive with {MISSION_CONFIG['square_size']}mm sides")
        movements.drive_square(
            side_length=MISSION_CONFIG["square_size"],
            pause_at_corners=MISSION_CONFIG["pause_at_corners"]
        )
        
        # Show completion
        if MISSION_CONFIG["show_progress"]:
            display.show_completion_checkmark()
        
        # Signal successful completion
        robot.mission_success_signal()
        print("Mission 01 completed successfully!")
        
    except Exception as e:
        print(f"Mission 01 failed: {e}")
        robot.mission_error_signal()
        
        # Show error on display
        display = DisplayPatterns(robot.hub)
        display.show_error_x()
        
        raise e
        
    finally:
        # Clean up robot state
        robot.cleanup()

def run_with_custom_size(size_mm):
    """
    Run mission with custom square size
    
    Args:
        size_mm: Square size in millimeters
    """
    # Override the square size
    custom_config = MISSION_CONFIG.copy()
    custom_config["square_size"] = size_mm
    
    print(f"=== Mission 01: Square Drive (Custom {size_mm}mm) ===")
    
    robot = RobotController(SeasonDefaults, custom_config)
    
    try:
        robot.initialize()
        movements = ShapeMovements(robot)
        display = DisplayPatterns(robot.hub)
        
        robot.mission_start_signal()
        
        if custom_config["show_progress"]:
            display.show_countdown(3)
        
        movements.drive_square(
            side_length=size_mm,
            pause_at_corners=custom_config["pause_at_corners"]
        )
        
        if custom_config["show_progress"]:
            display.show_completion_checkmark()
        
        robot.mission_success_signal()
        print(f"Custom square drive ({size_mm}mm) completed successfully!")
        
    except Exception as e:
        print(f"Custom square drive failed: {e}")
        robot.mission_error_signal()
        display = DisplayPatterns(robot.hub)
        display.show_error_x()
        raise e
        
    finally:
        robot.cleanup()

# Allow direct execution for testing
if __name__ == "__main__":
    run()
