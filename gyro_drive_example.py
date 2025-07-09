from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Initialize the hub
hub = PrimeHub()

# Initialize motors based on your robot configuration
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)   # Left wheel motor
right_motor = Motor(Port.D, Direction.CLOCKWISE)  # Right wheel motor

# Initialize the drive base with your robot's measurements
# Wheel diameter: 5.6cm = 56mm
# Axle track: 8cm = 80mm
drive_base = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)

# Enable gyro for improved accuracy
drive_base.use_gyro(True)

print("Starting gyro-assisted driving demonstration...")

# Wait 3 seconds before starting to give time to place the robot
print("Starting demonstration in 3 seconds...")
wait(3000)

print("Starting demonstration...")

# Demonstration 1: Gyro-assisted straight driving
print("Demo 1: Driving straight with gyro assistance")
drive_base.straight(300)  # Drive forward 300mm (30cm)
wait(1000)  # Wait 1 second

print("Demo 2: Turning with gyro assistance")
drive_base.turn(90)  # Turn 90 degrees clockwise
wait(1000)

print("Demo 3: More straight driving")
drive_base.straight(200)  # Drive forward 200mm (20cm)
wait(1000)

print("Demo 4: Turn left")
drive_base.turn(-90)  # Turn 90 degrees counterclockwise
wait(1000)

print("Demo 5: Return to start")
drive_base.straight(200)  # Drive forward 200mm
wait(1000)

print("Demo 6: Final turn to original orientation")
drive_base.turn(-90)  # Turn 90 degrees counterclockwise
wait(1000)

print("Demo 7: Return to original position")
drive_base.straight(-300)  # Drive backward 300mm
wait(1000)

print("Demo 8: Final turn to complete the square")
drive_base.turn(90)  # Turn 90 degrees clockwise

print("Demonstration complete!")

# Optional: Show the robot's estimated position
distance_traveled = drive_base.distance()
angle_turned = drive_base.angle()
print(f"Total distance traveled: {distance_traveled}mm")
print(f"Total angle turned: {angle_turned} degrees")

# Reset the measurements for future use
drive_base.reset()
print("Drive base measurements reset.")
