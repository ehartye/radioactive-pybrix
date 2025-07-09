"""
Mission 04: Triangle Combo
Combine triangle driving with triangle display patterns on screen
"""

from shared import RobotController
from shared import ShapeMovements
from shared import DisplayPatterns
from season_config import SeasonDefaults
from pybricks.tools import wait

# Mission-specific configuration overrides
MISSION_CONFIG = {
    "drive_speed": 100,        # Slower speed for coordinated movement
    "turn_rate": 40,           # Slower turns for precision
    "triangle_size": 250,      # Size of triangle in mm
    "display_delay": 300,      # Time between display updates (ms)
    "pause_at_corners": True,  # Pause at each corner
    "sync_display": True,      # Synchronize display with movement
    "show_progress": True,     # Show progress indicators
}

def run():
    """
    Main mission execution function
    Drive robot in triangle while displaying triangle patterns
    """
    print("=== Mission 04: Triangle Combo ===")
    
    # Initialize robot with mission-specific config
    robot = RobotController(SeasonDefaults, MISSION_CONFIG)
    
    try:
        # Initialize robot systems
        robot.initialize()
        
        # Initialize movement and display controllers
        movements = ShapeMovements(robot)
        display = DisplayPatterns(robot.hub, delay=MISSION_CONFIG["display_delay"])
        
        # Signal mission start
        robot.mission_start_signal()
        
        # Show countdown
        if MISSION_CONFIG["show_progress"]:
            display.show_countdown(3)
        
        print(f"Starting triangle combo with {MISSION_CONFIG['triangle_size']}mm triangle")
        
        if MISSION_CONFIG["sync_display"]:
            # Synchronized version: display changes with movement
            run_synchronized_triangle(robot, movements, display)
        else:
            # Parallel version: display animates independently
            run_parallel_triangle(robot, movements, display)
        
        # Show completion
        if MISSION_CONFIG["show_progress"]:
            display.show_completion_checkmark()
        
        # Signal successful completion
        robot.mission_success_signal()
        print("Mission 04 completed successfully!")
        
    except Exception as e:
        print(f"Mission 04 failed: {e}")
        robot.mission_error_signal()
        
        # Show error on display
        display = DisplayPatterns(robot.hub)
        display.show_error_x()
        
        raise e
        
    finally:
        # Clean up robot state
        robot.cleanup()

