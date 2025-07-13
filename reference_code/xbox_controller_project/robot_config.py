"""
Robot configuration constants
Based on robot_info.md specifications
"""

from pybricks.parameters import Direction, Port

# Motor port assignments
class Ports:
    LEFT_WHEEL = Port.C
    RIGHT_WHEEL = Port.D
    LEFT_ATTACHMENT = Port.E
    RIGHT_ATTACHMENT = Port.F
    LEFT_COLOR_SENSOR = Port.A
    RIGHT_COLOR_SENSOR = Port.B

# Motor directions
class Directions:
    LEFT_WHEEL = Direction.COUNTERCLOCKWISE
    RIGHT_WHEEL = Direction.CLOCKWISE
    LEFT_ATTACHMENT = Direction.CLOCKWISE
    RIGHT_ATTACHMENT = Direction.CLOCKWISE

# Robot physical specifications (in mm)
class Specifications:
    WHEEL_DIAMETER = 56  # 5.6 cm converted to mm
    AXLE_TRACK = 80      # 8 cm converted to mm

# Controller settings
class ControllerSettings:
    DRIVE_SPEED = 300           # mm/s
    ATTACHMENT_SPEED = 500      # degrees/s
    DRIVE_ACCELERATION = 1000   # mm/s²
    TURN_RATE = 60             # degrees/s (reasonable default even though we don't use turning)
    TURN_ACCELERATION = 120    # degrees/s² (reasonable default even though we don't use turning)
