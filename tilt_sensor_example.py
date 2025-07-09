#!/usr/bin/env pybricks-micropython
"""
Tilt Sensor Example for LEGO SPIKE Prime/MINDSTORMS Robot Inventor

This example demonstrates various ways to use the built-in IMU (Inertial Measurement Unit)
tilt sensor functionality in Pybricks. The IMU can detect:
- Pitch and roll angles (tilt)
- Which side of the hub is facing up
- Whether the hub is moving or stationary
- Acceleration and angular velocity

Author: Python Examples Collection
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Color, Side, Axis, Icon, Button
from pybricks.tools import wait


def wait_for_button_release(hub):
    """
    Helper function to wait for button release and add a small delay.
    This prevents button presses from carrying over between examples.
    """
    # Wait for button release
    while hub.buttons.pressed():
        wait(10)
    
    # Small delay to prevent immediate re-detection
    wait(200)


def example_basic_tilt_reading():
    """
    Example 1: Basic tilt reading
    
    This example continuously reads and displays the pitch and roll angles.
    Pitch is rotation around the X-axis (forward/backward tilt).
    Roll is rotation around the Y-axis (left/right tilt).
    """
    print("=== Example 1: Basic Tilt Reading ===")
    print("Tilt the hub and watch the pitch/roll values change.")
    print("Press RIGHT arrow button to continue to next example.")
    
    hub = PrimeHub()
    
    # Display an arrow to indicate this is about tilt
    hub.display.icon(Icon.ARROW_UP)
    
    while True:
        # Read the tilt values (pitch, roll) in degrees
        pitch, roll = hub.imu.tilt()
        
        # Print the results
        print(f"Pitch: {pitch:3.0f}°, Roll: {roll:3.0f}°")
        
        # Change display based on tilt direction
        if abs(pitch) > 30:  # Significant forward/backward tilt
            hub.display.icon(Icon.ARROW_UP if pitch > 0 else Icon.ARROW_DOWN)
        elif abs(roll) > 30:  # Significant left/right tilt
            hub.display.icon(Icon.ARROW_LEFT if roll > 0 else Icon.ARROW_RIGHT)
        else:
            hub.display.icon(Icon.CIRCLE)  # Level position
        
        # Exit when right arrow button is pressed
        if Button.RIGHT in hub.buttons.pressed():
            wait_for_button_release(hub)
            break
            
        wait(100)


def example_side_detection_with_colors():
    """
    Example 2: Side detection with color feedback
    
    This example detects which side of the hub is facing up and changes
    the hub light color accordingly.
    """
    print("\n=== Example 2: Side Detection with Colors ===")
    print("Rotate the hub to different orientations.")
    print("The light color will change based on which side is up.")
    print("Press RIGHT arrow button to continue to next example.")
    
    hub = PrimeHub()
    
    # Define colors for each side
    SIDE_COLORS = {
        Side.TOP: Color.RED,      # Top side up = Red
        Side.BOTTOM: Color.BLUE,  # Bottom side up = Blue  
        Side.LEFT: Color.GREEN,   # Left side up = Green
        Side.RIGHT: Color.YELLOW, # Right side up = Yellow
        Side.FRONT: Color.MAGENTA,# Front side up = Magenta
        Side.BACK: Color.ORANGE,  # Back side up = Orange
    }
    
    # Define display icons for each side
    SIDE_ICONS = {
        Side.TOP: Icon.ARROW_UP,
        Side.BOTTOM: Icon.ARROW_DOWN,
        Side.LEFT: Icon.ARROW_LEFT,
        Side.RIGHT: Icon.ARROW_RIGHT,
        Side.FRONT: Icon.TRIANGLE_UP,
        Side.BACK: Icon.SQUARE,
    }
    
    while True:
        # Check which side of the hub is up
        up_side = hub.imu.up()
        
        # Change the color and display based on the side
        hub.light.on(SIDE_COLORS[up_side])
        hub.display.icon(SIDE_ICONS[up_side])
        
        # Print the result
        print(f"Up side: {up_side}")
        
        # Exit when right arrow button is pressed
        if Button.RIGHT in hub.buttons.pressed():
            wait_for_button_release(hub)
            break
            
        wait(100)


def example_auto_orientation_display():
    """
    Example 3: Auto-orientation display
    
    This example automatically adjusts the display orientation based on
    which side is up, so numbers and icons always appear right-side up.
    """
    print("\n=== Example 3: Auto-Orientation Display ===")
    print("Rotate the hub and watch how the display stays oriented correctly.")
    print("Press RIGHT arrow button to continue to next example.")
    
    hub = PrimeHub()
    
    counter = 0
    
    while True:
        # Check which side of the hub is up
        up_side = hub.imu.up()
        
        # Use this side to set the display orientation
        hub.display.orientation(up_side)
        
        # Display a number that updates every second
        hub.display.number(counter % 100)
        
        # Print the current orientation
        print(f"Display oriented with {up_side} side up")
        
        # Exit when right arrow button is pressed
        if Button.RIGHT in hub.buttons.pressed():
            wait_for_button_release(hub)
            break
            
        counter += 1
        wait(200)


def example_motion_detection():
    """
    Example 4: Motion detection
    
    This example demonstrates how to detect if the hub is moving or stationary.
    It also shows how to check if the IMU is ready for accurate readings.
    """
    print("\n=== Example 4: Motion Detection ===")
    print("Keep the hub still to see 'STATIONARY', move it to see 'MOVING'.")
    print("Press RIGHT arrow button to continue to next example.")
    
    hub = PrimeHub()
    
    while True:
        # Check if the IMU is ready (calibrated)
        ready = hub.imu.ready()
        
        # Check if the hub is stationary
        stationary = hub.imu.stationary()
        
        # Display and print the status
        if not ready:
            hub.light.on(Color.ORANGE)
            hub.display.char("?")
            print("IMU not ready - keep still for calibration")
        elif stationary:
            hub.light.on(Color.GREEN)
            hub.display.icon(Icon.CIRCLE)
            print("STATIONARY")
        else:
            hub.light.on(Color.RED)
            hub.display.char("M")
            print("MOVING")
        
        # Exit when right arrow button is pressed
        if Button.RIGHT in hub.buttons.pressed():
            wait_for_button_release(hub)
            break
            
        wait(200)


def example_advanced_sensor_readings():
    """
    Example 5: Advanced sensor readings
    
    This example shows how to read acceleration and angular velocity values
    from the IMU for more advanced applications.
    """
    print("\n=== Example 5: Advanced Sensor Readings ===")
    print("Move and rotate the hub to see acceleration and angular velocity.")
    print("Press RIGHT arrow button to finish all examples.")
    
    hub = PrimeHub()
    
    # Display a spinning animation to indicate advanced mode
    hub.display.animate([
        Icon.ARROW_UP,
        Icon.ARROW_RIGHT,
        Icon.ARROW_DOWN,
        Icon.ARROW_LEFT
    ], interval=200)
    
    sample_count = 0
    
    while True:
        # Read acceleration vector (in mm/s²)
        acceleration = hub.imu.acceleration()
        
        # Read angular velocity vector (in deg/s)
        angular_velocity = hub.imu.angular_velocity()
        
        # Calculate total acceleration magnitude
        total_accel = (acceleration[0]**2 + acceleration[1]**2 + acceleration[2]**2)**0.5
        
        # Calculate total angular velocity magnitude
        total_angular = (angular_velocity[0]**2 + angular_velocity[1]**2 + angular_velocity[2]**2)**0.5
        
        # Print detailed readings every 10 samples to avoid spam
        if sample_count % 10 == 0:
            print(f"Acceleration: X={acceleration[0]:6.0f}, Y={acceleration[1]:6.0f}, Z={acceleration[2]:6.0f} mm/s²")
            print(f"Angular vel:  X={angular_velocity[0]:6.1f}, Y={angular_velocity[1]:6.1f}, Z={angular_velocity[2]:6.1f} deg/s")
            print(f"Total accel: {total_accel:6.0f} mm/s², Total angular: {total_angular:6.1f} deg/s")
            print()
        
        # Change light color based on motion intensity
        if total_angular > 100:  # Fast rotation
            hub.light.on(Color.MAGENTA)
        elif total_accel > 15000:  # Strong acceleration (beyond gravity)
            hub.light.on(Color.YELLOW)
        else:
            hub.light.on(Color.CYAN)
        
        # Exit when right arrow button is pressed
        if Button.RIGHT in hub.buttons.pressed():
            wait_for_button_release(hub)
            break
            
        sample_count += 1
        wait(100)


def main():
    """
    Main function to run all tilt sensor examples sequentially.
    """
    print("LEGO SPIKE Prime/MINDSTORMS Tilt Sensor Examples")
    print("=" * 50)
    print("This demo will show 5 different ways to use the tilt sensor.")
    print("Press the RIGHT arrow button to advance through each example.")
    print("The center button will still stop the entire program.")
    print()
    
    # Initialize the hub
    hub = PrimeHub()
    
    # Disable center button as stop button to prevent accidental exits
    hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))
    
    # Welcome animation
    hub.light.animate([Color.RED, Color.GREEN, Color.BLUE], interval=300)
    wait(2000)
    
    try:
        # Run all examples in sequence
        example_basic_tilt_reading()
        example_side_detection_with_colors()
        example_auto_orientation_display()
        example_motion_detection()
        example_advanced_sensor_readings()
        
        # Completion message
        print("\n" + "=" * 50)
        print("All tilt sensor examples completed!")
        print("Try experimenting with different orientations and movements.")
        
        # Final celebration
        hub.light.on(Color.GREEN)
        hub.display.icon(Icon.HAPPY)
        hub.speaker.beep(frequency=800, duration=200)
        wait(500)
        hub.speaker.beep(frequency=1000, duration=200)
        
    except KeyboardInterrupt:
        print("\nDemo interrupted by user.")
        
    finally:
        # Clean up
        hub.light.off()
        hub.display.off()
        print("Demo finished.")


if __name__ == "__main__":
    main()
