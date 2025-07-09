"""
Mission 02: Circle Drive
Drive robot in a circle pattern with configurable radius and direction
"""

from shared import RobotController
from shared import ShapeMovements
from shared import DisplayPatterns
from season_config import SeasonDefaults

# Mission-specific configuration overrides
MISSION_CONFIG = {
    "drive_speed": 120,        # Slower speed for smooth circle
    "circle_radius": 200,      # Circle radius in mm
    "clockwise": True,         # Direction of circle
    "show_progress": True,     # Show progress on display
    "return_to_start": True,   # Return to starting position after circle
}

def run():
    """
    Main mission execution function
    Drive robot in a circle pattern
    """
    print("=== Mission 02: Circle Drive ===")
    
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
        
        # Start circle animation on display
        if MISSION_CONFIG["show_progress"]:
            display.animate_circle(cycles=1)
        
        # Execute the circle drive
        direction_text = "clockwise" if MISSION_CONFIG["clockwise"] else "counter-clockwise"
        print(f"Starting circle drive with {MISSION_CONFIG['circle_radius']}mm radius ({direction_text})")
        
        movements.drive_circle(
            radius=MISSION_CONFIG["circle_radius"],
            clockwise=MISSION_CONFIG["clockwise"]
        )
        
        # Return to start if configured
        if MISSION_CONFIG["return_to_start"]:
            print("Returning to starting position...")
            movements.return_to_start()
        
        # Show completion
        if MISSION_CONFIG["show_progress"]:
            display.show_completion_checkmark()
        
        # Signal successful completion
        robot.mission_success_signal()
        print("Mission 02 completed successfully!")
        
    except Exception as e:
        print(f"Mission 02 failed: {e}")
        robot.mission_error_signal()
        
        # Show error on display
        display = DisplayPatterns(robot.hub)
        display.show_error_x()
        
        raise e
        
    finally:
        # Clean up robot state
        robot.cleanup()

def run_with_custom_radius(radius_mm, clockwise=True):
    """
    Run mission with custom circle radius and direction
    
    Args:
        radius_mm: Circle radius in millimeters
        clockwise: Direction of circle (True for clockwise, False for counter-clockwise)
    """
    # Override the circle parameters
    custom_config = MISSION_CONFIG.copy()
    custom_config["circle_radius"] = radius_mm
    custom_config["clockwise"] = clockwise
    
    direction_text = "clockwise" if clockwise else "counter-clockwise"
    print(f"=== Mission 02: Circle Drive (Custom {radius_mm}mm {direction_text}) ===")
    
    robot = RobotController(SeasonDefaults, custom_config)
    
    try:
        robot.initialize()
        movements = ShapeMovements(robot)
        display = DisplayPatterns(robot.hub)
        
        robot.mission_start_signal()
        
        if custom_config["show_progress"]:
            display.show_countdown(3)
            display.animate_circle(cycles=1)
        
        movements.drive_circle(
            radius=radius_mm,
            clockwise=clockwise
        )
        
        if custom_config["return_to_start"]:
            print("Returning to starting position...")
            movements.return_to_start()
        
        if custom_config["show_progress"]:
            display.show_completion_checkmark()
        
        robot.mission_success_signal()
        print(f"Custom circle drive ({radius_mm}mm {direction_text}) completed successfully!")
        
    except Exception as e:
        print(f"Custom circle drive failed: {e}")
        robot.mission_error_signal()
        display = DisplayPatterns(robot.hub)
        display.show_error_x()
        raise e
        
    finally:
        robot.cleanup()

def run_figure_eight():
    """
    Run a figure-eight pattern using two circles
    """
    print("=== Mission 02: Figure Eight Drive ===")
    
    # Use smaller radius for figure eight
    custom_config = MISSION_CONFIG.copy()
    custom_config["circle_radius"] = 150
    
    robot = RobotController(SeasonDefaults, custom_config)
    
    try:
        robot.initialize()
        movements = ShapeMovements(robot)
        display = DisplayPatterns(robot.hub)
        
        robot.mission_start_signal()
        
        if custom_config["show_progress"]:
            display.show_countdown(3)
        
        # Execute figure eight
        movements.drive_figure_eight(radius=custom_config["circle_radius"])
        
        if custom_config["show_progress"]:
            display.show_completion_checkmark()
        
        robot.mission_success_signal()
        print("Figure eight drive completed successfully!")
        
    except Exception as e:
        print(f"Figure eight drive failed: {e}")
        robot.mission_error_signal()
        display = DisplayPatterns(robot.hub)
        display.show_error_x()
        raise e
        
    finally:
        robot.cleanup()

# Allow direct execution for testing
if __name__ == "__main__":
    run()
