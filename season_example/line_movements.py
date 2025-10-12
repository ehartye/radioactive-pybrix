"""
Line Movements
Functions for line detection and line-following behaviors
"""

from pybricks.tools import wait


class LineMovements:
    """Collection of line-detection and line-following movement functions"""

    def __init__(self, robot_controller):
        """
        Initialize line movements

        Args:
            robot_controller: RobotController instance with configuration
        """
        self.robot = robot_controller
        self.drivebase = robot_controller.drivebase
        self.config = robot_controller.config

    def square_on_line(self, left_sensor=None, right_sensor=None, drive_speed=None, black_threshold=None):
        """
        Drive forward until BOTH color sensors detect a black line, then stop.
        This is called "squaring" because it lines up the robot perpendicular to the line.

        Args:
            left_sensor: Left ColorSensor (default: uses robot.left_color_sensor)
            right_sensor: Right ColorSensor (default: uses robot.right_color_sensor)
            drive_speed: Speed to drive forward in mm/s (default: uses robot's drive_speed config)
            black_threshold: Reflection % below which is considered "black" (default: 20)

        How reflection values work:
            - White surface: 70-100%
            - Gray surface: 30-70%
            - Black line: 5-20%
            - Lower number = darker surface

        Example usage:
            from line_movements import LineMovements

            # Create line movements helper
            line_moves = LineMovements(robot)

            # Simple! Uses robot's built-in sensors
            line_moves.square_on_line()

            # With custom speed (slower for precision)
            line_moves.square_on_line(drive_speed=80)

            # With custom threshold (more sensitive)
            line_moves.square_on_line(black_threshold=25)

            # Advanced: Override sensors if needed
            from pybricks.pupdevices import ColorSensor
            from pybricks.parameters import Port
            custom_sensor = ColorSensor(Port.E)
            line_moves.square_on_line(left_sensor=custom_sensor)
        """
        if not self.robot.is_initialized:
            raise RuntimeError("Robot not initialized. Call robot.initialize() first!")

        # Use robot's sensors if not specified
        if left_sensor is None:
            left_sensor = self.robot.left_color_sensor
        if right_sensor is None:
            right_sensor = self.robot.right_color_sensor

        # Check we have sensors
        if not (left_sensor and right_sensor):
            raise RuntimeError(
                "This function needs both color sensors!\n"
                "  Make sure your sensors are plugged in and ports are correct in season_config.py"
            )

        # Use defaults from config if not specified
        if drive_speed is None:
            drive_speed = self.config.get('drive_speed', 100)

        if black_threshold is None:
            black_threshold = self.config.get('black_threshold', 20)

        print(f"=== Square on Line ===")
        print(f"Drive speed: {drive_speed} mm/s")
        print(f"Black threshold: {black_threshold}%")
        print(f"Driving forward until both sensors detect black line...")

        # Convert drive_speed from mm/s to motor deg/s
        # Formula: wheel_circumference = π * diameter
        # Speed in deg/s = (speed in mm/s / circumference) * 360
        from season_config import Specifications
        import umath as math
        wheel_circumference = math.pi * Specifications.WHEEL_DIAMETER
        motor_speed = int((drive_speed / wheel_circumference) * 360)

        # Start both wheels driving forward independently
        # This allows us to stop each wheel separately when its sensor sees black
        left_motor = self.robot.left_wheel
        right_motor = self.robot.right_wheel

        left_motor.run(motor_speed)
        right_motor.run(motor_speed)

        # Keep checking sensors and stop each wheel independently
        left_stopped = False
        right_stopped = False

        while not (left_stopped and right_stopped):
            # Read reflection values (0-100%, lower = darker)
            left_reflection = left_sensor.reflection()
            right_reflection = right_sensor.reflection()

            # Stop left wheel if it sees black and hasn't stopped yet
            if not left_stopped and left_reflection < black_threshold:
                left_motor.stop()
                left_stopped = True
                print(f"  Left wheel stopped (reflection: {left_reflection}%)")

            # Stop right wheel if it sees black and hasn't stopped yet
            if not right_stopped and right_reflection < black_threshold:
                right_motor.stop()
                right_stopped = True
                print(f"  Right wheel stopped (reflection: {right_reflection}%)")

            # Optional: Print values for debugging
            # Uncomment this line to see what your sensors are reading:
            # print(f"Left: {left_reflection}% | Right: {right_reflection}%")

            # Small delay to prevent overwhelming the sensors
            wait(10)

        # Phase 2: Align robot so both sensors read equally (actually square on line)
        print("  Aligning robot to square on line...")

        tolerance = 3  # Sensors must be within 3% of each other
        max_alignment_attempts = 20  # Prevent infinite loop
        alignment_speed = motor_speed // 4  # Use slower speed for fine adjustment (25% of drive speed)

        # Proportional control: distance to move is proportional to error
        # Bigger difference = bigger movement (up to a max)
        angle_per_percent = 5  # Move 5 degrees per 1% reflection difference
        max_adjustment_angle = 30  # Cap maximum movement at 30 degrees

        attempt = 0
        while attempt < max_alignment_attempts:
            # Read current sensor values
            left_reflection = left_sensor.reflection()
            right_reflection = right_sensor.reflection()

            # Calculate difference
            difference = abs(left_reflection - right_reflection)

            # If sensors are close enough, we're aligned!
            if difference <= tolerance:
                print(f"  ✓ Aligned! Difference: {difference}%")
                break

            # STRATEGY: Use the DARKER sensor (lower reflection) as the target
            # This is likely the better position on the line (first one that hit)
            # Move the LIGHTER sensor BACKWARD to match the darker one
            target_reflection = min(left_reflection, right_reflection)

            # Calculate how much each sensor differs from target
            left_error = left_reflection - target_reflection
            right_error = right_reflection - target_reflection

            # Proportional control: movement proportional to error
            # Negative angle = backward movement
            if left_error > tolerance:
                # Left is lighter, needs to move BACKWARD
                movement = min(int(left_error * angle_per_percent), max_adjustment_angle)
                left_motor.run_angle(alignment_speed, -movement, wait=False)
                print(f"  Adjusting left backward {movement}° (L:{left_reflection}% → target:{target_reflection}%)")

            if right_error > tolerance:
                # Right is lighter, needs to move BACKWARD
                movement = min(int(right_error * angle_per_percent), max_adjustment_angle)
                right_motor.run_angle(alignment_speed, -movement, wait=False)
                print(f"  Adjusting right backward {movement}° (R:{right_reflection}% → target:{target_reflection}%)")

            wait(150)  # Wait for adjustment to complete
            attempt += 1

        # Final check
        if attempt >= max_alignment_attempts:
            print(f"  ⚠ Reached max alignment attempts, difference: {difference}%")

        # Make sure everything is fully stopped
        left_motor.stop()
        right_motor.stop()
        self.drivebase.stop()

        # Final readings
        left_reflection = left_sensor.reflection()
        right_reflection = right_sensor.reflection()
        print(f"✓ Robot squared on line!")
        print(f"  Final readings - Left: {left_reflection}% | Right: {right_reflection}%")
        print(f"  Difference: {abs(left_reflection - right_reflection)}%")
        print()
