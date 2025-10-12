"""
Port Finder - Motors & Sensors
This program checks all ports on your SPIKE Prime hub and tells you what's connected.
It will detect motors, color sensors, distance sensors, and force sensors.
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize the hub
hub = PrimeHub()

print("=== PORT FINDER ===")
print("Checking all ports for motors and sensors...")
print("")

# List of all available ports
all_ports = [Port.A, Port.B, Port.C, Port.D, Port.E, Port.F]
port_names = ["A", "B", "C", "D", "E", "F"]

# Store what we find
port_info = {}

# Check each port
for i, port in enumerate(all_ports):
    port_name = port_names[i]
    device_type = None

    # Try Motor
    try:
        device = Motor(port)
        device_type = "Motor"
        # Make it run longer so you can easily identify it
        print(f"  ** Motor on Port {port_name} is running NOW! **")
        device.run_time(500, 3000)  # Run at 500 deg/s for 3 seconds
        wait(500)  # Short pause
        device.run_time(-500, 3000)  # Run backwards for 3 seconds
        wait(500)
    except:
        pass

    # Try Color Sensor
    if device_type is None:
        try:
            device = ColorSensor(port)
            device_type = "Color Sensor"
            # Flash the lights so you can identify it
            print(f"  ** Color Sensor on Port {port_name} is flashing NOW! **")
            from pybricks.parameters import Color
            for _ in range(6):  # Flash 6 times
                device.lights.on(100)  # Turn on bright white
                wait(300)
                device.lights.off()
                wait(300)
            # Read the color to verify it works
            color = device.color()
            print(f"  (Detected color: {color})")
        except:
            pass

    # Try Ultrasonic/Distance Sensor
    if device_type is None:
        try:
            device = UltrasonicSensor(port)
            device_type = "Distance Sensor"
            # Read distance to verify it works
            distance = device.distance()
            print(f"  (Detected distance: {distance}mm)")
        except:
            pass

    # Try Force Sensor
    if device_type is None:
        try:
            device = ForceSensor(port)
            device_type = "Force Sensor"
            # Read force to verify it works
            force = device.force()
            print(f"  (Detected force: {force}N)")
        except:
            pass

    # Report what we found
    if device_type:
        print(f"Port {port_name}: {device_type} FOUND!")
        port_info[port_name] = device_type
    else:
        print(f"Port {port_name}: empty")

    wait(300)  # Small delay between checks

# Show summary
print("")
print("=== SUMMARY ===")
if len(port_info) > 0:
    for port_name, device_type in port_info.items():
        print(f"  Port {port_name}: {device_type}")
    print(f"\nTotal devices: {len(port_info)}")
else:
    print("No devices found. Check your connections!")

# Show count on hub display
hub.display.number(len(port_info))
wait(2000)

# Show each port letter on display
for port_name in port_info.keys():
    hub.display.text(port_name)
    wait(800)

print("")
print("Done! Check the summary above.")
print("Motors wiggled when detected to help you identify them.")
