"""
Mission 03: Square Display
Display animated square patterns on the robot's screen without driving
"""

from robot_controller import RobotController
from display_patterns import DisplayPatterns
from season_config import SeasonDefaults
from pybricks.tools import wait

# Mission-specific configuration overrides
MISSION_CONFIG = {
    "display_delay": 400,      # Time between display updates (ms)
    "animation_cycles": 5,     # Number of complete animation cycles
    "show_variants": True,     # Show different square variants
    "final_display_time": 2000, # Time to show final pattern (ms)
}

def run():
    """
    Main mission execution function
    Display animated square patterns on screen
    """
    print("=== Mission 03: Square Display ===")
    
    # Initialize robot with mission-specific config
    robot = RobotController(SeasonDefaults, MISSION_CONFIG)
    
    try:
        # Initialize robot systems (display only, no driving)
        robot.initialize()
        
        # Initialize display controller
        display = DisplayPatterns(robot.hub, delay=MISSION_CONFIG["display_delay"])
        
        # Signal mission start
        robot.mission_start_signal()
        
        # Show countdown
        display.show_countdown(3)
        
        print(f"Starting square display animation with {MISSION_CONFIG['animation_cycles']} cycles")
        
        # Main square animation
        display.animate_square(cycles=MISSION_CONFIG["animation_cycles"])
        
        # Show variants if enabled
        if MISSION_CONFIG["show_variants"]:
            print("Showing square pattern variants...")
            
            # Static square patterns
            patterns = [
                # Filled square
                [
                    [100, 100, 100, 100, 100],
                    [100, 100, 100, 100, 100],
                    [100, 100, 100, 100, 100],
                    [100, 100, 100, 100, 100],
                    [100, 100, 100, 100, 100]
                ],
                # Corner squares
                [
                    [100, 0, 0, 0, 100],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [100, 0, 0, 0, 100]
                ],
                # Cross pattern
                [
                    [0, 0, 100, 0, 0],
                    [0, 0, 100, 0, 0],
                    [100, 100, 100, 100, 100],
                    [0, 0, 100, 0, 0],
                    [0, 0, 100, 0, 0]
                ],
                # Diagonal squares
                [
                    [100, 0, 0, 0, 0],
                    [0, 100, 0, 0, 0],
                    [0, 0, 100, 0, 0],
                    [0, 0, 0, 100, 0],
                    [0, 0, 0, 0, 100]
                ]
            ]
            
            for i, pattern in enumerate(patterns):
                print(f"Showing pattern variant {i+1}")
                display.hub.display.icon(pattern)
                wait(MISSION_CONFIG["display_delay"] * 2)
        
        # Final display
        print("Showing final square pattern")
        display.animate_square(cycles=1)
        wait(MISSION_CONFIG["final_display_time"])
        
        # Show completion
        display.show_completion_checkmark()
        
        # Signal successful completion
        robot.mission_success_signal()
        print("Mission 03 completed successfully!")
        
    except Exception as e:
        print(f"Mission 03 failed: {e}")
        robot.mission_error_signal()
        
        # Show error on display
        display = DisplayPatterns(robot.hub)
        display.show_error_x()
        
        raise e
        
    finally:
        # Clean up robot state
        robot.cleanup()

def run_with_custom_timing(delay_ms, cycles):
    """
    Run mission with custom timing and cycle count
    
    Args:
        delay_ms: Delay between display updates in milliseconds
        cycles: Number of animation cycles
    """
    # Override the display parameters
    custom_config = MISSION_CONFIG.copy()
    custom_config["display_delay"] = delay_ms
    custom_config["animation_cycles"] = cycles
    
    print(f"=== Mission 03: Square Display (Custom {delay_ms}ms delay, {cycles} cycles) ===")
    
    robot = RobotController(SeasonDefaults, custom_config)
    
    try:
        robot.initialize()
        display = DisplayPatterns(robot.hub, delay=delay_ms)
        
        robot.mission_start_signal()
        display.show_countdown(3)
        
        display.animate_square(cycles=cycles)
        
        if custom_config["show_variants"]:
            # Show one variant pattern
            variant_pattern = [
                [100, 100, 100, 100, 100],
                [100, 0, 0, 0, 100],
                [100, 0, 100, 0, 100],
                [100, 0, 0, 0, 100],
                [100, 100, 100, 100, 100]
            ]
            display.hub.display.icon(variant_pattern)
            wait(custom_config["final_display_time"])
        
        display.show_completion_checkmark()
        robot.mission_success_signal()
        print(f"Custom square display ({delay_ms}ms, {cycles} cycles) completed successfully!")
        
    except Exception as e:
        print(f"Custom square display failed: {e}")
        robot.mission_error_signal()
        display = DisplayPatterns(robot.hub)
        display.show_error_x()
        raise e
        
    finally:
        robot.cleanup()

def run_interactive_display():
    """
    Run an interactive display that shows progress through different square patterns
    """
    print("=== Mission 03: Interactive Square Display ===")
    
    robot = RobotController(SeasonDefaults, MISSION_CONFIG)
    
    try:
        robot.initialize()
        display = DisplayPatterns(robot.hub)
        
        robot.mission_start_signal()
        
        # Show progress through different stages
        stages = [
            "Outer square",
            "Inner square", 
            "Center dot",
            "Filled square",
            "Corner pattern"
        ]
        
        patterns = [
            [
                [100, 100, 100, 100, 100],
                [100, 0, 0, 0, 100],
                [100, 0, 0, 0, 100],
                [100, 0, 0, 0, 100],
                [100, 100, 100, 100, 100]
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 100, 100, 100, 0],
                [0, 100, 0, 100, 0],
                [0, 100, 100, 100, 0],
                [0, 0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 100, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ],
            [
                [100, 100, 100, 100, 100],
                [100, 100, 100, 100, 100],
                [100, 100, 100, 100, 100],
                [100, 100, 100, 100, 100],
                [100, 100, 100, 100, 100]
            ],
            [
                [100, 0, 0, 0, 100],
                [0, 0, 0, 0, 0],
                [0, 0, 100, 0, 0],
                [0, 0, 0, 0, 0],
                [100, 0, 0, 0, 100]
            ]
        ]
        
        for i, (stage, pattern) in enumerate(zip(stages, patterns)):
            print(f"Stage {i+1}: {stage}")
            display.show_progress_bar((i+1) * 20)  # Show progress
            wait(1000)
            display.hub.display.icon(pattern)
            wait(2000)
        
        display.show_completion_checkmark()
        robot.mission_success_signal()
        print("Interactive square display completed successfully!")
        
    except Exception as e:
        print(f"Interactive square display failed: {e}")
        robot.mission_error_signal()
        display = DisplayPatterns(robot.hub)
        display.show_error_x()
        raise e
        
    finally:
        robot.cleanup()

# Allow direct execution for testing
if __name__ == "__main__":
    run()
