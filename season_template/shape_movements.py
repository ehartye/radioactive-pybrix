"""
Shape Movements
Common geometric movement functions for robot missions
"""

from pybricks.tools import wait
import umath as math


class ShapeMovements:
    """Collection of shape-based movement functions"""
    
    def __init__(self, robot_controller):
        """
        Initialize shape movements
        
        Args:
            robot_controller: RobotController instance
        """
        self.robot = robot_controller
        self.drivebase = robot_controller.drivebase
    
    def drive_square(self, side_length=300, pause_at_corners=True):
        """
        Drive robot in a square pattern
        
        Args:
            side_length: Length of each side in mm
            pause_at_corners: Whether to pause briefly at each corner
        """
        if not self.robot.is_initialized:
            raise RuntimeError("Robot not initialized")
        
        print(f"Driving square with {side_length}mm sides")
        
        for corner in range(4):
            # Drive straight for one side
            self.drivebase.straight(side_length)
            
            if pause_at_corners:
                wait(500)
            
            # Turn 90 degrees clockwise
            self.drivebase.turn(-90)
            
            if pause_at_corners:
                wait(500)
        
        print("Square drive complete")
    
    def drive_rectangle(self, width=300, height=200, pause_at_corners=True):
        """
        Drive robot in a rectangle pattern
        
        Args:
            width: Width of rectangle in mm
            height: Height of rectangle in mm
            pause_at_corners: Whether to pause briefly at each corner
        """
        if not self.robot.is_initialized:
            raise RuntimeError("Robot not initialized")
        
        print(f"Driving rectangle {width}mm x {height}mm")
        
        for side in range(2):
            # Drive width
            self.drivebase.straight(width)
            if pause_at_corners:
                wait(500)
            self.drivebase.turn(-90)
            if pause_at_corners:
                wait(500)
            
            # Drive height
            self.drivebase.straight(height)
            if pause_at_corners:
                wait(500)
            self.drivebase.turn(-90)
            if pause_at_corners:
                wait(500)
        
        print("Rectangle drive complete")
    
    def drive_triangle(self, side_length=300, pause_at_corners=True):
        """
        Drive robot in an equilateral triangle pattern
        
        Args:
            side_length: Length of each side in mm
            pause_at_corners: Whether to pause briefly at each corner
        """
        if not self.robot.is_initialized:
            raise RuntimeError("Robot not initialized")
        
        print(f"Driving triangle with {side_length}mm sides")
        
        for corner in range(3):
            # Drive straight for one side
            self.drivebase.straight(side_length)
            
            if pause_at_corners:
                wait(500)
            
            # Turn 120 degrees clockwise (exterior angle of equilateral triangle)
            self.drivebase.turn(-120)
            
            if pause_at_corners:
                wait(500)
        
        print("Triangle drive complete")
    
    def drive_circle(self, radius=150, clockwise=True):
        """
        Drive robot in a circle pattern
        
        Args:
            radius: Circle radius in mm
            clockwise: Direction of circle (True for clockwise)
        """
        if not self.robot.is_initialized:
            raise RuntimeError("Robot not initialized")
        
        print(f"Driving circle with {radius}mm radius")
        
        # Calculate circumference
        circumference = 2 * math.pi * radius
        
        # Calculate the turn rate needed for the circle
        # For a smooth circle, we need to turn while moving
        # Turn rate = (speed / radius) * (180 / pi) to convert to degrees/second
        drive_speed = self.robot.config.get('drive_speed', 200)
        turn_rate = (drive_speed / radius) * (180 / math.pi)
        
        # Adjust direction
        if not clockwise:
            turn_rate = -turn_rate
        
        # Drive in circle by combining straight movement with turning
        duration = (circumference / drive_speed) * 1000  # Convert to milliseconds
        
        self.drivebase.drive(drive_speed, turn_rate)
        wait(int(duration))
        self.drivebase.stop()
        
        print("Circle drive complete")
    
    def drive_figure_eight(self, radius=100):
        """
        Drive robot in a figure-eight pattern
        
        Args:
            radius: Radius of each circle in the figure-eight
        """
        if not self.robot.is_initialized:
            raise RuntimeError("Robot not initialized")
        
        print(f"Driving figure-eight with {radius}mm radius circles")
        
        # First circle (clockwise)
        self.drive_circle(radius, clockwise=True)
        
        # Brief pause at intersection
        wait(500)
        
        # Second circle (counter-clockwise)
        self.drive_circle(radius, clockwise=False)
        
        print("Figure-eight drive complete")
    
    def drive_zigzag(self, segment_length=200, angle=45, segments=6):
        """
        Drive robot in a zigzag pattern
        
        Args:
            segment_length: Length of each zigzag segment in mm
            angle: Angle of zigzag turns in degrees
            segments: Number of segments to drive
        """
        if not self.robot.is_initialized:
            raise RuntimeError("Robot not initialized")
        
        print(f"Driving zigzag with {segments} segments")
        
        # Start with first segment
        self.drivebase.straight(segment_length)
        
        for segment in range(segments - 1):
            # Alternate turn direction
            turn_angle = angle if segment % 2 == 0 else -angle
            self.drivebase.turn(turn_angle)
            
            # Drive next segment
            self.drivebase.straight(segment_length)
        
        print("Zigzag drive complete")
    
    def drive_spiral(self, start_radius=50, end_radius=200, turns=3):
        """
        Drive robot in an outward spiral pattern
        
        Args:
            start_radius: Starting radius in mm
            end_radius: Ending radius in mm
            turns: Number of complete turns in the spiral
        """
        if not self.robot.is_initialized:
            raise RuntimeError("Robot not initialized")
        
        print(f"Driving spiral from {start_radius}mm to {end_radius}mm")
        
        drive_speed = self.robot.config.get('drive_speed', 200)
        
        # Calculate spiral parameters
        radius_increment = (end_radius - start_radius) / turns
        
        for turn in range(turns):
            current_radius = start_radius + (turn * radius_increment)
            
            # Calculate turn rate for current radius
            turn_rate = (drive_speed / current_radius) * (180 / math.pi)
            
            # Drive one complete turn at current radius
            circumference = 2 * math.pi * current_radius
            duration = (circumference / drive_speed) * 1000
            
            self.drivebase.drive(drive_speed, -turn_rate)  # Negative for clockwise
            wait(int(duration))
        
        self.drivebase.stop()
        print("Spiral drive complete")
