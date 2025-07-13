"""
Season Configuration
Base configuration for all missions in the season with robot specifications and defaults
"""

from pybricks.parameters import Direction, Port, Color

# Robot Hardware Configuration
class Ports:
    """Robot port assignments"""
    LEFT_WHEEL = Port.C
    RIGHT_WHEEL = Port.D
    LEFT_ATTACHMENT = Port.E
    RIGHT_ATTACHMENT = Port.F
    LEFT_COLOR_SENSOR = Port.A
    RIGHT_COLOR_SENSOR = Port.B

class Directions:
    """Motor direction settings"""
    LEFT_WHEEL = Direction.COUNTERCLOCKWISE
    RIGHT_WHEEL = Direction.CLOCKWISE
    LEFT_ATTACHMENT = Direction.CLOCKWISE
    RIGHT_ATTACHMENT = Direction.CLOCKWISE

class Specifications:
    """Robot physical specifications (in mm)"""
    WHEEL_DIAMETER = 56  # 5.6 cm converted to mm
    AXLE_TRACK = 80      # 8 cm converted to mm

# Season-wide Default Settings
class SeasonDefaults:
    """Default settings that can be overridden by individual missions"""
    DRIVE_SPEED = 200           # mm/s - Conservative speed for accuracy
    TURN_RATE = 60             # degrees/s
    DRIVE_ACCELERATION = 800    # mm/s²
    TURN_ACCELERATION = 120     # degrees/s²
    
    # Display settings
    DISPLAY_DELAY = 500         # ms between display updates
    COMPLETION_BEEP_FREQ = 800  # Hz
    COMPLETION_BEEP_TIME = 200  # ms
    
    # Mission feedback colors
    MISSION_START_COLOR = Color.BLUE
    MISSION_SUCCESS_COLOR = Color.GREEN
    MISSION_ERROR_COLOR = Color.RED
    MISSION_RUNNING_COLOR = Color.YELLOW

# Season Information
class SeasonInfo:
    """Season metadata"""
    NAME = "Shape Demonstration Season"
    VERSION = "1.0"
    DESCRIPTION = "Example season showcasing robot driving in shapes and displaying patterns"
