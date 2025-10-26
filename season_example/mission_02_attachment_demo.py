"""
Mission 02: Attachment Demo
Demonstrates using attachment motors for mechanisms (claws, lifts, etc.)
This shows the FLL pattern: Navigate → Deploy mechanism → Complete task → Retract → Return
"""

from pybricks.tools import wait

# Mission-specific configuration
MISSION_CONFIG = {
    "drive_speed": 180,           # Slower for precise positioning
    "turn_rate": 50,              # Slower turns for stability
    "navigation_distance": 350,   # Distance to task area
    "deploy_speed": 400,          # Motor speed for deployment (deg/s)
    "deploy_angle": 180,          # How far to rotate mechanism
    "task_pause": 1000,           # Pause time at task (ms)
}

def run(robot, display):
    """
    Navigate to task, deploy attachment, complete task, return

    This mission demonstrates:
    - Checking if attachment exists before using
    - Using run_angle for precise motor control
    - Coordinating driving with mechanism deployment
    - Error handling for missing attachments

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Mission 02: Attachment Demo ===")

    # Check if we have attachments
    if not robot.left_attachment:
        print("⚠️  WARNING: No left attachment motor detected!")
        print("This mission requires an attachment motor on Port E")
        print("Continuing with driving only...")
        robot.hub.display.text("NO ATTACH")
        wait(2000)

    display.show_countdown(3)

    # STEP 1: Drive to task area
    print(f"Step 1: Driving to task area ({MISSION_CONFIG['navigation_distance']}mm)")
    robot.hub.display.number(1)
    robot.drivebase.straight(MISSION_CONFIG['navigation_distance'])
    wait(500)

    # STEP 2: Deploy attachment mechanism
    if robot.left_attachment:
        print(f"Step 2: Deploying mechanism ({MISSION_CONFIG['deploy_angle']}°)")
        robot.hub.display.text("DEPLOY")

        # Run motor to specific angle
        robot.left_attachment.run_angle(
            MISSION_CONFIG['deploy_speed'],
            MISSION_CONFIG['deploy_angle']
        )
        wait(500)

        # STEP 3: Pause at task (simulating task completion)
        print(f"Step 3: Completing task (pause {MISSION_CONFIG['task_pause']}ms)")
        robot.hub.display.text("TASK")
        wait(MISSION_CONFIG['task_pause'])

        # STEP 4: Retract mechanism
        print("Step 4: Retracting mechanism")
        robot.hub.display.text("RETRACT")
        robot.left_attachment.run_angle(
            MISSION_CONFIG['deploy_speed'],
            -MISSION_CONFIG['deploy_angle']
        )
        wait(500)
    else:
        print("Step 2-4: Skipped (no attachment)")
        wait(MISSION_CONFIG['task_pause'])

    # STEP 5: Return to start
    print("Step 5: Returning to start")
    robot.hub.display.number(5)
    robot.drivebase.straight(-MISSION_CONFIG['navigation_distance'])

    # Show completion
    display.show_completion_checkmark()
    print("Mission 02 completed successfully!")

def run_dual_attachment_demo(robot, display):
    """
    Demonstrate using both left and right attachments

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Dual Attachment Demo ===")

    # Check what we have
    has_left = robot.left_attachment is not None
    has_right = robot.right_attachment is not None

    print(f"Left attachment: {'✓' if has_left else '✗'}")
    print(f"Right attachment: {'✓' if has_right else '✗'}")

    if not (has_left or has_right):
        print("No attachments detected - cannot run demo")
        return

    display.show_countdown(3)

    # Drive to position
    robot.drivebase.straight(300)
    wait(500)

    # Deploy both attachments simultaneously
    if has_left and has_right:
        print("Deploying both attachments")
        robot.hub.display.text("BOTH")

        # Start both motors
        robot.left_attachment.run(400)
        robot.right_attachment.run(400)

        # Let them run for 1 second
        wait(1000)

        # Stop both
        robot.left_attachment.stop()
        robot.right_attachment.stop()

    elif has_left:
        print("Deploying left attachment only")
        robot.hub.display.text("LEFT")
        robot.left_attachment.run_angle(400, 180)

    elif has_right:
        print("Deploying right attachment only")
        robot.hub.display.text("RIGHT")
        robot.right_attachment.run_angle(400, 180)

    wait(500)

    # Return
    robot.drivebase.straight(-300)
    display.show_completion_checkmark()
    print("Dual attachment demo completed!")

def run_until_stalled_demo(robot, display):
    """
    Demonstrate run_until_stalled for pushing/gripping

    Args:
        robot: RobotController object (already initialized)
        display: DisplayPatterns object for hub display
    """
    print("=== Run Until Stalled Demo ===")

    if not robot.left_attachment:
        print("No left attachment - cannot demo")
        return

    display.show_countdown(3)

    # Drive to position
    robot.drivebase.straight(300)

    # Run attachment until it hits resistance (stalls)
    print("Running attachment until stalled (hits resistance)")
    robot.hub.display.text("PUSH")

    # Run slowly and stop when stalled (useful for grippers/pushers)
    robot.left_attachment.run_until_stalled(200, duty_limit=50)

    print("Attachment stalled - task complete")
    wait(1000)

    # Retract
    robot.left_attachment.run_angle(400, -90)
    wait(500)

    # Return
    robot.drivebase.straight(-300)
    display.show_completion_checkmark()
    print("Stall demo completed!")

# Standalone testing support
if __name__ == "__main__":
    from robot_controller import RobotController
    from display_patterns import DisplayPatterns
    from season_config import SeasonDefaults

    robot = RobotController(SeasonDefaults, MISSION_CONFIG)

    try:
        robot.initialize()
        display = DisplayPatterns(robot.hub)
        robot.mission_start_signal()

        run(robot, display)

        robot.mission_success_signal()
        print("Mission completed successfully!")

    except Exception as e:
        print(f"Mission failed: {e}")
        robot.mission_error_signal()
        raise e

    finally:
        robot.cleanup()
