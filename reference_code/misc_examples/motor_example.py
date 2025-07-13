from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait

# Initialize the hub and the steering motor.
hub = PrimeHub()
steer_motor = Motor(Port.A, Direction.CLOCKWISE)

# --- Find the center of the steering mechanism ---

# Set a low speed and torque limit for finding the ends.
STALL_SPEED = 150
STALL_TORQUE = 60

# Run the motor clockwise until it stalls.
steer_motor.run_until_stalled(STALL_SPEED, then=Stop.COAST, duty_limit=STALL_TORQUE)

# Reset the angle to 0 at the clockwise end.
steer_motor.reset_angle(0)

# Run the motor counter-clockwise until it stalls.
steer_motor.run_until_stalled(-STALL_SPEED, then=Stop.HOLD, duty_limit=STALL_TORQUE)

# Get the angle at the counter-clockwise end.
full_range = steer_motor.angle()

# Calculate the center position.
center_angle = full_range / 2

# Go to the center position and wait for it to complete.
steer_motor.run_target(500, center_angle, then=Stop.HOLD, duty_limit=100)
wait(1000)

# Announce that centering is complete.
hub.speaker.beep()
print("Steering centered!")
