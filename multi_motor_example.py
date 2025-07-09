from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait

# Initialize the hub and two motors.
hub = PrimeHub()
motor_e = Motor(Port.E, Direction.CLOCKWISE)
motor_f = Motor(Port.F, Direction.CLOCKWISE)

# --- Example 1: Run motors to specific targets in parallel ---

print("Example 1: Running motors to targets in parallel")

# Reset both motors to 0 degrees
motor_e.reset_angle(0)
motor_f.reset_angle(0)

# Start both motors moving to their targets at the same time
# Motor E will rotate 360 degrees clockwise
# Motor F will rotate 720 degrees clockwise
motor_e.run_target(300, 360, then=Stop.HOLD, wait=False)
motor_f.run_target(300, 720, then=Stop.HOLD, wait=False)

# Wait for both motors to reach their targets
while not motor_e.done() or not motor_f.done():
    wait(10)

print("Both motors reached their targets!")
wait(1000)

# --- Example 2: Run motors at constant speed for a duration ---

print("Example 2: Running motors at constant speed")

# Start both motors running at different speeds
motor_e.run(200)   # 200 degrees per second
motor_f.run(-400)  # -400 degrees per second (opposite direction)

# Let them run for 2 seconds
wait(2000)

# Stop both motors
motor_e.stop()
motor_f.stop()

print("Motors stopped!")
wait(1000)

# --- Example 3: Synchronized movement using track_target ---

print("Example 3: Synchronized tracking movement")

# Reset angles
motor_e.reset_angle(0)
motor_f.reset_angle(0)

# Make both motors follow a synchronized pattern
for angle in range(0, 361, 10):
    # Motor E follows the angle directly
    motor_e.track_target(angle)
    # Motor F follows the negative angle (mirror movement)
    motor_f.track_target(-angle)
    wait(50)

print("Synchronized movement complete!")

# Final beep to indicate completion
hub.speaker.beep()
print("Multi-motor parallel control examples finished!")
