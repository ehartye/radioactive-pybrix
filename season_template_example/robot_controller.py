"""
Robot Controller
Common robot initialization and control functions for season missions
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.parameters import Stop

from season_config import Ports, Directions, Specifications, SeasonDefaults

class RobotInitializationError(Exception):
    """Custom exception for robot initialization errors with enhanced debugging"""
    def __init__(self, message, component=None, port=None, original_error=None):
        self.component = component
        self.port = port
        self.original_error = original_error
        
        # Build detailed error message
        error_msg = f"Robot initialization failed: {message}"
        if component:
            error_msg += f" (Component: {component})"
        if port:
            error_msg += f" (Port: {port})"
        if original_error:
            error_msg += f" (Original: {original_error})"
        
        super().__init__(error_msg)


class RobotController:
    """Centralized robot control and management"""
    
    def __init__(self, base_config=None, mission_overrides=None):
        """
        Initialize robot controller
        
        Args:
            base_config: Base season configuration (typically SeasonDefaults)
            mission_overrides: Dictionary of mission-specific setting overrides
        """
        self.hub = PrimeHub()
        self.left_wheel = None
        self.right_wheel = None
        self.left_attachment = None
        self.right_attachment = None
        self.drivebase = None
        
        # Merge configuration
        self.config = self._merge_config(base_config or SeasonDefaults, mission_overrides or {})
        
        self.is_initialized = False
    
    def _merge_config(self, base_config, overrides):
        """Merge base configuration with mission-specific overrides"""
        config = {}
        
        # Get all attributes from base config
        for attr in dir(base_config):
            if not attr.startswith('_'):
                config[attr.lower()] = getattr(base_config, attr)
        
        # Apply overrides
        for key, value in overrides.items():
            config[key.lower()] = value
        
        return config
    
    def initialize(self):
        """Initialize all robot components with detailed debugging"""
        if self.is_initialized:
            print("Robot already initialized, skipping...")
            return
        
        print("=== Robot Initialization Debug Info ===")
        print(f"Left wheel port: {Ports.LEFT_WHEEL}, direction: {Directions.LEFT_WHEEL}")
        print(f"Right wheel port: {Ports.RIGHT_WHEEL}, direction: {Directions.RIGHT_WHEEL}")
        print(f"Left attachment port: {Ports.LEFT_ATTACHMENT}, direction: {Directions.LEFT_ATTACHMENT}")
        print(f"Right attachment port: {Ports.RIGHT_ATTACHMENT}, direction: {Directions.RIGHT_ATTACHMENT}")
        print(f"Wheel diameter: {Specifications.WHEEL_DIAMETER}mm")
        print(f"Axle track: {Specifications.AXLE_TRACK}mm")
        
        try:
            # Initialize left wheel motor
            print("Initializing left wheel motor...")
            try:
                self.left_wheel = Motor(Ports.LEFT_WHEEL, Directions.LEFT_WHEEL)
                print("✓ Left wheel motor initialized successfully")
            except Exception as e:
                raise RobotInitializationError(
                    "Failed to initialize left wheel motor",
                    component="left_wheel",
                    port=Ports.LEFT_WHEEL,
                    original_error=e
                )
            
            # Initialize right wheel motor
            print("Initializing right wheel motor...")
            try:
                self.right_wheel = Motor(Ports.RIGHT_WHEEL, Directions.RIGHT_WHEEL)
                print("✓ Right wheel motor initialized successfully")
            except Exception as e:
                raise RobotInitializationError(
                    "Failed to initialize right wheel motor",
                    component="right_wheel",
                    port=Ports.RIGHT_WHEEL,
                    original_error=e
                )
            
            # Initialize left attachment motor (OPTIONAL - won't fail if not connected)
            print("Initializing left attachment motor (optional)...")
            try:
                self.left_attachment = Motor(Ports.LEFT_ATTACHMENT, Directions.LEFT_ATTACHMENT)
                print("✓ Left attachment motor initialized successfully")
            except Exception as e:
                self.left_attachment = None
                print("⚠ Left attachment not connected (this is okay!)")
                print(f"  If you need it later, check Port {Ports.LEFT_ATTACHMENT}")

            # Initialize right attachment motor (OPTIONAL - won't fail if not connected)
            print("Initializing right attachment motor (optional)...")
            try:
                self.right_attachment = Motor(Ports.RIGHT_ATTACHMENT, Directions.RIGHT_ATTACHMENT)
                print("✓ Right attachment motor initialized successfully")
            except Exception as e:
                self.right_attachment = None
                print("⚠ Right attachment not connected (this is okay!)")
                print(f"  If you need it later, check Port {Ports.RIGHT_ATTACHMENT}")
            
            # Create drivebase
            print("Creating drivebase...")
            try:
                self.drivebase = DriveBase(
                    self.left_wheel, 
                    self.right_wheel, 
                    Specifications.WHEEL_DIAMETER, 
                    Specifications.AXLE_TRACK
                )
                print("✓ Drivebase created successfully")
            except Exception as e:
                raise RobotInitializationError(
                    "Failed to create drivebase",
                    component="drivebase",
                    original_error=e
                )
            
            # Configure drivebase settings
            print("Configuring drivebase settings...")
            try:
                drive_speed = self.config.get('drive_speed', SeasonDefaults.DRIVE_SPEED)
                drive_accel = self.config.get('drive_acceleration', SeasonDefaults.DRIVE_ACCELERATION)
                turn_rate = self.config.get('turn_rate', SeasonDefaults.TURN_RATE)
                turn_accel = self.config.get('turn_acceleration', SeasonDefaults.TURN_ACCELERATION)
                
                print(f"  Drive speed: {drive_speed} mm/s")
                print(f"  Drive acceleration: {drive_accel} mm/s²")
                print(f"  Turn rate: {turn_rate} °/s")
                print(f"  Turn acceleration: {turn_accel} °/s²")
                
                self.drivebase.settings(
                    straight_speed=drive_speed,
                    straight_acceleration=drive_accel,
                    turn_rate=turn_rate,
                    turn_acceleration=turn_accel
                )
                print("✓ Drivebase settings configured successfully")
            except Exception as e:
                raise RobotInitializationError(
                    "Failed to configure drivebase settings",
                    component="drivebase_settings",
                    original_error=e
                )
            
            # Enable gyro for accurate turns
            print("Enabling gyro...")
            try:
                self.drivebase.use_gyro(True)
                print("✓ Gyro enabled successfully")
            except Exception as e:
                print(f"⚠ Warning: Failed to enable gyro: {e}")
                print("  Continuing without gyro (turns may be less accurate)")
            
            # Reset measurements
            print("Resetting measurements...")
            try:
                self.reset_measurements()
                print("✓ Measurements reset successfully")
            except Exception as e:
                print(f"⚠ Warning: Failed to reset measurements: {e}")
            
            # Signal successful initialization
            self.hub.light.on(SeasonDefaults.MISSION_START_COLOR)
            self.hub.speaker.beep(500, 100)
            
            self.is_initialized = True
            print("✓ Robot initialization completed successfully!")
            print("=" * 40)
            
        except RobotInitializationError:
            # Re-raise our custom error as-is
            self.hub.light.on(SeasonDefaults.MISSION_ERROR_COLOR)
            self.hub.speaker.beep(200, 500)
            raise
        except Exception as e:
            # Catch any other unexpected errors
            self.hub.light.on(SeasonDefaults.MISSION_ERROR_COLOR)
            self.hub.speaker.beep(200, 500)
            raise RobotInitializationError(
                "Unexpected error during initialization",
                original_error=e
            )
    
    def reset_measurements(self):
        """Reset all distance and angle measurements"""
        if self.drivebase:
            self.drivebase.reset()
        if self.left_attachment:
            self.left_attachment.reset_angle(0)
        if self.right_attachment:
            self.right_attachment.reset_angle(0)
    
    def get_measurements(self):
        """Get current robot measurements"""
        if not self.is_initialized:
            return None

        measurements = {
            'drive_distance': self.drivebase.distance(),
            'drive_angle': self.drivebase.angle(),
        }

        # Only include attachment measurements if they exist
        if self.left_attachment:
            measurements['left_attachment_angle'] = self.left_attachment.angle()
        if self.right_attachment:
            measurements['right_attachment_angle'] = self.right_attachment.angle()

        return measurements
    
    def mission_start_signal(self):
        """Signal start of mission execution"""
        self.hub.light.on(SeasonDefaults.MISSION_RUNNING_COLOR)
        self.hub.speaker.beep(600, 100)
    
    def mission_success_signal(self):
        """Signal successful mission completion"""
        self.hub.light.on(SeasonDefaults.MISSION_SUCCESS_COLOR)
        self.hub.speaker.beep(
            SeasonDefaults.COMPLETION_BEEP_FREQ, 
            SeasonDefaults.COMPLETION_BEEP_TIME
        )
    
    def mission_error_signal(self):
        """Signal mission error or failure"""
        self.hub.light.on(SeasonDefaults.MISSION_ERROR_COLOR)
        self.hub.speaker.beep(200, 500)
    
    def cleanup(self):
        """Clean up robot state and stop all motors with proper resource release"""
        print("=== Robot Cleanup Debug Info ===")
        
        # Stop and reset drivebase first
        if self.drivebase:
            print("Stopping and resetting drivebase...")
            try:
                self.drivebase.stop()
                print("✓ Drivebase stopped")
            except Exception as e:
                print(f"⚠ Warning: Failed to stop drivebase: {e}")
            
            try:
                self.drivebase.use_gyro(False)
                print("✓ Gyro disabled")
            except Exception as e:
                print(f"⚠ Warning: Failed to disable gyro: {e}")
            
            try:
                self.drivebase.reset()
                print("✓ Drivebase reset (also calls stop)")
            except Exception as e:
                print(f"⚠ Warning: Failed to reset drivebase: {e}")
            
            self.drivebase = None
            print("✓ Drivebase reference cleared")
        
        # Close each motor properly to release hardware resources
        motors_to_close = [
            ("left_wheel", self.left_wheel),
            ("right_wheel", self.right_wheel),
            ("left_attachment", self.left_attachment),
            ("right_attachment", self.right_attachment)
        ]
        
        for motor_name, motor in motors_to_close:
            if motor:
                print(f"Stopping and closing {motor_name}...")
                try:
                    motor.stop()
                    print(f"✓ {motor_name} stopped")
                except Exception as e:
                    print(f"⚠ Warning: Failed to stop {motor_name}: {e}")
                
                try:
                    motor.close()  # This is the key addition - properly releases hardware!
                    print(f"✓ {motor_name} closed and hardware released")
                except Exception as e:
                    print(f"⚠ Warning: Failed to close {motor_name}: {e}")
                
                # Clear the reference
                setattr(self, motor_name, None)
                print(f"✓ {motor_name} reference cleared")
        
        # Turn off display and light
        try:
            self.hub.display.off()
            self.hub.light.off()
            print("✓ Display and light turned off")
        except Exception as e:
            print(f"⚠ Warning: Failed to turn off display/light: {e}")
        
        # Reset initialization flag
        self.is_initialized = False
        print("✓ Initialization flag reset")
        
        wait(100)  # Brief pause for cleanup
        print("✓ Robot cleanup completed with proper hardware release")
        print("=" * 55)
    
    def get_system_info(self):
        """Get system diagnostic information"""
        print("=== System Diagnostic Info ===")
        
        try:
            # Hub information
            print(f"Hub battery: {self.hub.battery.voltage()} mV")
            print(f"Hub temperature: {self.hub.system.temperature()} °C")
            print(f"Hub system time: {self.hub.system.time()} ms")
            
            # Component status
            print(f"Robot initialized: {self.is_initialized}")
            print(f"Left wheel connected: {self.left_wheel is not None}")
            print(f"Right wheel connected: {self.right_wheel is not None}")
            print(f"Left attachment connected: {self.left_attachment is not None}")
            print(f"Right attachment connected: {self.right_attachment is not None}")
            print(f"Drivebase created: {self.drivebase is not None}")
            
            # Current measurements if available
            if self.is_initialized:
                measurements = self.get_measurements()
                if measurements:
                    print(f"Drive distance: {measurements['drive_distance']} mm")
                    print(f"Drive angle: {measurements['drive_angle']} degrees")
                    print(f"Left attachment angle: {measurements['left_attachment_angle']} degrees")
                    print(f"Right attachment angle: {measurements['right_attachment_angle']} degrees")
            
        except Exception as e:
            print(f"Error getting system info: {e}")
        
        print("=" * 31)
    
    def debug_motor_status(self):
        """Debug individual motor status"""
        print("=== Motor Status Debug ===")
        
        motors = [
            ("Left Wheel", self.left_wheel, Ports.LEFT_WHEEL),
            ("Right Wheel", self.right_wheel, Ports.RIGHT_WHEEL),
            ("Left Attachment", self.left_attachment, Ports.LEFT_ATTACHMENT),
            ("Right Attachment", self.right_attachment, Ports.RIGHT_ATTACHMENT)
        ]
        
        for name, motor, port in motors:
            print(f"{name} (Port {port}):")
            if motor is None:
                print("  Status: Not initialized")
            else:
                try:
                    angle = motor.angle()
                    speed = motor.speed()
                    print(f"  Status: Active")
                    print(f"  Angle: {angle} degrees")
                    print(f"  Speed: {speed} deg/s")
                except Exception as e:
                    print(f"  Status: Error - {e}")
            print()
        
        print("=" * 26)
    
    def safe_execute(self, operation_name, operation_func, *args, **kwargs):
        """
        Safely execute an operation with enhanced error reporting
        
        Args:
            operation_name: Name of the operation for debugging
            operation_func: Function to execute
            *args: Arguments for the function
            **kwargs: Keyword arguments for the function
            
        Returns:
            Result of the operation or None if failed
        """
        print(f"Executing: {operation_name}")
        
        try:
            result = operation_func(*args, **kwargs)
            print(f"✓ {operation_name} completed successfully")
            return result
        except Exception as e:
            print(f"✗ {operation_name} failed: {e}")
            print(f"  Error type: {type(e).__name__}")
            
            # Try to get more detailed error info
            import sys
            if hasattr(e, 'errno'):
                print(f"  Error code: {e.errno}")
            if hasattr(e, 'strerror'):
                print(f"  Error message: {e.strerror}")
            
            # System info on error
            print("  System state at error:")
            try:
                print(f"    Battery: {self.hub.battery.voltage()} mV")
                print(f"    Temperature: {self.hub.system.temperature()} °C")
                print(f"    Time: {self.hub.system.time()} ms")
            except:
                print("    Could not get system state")
            
            return None