def run_synchronized_triangle(robot, movements, display):
    """
    Run triangle drive with synchronized display updates
    """
    print("Running synchronized triangle combo...")
    
    # Triangle display patterns for each side
    side_patterns = [
        # Side 1 pattern
        [
            [0, 0, 100, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],
        # Side 2 pattern
        [
            [0, 0, 100, 0, 0],
            [0, 100, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],
        # Side 3 pattern (complete triangle)
        [
            [0, 0, 100, 0, 0],
            [0, 100, 0, 100, 0],
            [100, 0, 0, 0, 100],
            [100, 100, 100, 100, 100],
            [0, 0, 0, 0, 0]
        ]
    ]
    
    for side in range(3):
        print(f"Driving triangle side {side + 1}")
        
        # Show pattern for current side
        display.hub.display.icon(side_patterns[side])
        
        # Drive one side of the triangle
        movements.drivebase.straight(MISSION_CONFIG["triangle_size"])
        
        if MISSION_CONFIG["pause_at_corners"]:
            wait(500)
        
        # Show turn indicator
        turn_pattern = [
            [0, 0, 0, 0, 100],
            [0, 0, 0, 100, 0],
            [0, 0, 100, 0, 0],
            [0, 100, 0, 0, 0],
            [100, 0, 0, 0, 0]
        ]
        display.hub.display.icon(turn_pattern)
        
        # Turn 120 degrees clockwise
        movements.drivebase.turn(-120)
        
        if MISSION_CONFIG["pause_at_corners"]:
            wait(500)
    
    # Final triangle display animation
    print("Showing final triangle animation...")
    display.animate_triangle(cycles=2)

def run_parallel_triangle(robot, movements, display):
    """
    Run triangle drive with parallel display animation
    """
    print("Running parallel triangle combo...")
    
    # Start triangle animation in background
    display.animate_triangle(cycles=1)
    
    # Drive the triangle
    movements.drive_triangle(
        side_length=MISSION_CONFIG["triangle_size"],
        pause_at_corners=MISSION_CONFIG["pause_at_corners"]
    )
    
    # Continue animation while robot finishes
    display.animate_triangle(cycles=1)

def run_with_custom_size(size_mm):
    """
    Run mission with custom triangle size
    
    Args:
        size_mm: Triangle size in millimeters
    """
    # Override the triangle size
    custom_config = MISSION_CONFIG.copy()
    custom_config["triangle_size"] = size_mm
    
    print(f"=== Mission 04: Triangle Combo (Custom {size_mm}mm) ===")
    
    robot = RobotController(SeasonDefaults, custom_config)
    
    try:
        robot.initialize()
        movements = ShapeMovements(robot)
        display = DisplayPatterns(robot.hub, delay=custom_config["display_delay"])
        
        robot.mission_start_signal()
        
        if custom_config["show_progress"]:
            display.show_countdown(3)
        
        # Run synchronized version for custom size
        run_synchronized_triangle(robot, movements, display)
        
        if custom_config["show_progress"]:
            display.show_completion_checkmark()
        
        robot.mission_success_signal()
        print(f"Custom triangle combo ({size_mm}mm) completed successfully!")
        
    except Exception as e:
        print(f"Custom triangle combo failed: {e}")
        robot.mission_error_signal()
        display = DisplayPatterns(robot.hub)
        display.show_error_x()
        raise e
        
    finally:
        robot.cleanup()

def run_multi_triangle_combo():
    """
    Run multiple triangles with different display patterns
    """
    print("=== Mission 04: Multi-Triangle Combo ===")
    
    custom_config = MISSION_CONFIG.copy()
    custom_config["triangle_size"] = 200  # Smaller triangles
    
    robot = RobotController(SeasonDefaults, custom_config)
    
    try:
        robot.initialize()
        movements = ShapeMovements(robot)
        display = DisplayPatterns(robot.hub)
        
        robot.mission_start_signal()
        
        if custom_config["show_progress"]:
            display.show_countdown(3)
        
        # Drive 3 triangles with different orientations
        for triangle_num in range(3):
            print(f"Triangle {triangle_num + 1} of 3")
            
            # Show progress
            if custom_config["show_progress"]:
                display.show_progress_bar((triangle_num + 1) * 33)
                wait(1000)
            
            # Animate triangle for this iteration
            display.animate_triangle(cycles=1)
            
            # Drive triangle
            movements.drive_triangle(
                side_length=custom_config["triangle_size"],
                pause_at_corners=custom_config["pause_at_corners"]
            )
            
            # Brief pause between triangles
            if triangle_num < 2:
                wait(1000)
        
        # Final animation
        display.animate_triangle(cycles=2)
        
        if custom_config["show_progress"]:
            display.show_completion_checkmark()
        
        robot.mission_success_signal()
        print("Multi-triangle combo completed successfully!")
        
    except Exception as e:
        print(f"Multi-triangle combo failed: {e}")
        robot.mission_error_signal()
        display = DisplayPatterns(robot.hub)
        display.show_error_x()
        raise e
        
    finally:
        robot.cleanup()

def run_triangle_with_return():
    """
    Run triangle combo and return to starting position
    """
    print("=== Mission 04: Triangle Combo with Return ===")
    
    robot = RobotController(SeasonDefaults, MISSION_CONFIG)
    
    try:
        robot.initialize()
        movements = ShapeMovements(robot)
        display = DisplayPatterns(robot.hub)
        
        robot.mission_start_signal()
        
        if MISSION_CONFIG["show_progress"]:
            display.show_countdown(3)
        
        # Execute triangle combo
        run_synchronized_triangle(robot, movements, display)
        
        # Return to start
        print("Returning to starting position...")
        return_pattern = [
            [0, 100, 0, 100, 0],
            [100, 0, 0, 0, 100],
            [0, 0, 0, 0, 0],
            [100, 0, 0, 0, 100],
            [0, 100, 0, 100, 0]
        ]
        display.hub.display.icon(return_pattern)
        
        movements.return_to_start()
        
        if MISSION_CONFIG["show_progress"]:
            display.show_completion_checkmark()
        
        robot.mission_success_signal()
        print("Triangle combo with return completed successfully!")
        
    except Exception as e:
        print(f"Triangle combo with return failed: {e}")
        robot.mission_error_signal()
        display = DisplayPatterns(robot.hub)
        display.show_error_x()
        raise e
        
    finally:
        robot.cleanup()

# Allow direct execution for testing
if __name__ == "__main__":
    run()
