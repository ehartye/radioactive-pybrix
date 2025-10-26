# PyBricks Learning Project - Middle School Robotics

## Project Overview
This is a learning environment for middle school students working with **LEGO SPIKE Prime** using PyBricks (Python programming). The goal is to teach fundamental programming concepts through hands-on robotics.

**Primary Platform**: LEGO SPIKE Prime hub
**Programming Environment**: PyBricks MicroPython

## Target Audience
- **Age Level**: Middle school students (grades 6-8)
- **Experience Level**: Beginner to intermediate Python programmers
- **Learning Goals**:
  - Understand basic Python syntax and structure
  - Learn to control motors, sensors, and displays
  - Build problem-solving skills through robotics challenges
  - Develop computational thinking and debugging skills

## Communication Style
When helping students:
- Use clear, simple language appropriate for middle school level
- Break down complex concepts into smaller, digestible steps
- Encourage experimentation and learning from mistakes
- Provide encouraging feedback and celebrate successes
- Use analogies and real-world examples when explaining concepts
- Avoid overly technical jargon unless teaching it explicitly

## Project Structure

This repository provides a complete season management system for students:

### Interactive Training (`training/`)
Before students start building, they should take the interactive training quiz:
- **`launch_training.py`**: Launcher script to open training in browser
- **`quiz.html/js/css`**: Interactive presentation and quiz system
- **`README.md`**: Training documentation for educators
- **Topics covered**: Python basics, Python vs block programming, PyBricks overview, libraries, project workflow
- **Format**: 15 presentation slides + 12 quiz questions with immediate feedback
- **Key benefits explained**: Source control (Git), professional skills, easier collaboration, more powerful logic

### Season Management Tools (Root Level)
- **`new_season.py`**: Interactive script to create a new season folder with robot-specific configuration
- **`new_mission.py`**: Interactive script to add missions to a season (auto-updates menu)
- **`STUDENT_GUIDE.md`**: Complete walkthrough for students to create seasons and missions

### Season Template (`season_template/`)
Template files used by the scripts (students don't edit these directly):
- **`_template_mission_simple.py`**: Minimal mission template with quick-start examples
- **`_template_mission_guided.py`**: Full mission template with detailed comments (default)
- **`season_config.py.template`**: Robot configuration template with placeholders
- **`season_menu.py.template`**: Menu system template with placeholders
- **Shared utilities**: `robot_controller.py`, `display_patterns.py`, `line_movements.py`

### Working Example (`season_example/`)
Complete working example with 4 FLL-realistic missions students can learn from:
- **`mission_01_drive_to_target.py`**: Navigate to precise position (basic FLL pattern)
- **`mission_02_attachment_demo.py`**: Using attachment motors for mechanisms
- **`mission_03_display_feedback.py`**: Display/sound feedback (no motors - good for testing!)
- **`mission_04_line_following.py`**: Using color sensors for precision positioning
- **`season_menu.py`**: Mission selector menu
- **`season_config.py`**: Robot-specific configuration
- **`archive/`**: Alternative mission examples (square drive, circle drive, display patterns, triangle combo) - not in menu but available as reference

### Reference Documentation (`reference_docs/`)
Contains excerpts from official PyBricks documentation covering:
- **prime_hub.txt**: Hub features (display, buttons, IMU/tilt sensor, lights, speaker, battery)
- **motors.txt**: Motor control (running, stopping, measuring position/speed)
- **robotics_drive_bases.txt**: DriveBase class for two-wheeled robots
- **icon.txt**: Built-in display icons and custom patterns
- **menu.txt**: Creating menu systems for program selection

### Reference Code (`reference_code/`)
Working code examples demonstrating key concepts:
- **misc_examples/**: Single-file examples (motors, drive bases, tilt sensors)
- **menu_example/**: Multi-file project showing program organization
- **xbox_controller_project/**: Advanced remote control example
- **cryptid_example/**: Complex multi-file project structure

## Key Concepts to Teach - What Students Actually Write

**IMPORTANT:** Students in this project **never initialize the robot themselves**. The RobotController handles all setup automatically. Students receive a pre-configured `robot` object and just write movement logic!

### 1. The Mission Function - Your Starting Point

```python
def run(robot: RobotController):
    """Every mission follows this pattern"""
    # The robot is already initialized for you!
    # You have access to:
    #   robot.drivebase          - Drive the robot
    #   robot.hub                - Hub features (display, buttons, sensors, speaker, light)
    #   robot.display            - Display helper (countdown, checkmarks, animations)
    #   robot.left_attachment    - Left attachment motor (if configured)
    #   robot.right_attachment   - Right attachment motor (if configured)
    #   robot.left_color_sensor  - Left color sensor (if configured)
    #   robot.right_color_sensor - Right color sensor (if configured)
```

**Key Teaching Points:**
- Every mission has a `run()` function that receives a `robot` parameter
- **No initialization needed** - just start driving!
- Robot configuration (ports, wheel size, speeds) lives in `season_config.py`
- Students focus on **what the robot should do**, not **how to set it up**

### 2. Basic Driving - 90% of Missions
```python
# Drive straight forward 300mm
robot.drivebase.straight(300)

# Drive backward 200mm (negative number)
robot.drivebase.straight(-200)

# Turn right 90 degrees
robot.drivebase.turn(90)

# Turn left 90 degrees (negative number)
robot.drivebase.turn(-90)

# Complete mission example:
robot.drivebase.straight(500)    # Drive forward
robot.drivebase.turn(90)         # Turn right
robot.drivebase.straight(300)    # Drive forward again
robot.drivebase.turn(-90)        # Turn left
robot.drivebase.straight(500)    # Return
```

**Key Teaching Points:**
- **DriveBase is pre-configured** with correct wheel size and motor directions
- **Gyro is automatically enabled** for accurate turns (no drift!)
- **Distances** in millimeters (mm) - 1000mm = 1 meter
- **Angles** in degrees (°) - 360° = full circle
- **Positive** = forward/right, **Negative** = backward/left
- Speed and acceleration already set in config (can override per mission)

**Advanced Driving (optional):**
```python
# Drive forward continuously at 100 mm/s (until you call stop)
robot.drivebase.drive(100, 0)

# Drive and turn at same time (100 mm/s forward, 30 deg/s turn)
robot.drivebase.drive(100, 30)

# Stop the robot
robot.drivebase.stop()
```

### 3. Hub Display
```python
# Show a number
robot.hub.display.number(42)

# Show scrolling text
robot.hub.display.text("GO!")

# Show built-in icon
from pybricks.parameters import Icon
robot.hub.display.icon(Icon.HEART)

# Turn on single pixel (row, col) - both 0-4
robot.hub.display.pixel(2, 2)

# Clear display
robot.hub.display.off()

# Display helper shortcuts
robot.display.show_countdown(3)               # Count down 3-2-1
robot.display.show_completion_checkmark()     # Show success checkmark
```

**Key Teaching Points:**

- Display is 5×5 grid of LEDs
- Can show numbers, text (scrolls if long), icons, or custom patterns
- `robot.display` provides helpful shortcuts for common patterns (countdown, checkmarks, animations, progress bars)
- For direct display control, use `robot.hub.display` (for numbers, text, icons, pixels)

### 4. Hub Buttons
```python
from pybricks.parameters import Button

# Check which buttons are pressed
pressed = robot.hub.buttons.pressed()

if Button.LEFT in pressed:
    # Left button was pressed
    robot.hub.display.text("<")

if Button.RIGHT in pressed:
    # Right button was pressed
    robot.hub.display.text(">")

if Button.CENTER in pressed:
    # Center button was pressed
    robot.hub.display.text("GO!")
```

**Key Teaching Points:**

- Three buttons: LEFT, RIGHT, CENTER (located on hub below display)
- `pressed()` returns a list of currently pressed buttons
- Use `in` to check if specific button is in the list
- Useful for manual triggers or mode selection within missions

### 5. Tilt/Gyro/IMU Sensor
```python
# Get tilt angles (-180 to 180 degrees)
pitch, roll = robot.hub.imu.tilt()
print(f"Pitch: {pitch}, Roll: {roll}")

# Check which side is facing up
from pybricks.parameters import Side
up_side = robot.hub.imu.up()
if up_side == Side.TOP:
    print("Hub is right-side up!")

# Get compass heading (0-360 degrees)
heading = robot.hub.imu.heading()
print(f"Heading: {heading} degrees")

# Check if robot is stationary
if robot.hub.imu.stationary():
    print("Robot is not moving")

# Get acceleration (in mm/s²)
ax, ay, az = robot.hub.imu.acceleration()
```

**Key Teaching Points:**

- IMU = "Inertial Measurement Unit" (gyro + accelerometer)
- **Gyro is automatically used for accurate turns** - students don't need to enable it
- Tilt angles useful for detecting if robot is on a ramp
- `up()` useful for orientation detection
- `heading()` gives compass direction (resets when robot initializes)

### 6. Hub Light (Status LED)
```python
from pybricks.parameters import Color

# Turn light on
robot.hub.light.on(Color.RED)
robot.hub.light.on(Color.GREEN)
robot.hub.light.on(Color.BLUE)

# Turn light off
robot.hub.light.off()

# Blink pattern (500ms on, 500ms off, repeat)
robot.hub.light.blink(Color.GREEN, [500, 500])
```

**Key Teaching Points:**

- This is the **status light around the center button**, not the display
- Useful for showing mission status or debugging
- RobotController automatically manages light color during missions (start/success/error)
- Custom colors: `Color(h=180, s=100, v=100)` (hue, saturation, value)

### 7. Speaker/Sounds
```python
# Simple beep
robot.hub.speaker.beep()

# Custom beep (frequency in Hz, duration in ms)
robot.hub.speaker.beep(frequency=800, duration=200)

# Play note (musical note, duration in ms)
from pybricks.parameters import Note
robot.hub.speaker.play_notes([
    (Note.C4, 500),
    (Note.E4, 500),
    (Note.G4, 500)
])

# Set volume (0-100%)
robot.hub.speaker.volume(50)
```

**Key Teaching Points:**

- RobotController automatically beeps at mission start/success/error
- Students can add custom beeps for feedback or debugging
- Musical notes useful for creative projects (play tunes!)

### 8. Waiting/Delays
```python
from pybricks.tools import wait

# Wait 1 second (1000 milliseconds)
wait(1000)

# Wait 2.5 seconds
wait(2500)

# Common pattern: run motor, wait, stop motor
if robot.left_attachment:
    robot.left_attachment.run(500)
    wait(1000)  # Run for 1 second
    robot.left_attachment.stop()
```

**Key Teaching Points:**

- **Time is in milliseconds (ms)** - 1000ms = 1 second
- `wait()` pauses program execution
- Useful for precise timing between movements
- Don't confuse with `sleep()` (that's regular Python, not available here)

### 9. Attachment Motors (If Configured)
```python
# Check if attachment exists before using
if robot.left_attachment:
    # Run continuously at 500 deg/s
    robot.left_attachment.run(500)

    # Run for specific time (using wait)
    robot.left_attachment.run(500)
    wait(1000)  # Run for 1 second
    robot.left_attachment.stop()

    # Run to specific angle
    robot.left_attachment.run_angle(500, 90)  # Turn 90 degrees at 500 deg/s

    # Run until stalled (hits resistance)
    robot.left_attachment.run_until_stalled(200)

    # Get current angle
    angle = robot.left_attachment.angle()
    print(f"Attachment angle: {angle}")

# Same methods work for right attachment
if robot.right_attachment:
    robot.right_attachment.run_angle(300, 180)
```

**Key Teaching Points:**

- Attachments are **optional** (not all robots have them)
- **Always check with `if`** before using to avoid errors
- Configured in `season_config.py` with ports and directions
- Useful for claws, lifts, spinning mechanisms, etc.
- Angles measured in degrees, speeds in degrees per second

### 10. Color Sensors (If Configured)
```python
# Check if sensor exists before using
if robot.left_color_sensor:
    # Get reflected light intensity (0-100%)
    reflection = robot.left_color_sensor.reflection()
    print(f"Reflection: {reflection}%")

    # Detect color
    from pybricks.parameters import Color
    color = robot.left_color_sensor.color()
    if color == Color.BLACK:
        print("Detected black line!")

    # Get ambient light
    ambient = robot.left_color_sensor.ambient()

    # Get RGB values
    hue, saturation, value = robot.left_color_sensor.hsv()

# Common pattern: drive until seeing black line
if robot.left_color_sensor:
    robot.drivebase.drive(100, 0)  # Start driving
    while robot.left_color_sensor.reflection() > 20:
        wait(10)  # Check every 10ms
    robot.drivebase.stop()  # Stop when black detected
```

**Key Teaching Points:**

- Color sensors are **optional** (not all robots have them)
- **Always check with `if`** before using
- Useful for line following, color sorting, detecting edges
- `reflection()` most common - lower values = darker surfaces
- Black lines typically have reflection < 25%

## Understanding the RobotController Pattern

**CRITICAL for AI Assistants:** When students ask about hub features (gyro/IMU, buttons, display, speaker, light, battery), remember the inheritance chain:

### The Pattern
```python
# In RobotController class (robot_controller.py)
class RobotController:
    def __init__(self):
        self.hub = PrimeHub()  # ← Hub is wrapped here
        # ...

# In mission files
def run(robot: RobotController):
    # Students access hub features through robot.hub:
    robot.hub.imu.tilt()           # ✅ Correct
    robot.hub.buttons.pressed()    # ✅ Correct
    robot.hub.display.icon(...)    # ✅ Correct (direct display control)
    robot.hub.speaker.beep()       # ✅ Correct
    robot.hub.light.on(Color.RED)  # ✅ Correct

    # Or use the display helper for common patterns:
    robot.display.show_countdown(3)              # ✅ Correct (helper methods)
    robot.display.show_completion_checkmark()    # ✅ Correct
```

### What Students Have Access To

Through the `robot` parameter in mission functions:
- **`robot.drivebase`** - Drive the robot (straight, turn, drive, stop)
- **`robot.display`** - Display helper for common patterns (countdown, checkmarks, animations, progress bars)
- **`robot.hub`** - **ALL hub features**:
  - `robot.hub.imu` - Gyro/tilt sensor, heading, acceleration
  - `robot.hub.buttons` - Button presses
  - `robot.hub.display` - Direct display control (numbers, text, icons, pixels)
  - `robot.hub.speaker` - Sounds and beeps
  - `robot.hub.light` - Hub status light
  - `robot.hub.battery` - Battery info
  - `robot.hub.system` - System functions
- **`robot.left_attachment`** / **`robot.right_attachment`** - Attachment motors (if configured)
- **`robot.left_color_sensor`** / **`robot.right_color_sensor`** - Color sensors (if configured)

### When Students Ask "How do I use [feature]?"

**ALWAYS consider:** They have a `robot: RobotController` parameter with everything built-in

**Examples:**
- "How do I show a countdown?" → `robot.display.show_countdown(3)`
- "How do I show a checkmark?" → `robot.display.show_completion_checkmark()`
- "How do I show a number?" → `robot.hub.display.number(5)` (direct display control)
- "How do I use the gyro?" → `robot.hub.imu.tilt()` or `robot.hub.imu.heading()`
- "How do I check buttons?" → `robot.hub.buttons.pressed()`
- "How do I make a beep?" → `robot.hub.speaker.beep()`
- "How do I change the hub light?" → `robot.hub.light.on(Color.GREEN)`
- "How do I check battery?" → `robot.hub.battery.voltage()`

**Key distinction:**
- `robot.display.*` - Helper methods for common patterns (countdown, checkmarks, animations, progress bars)
- `robot.hub.display.*` - Direct display control (numbers, text, icons, pixels, off)

### Why This Pattern?

The RobotController wraps initialization and configuration so students don't have to:
- ✅ Hub already initialized
- ✅ Motors already configured with correct ports and directions
- ✅ DriveBase already created with correct wheel/axle measurements
- ✅ Attachments already set up (if configured)
- ✅ **Gyro automatically enabled** for accurate driving and turns

Students just use `robot.*` - everything is ready to go!

### IMPORTANT: Check the Actual Implementation First!

**Before answering questions about robot features, ALWAYS check the actual `robot_controller.py` implementation in the student's season folder.**

Common questions where you MUST check the implementation:
- **"Does drive straight use gyro?"** → Check if `drivebase.use_gyro(True)` is called in `initialize()`
- **"What speed does the robot drive at?"** → Check the `drivebase.settings()` configuration
- **"How do I access [feature]?"** → Check what's exposed through `robot.*` attributes
- **"Is [feature] already set up?"** → Check the `initialize()` method

**Example: Gyro Question**
❌ **Wrong approach:** Give generic PyBricks answer about `heading_control` parameter
✅ **Right approach:** Check `robot_controller.py` line ~179 and say "Yes! Gyro is already enabled by default in the `initialize()` method with `self.drivebase.use_gyro(True)`"

**Why this matters:**
- This project has custom abstractions that differ from vanilla PyBricks
- Students are using **this specific codebase**, not generic PyBricks
- The `robot_controller.py` already handles most setup automatically
- Giving generic answers can confuse students about what's already done for them

## Common Student Challenges

### Challenge 1: "My robot drives backwards!"

**Solution**: Update motor direction in `season_config.py`

```python
# In season_config.py, change the direction:
from pybricks.parameters import Direction

class Directions:
    LEFT_WHEEL = Direction.COUNTERCLOCKWISE  # ← Change this
    RIGHT_WHEEL = Direction.CLOCKWISE
```

**Key Point**: Students don't initialize motors in their missions - they configure them in `season_config.py`

### Challenge 2: "The robot doesn't turn the right amount!"

**Solution**: Calibrate measurements in `season_config.py`

```python
# In season_config.py, adjust these values:
class Specifications:
    WHEEL_DIAMETER = 56  # Measure actual wheel diameter (mm)
    AXLE_TRACK = 115     # Measure distance between wheel centers (mm)
```

**Debugging tips**:

- Measure wheel diameter with ruler
- Measure axle track (distance between wheel contact points)
- Test with `robot.drivebase.turn(360)` - should turn exactly once
- If it turns too much, increase AXLE_TRACK; too little, decrease it

### Challenge 3: "My motors are too slow/fast!"

**Solution**: Adjust speed settings in `season_config.py` or mission config

```python
# Option 1: Change defaults in season_config.py
class SeasonDefaults:
    DRIVE_SPEED = 300         # Increase for faster (mm/s)
    TURN_RATE = 100           # Increase for faster turns (deg/s)

# Option 2: Override in specific mission
MISSION_CONFIG = {
    "drive_speed": 500,       # Faster for this mission
    "turn_rate": 150,
}
```

**Key Point**: Speed configuration is separate from mission logic!

### Challenge 4: "I get an error about attachments/sensors not existing!"

**Solution**: Always check if optional components exist before using

```python
# WRONG - crashes if no attachment
robot.left_attachment.run(500)

# RIGHT - safe check first
if robot.left_attachment:
    robot.left_attachment.run(500)
else:
    print("No left attachment configured!")
```

**Key Point**: Only wheel motors are required. Attachments and sensors are optional and must be checked.

### Challenge 5: "I don't know what went wrong!"

**Solution**: Use print statements for debugging

```python
# Print robot state
print("Distance traveled:", robot.drivebase.distance())
print("Angle turned:", robot.drivebase.angle())

# Print hub state
pitch, roll = robot.hub.imu.tilt()
print(f"Tilt: pitch={pitch}, roll={roll}")

# Print attachment state
if robot.left_attachment:
    print("Attachment angle:", robot.left_attachment.angle())
```

**Advanced debugging**:

```python
# Get system info
robot.get_system_info()      # Shows battery, temperature, connections
robot.debug_motor_status()   # Shows all motor angles and speeds
```

### Challenge 6: "I can't find my ports/configuration!"

**Solution**: Everything is in `season_config.py` - never in mission files

```python
# Look in season_config.py to see your robot setup:
class Ports:
    LEFT_WHEEL = Port.C
    RIGHT_WHEEL = Port.D
    LEFT_ATTACHMENT = Port.A    # ← Your ports are here
    RIGHT_ATTACHMENT = Port.B
```

**Key Point**: Use `new_season.py` script to set this up correctly from the start!

## Example Project Ideas for Students

### Beginner Projects
1. **Traffic Light**: Use hub light to create red/yellow/green sequence
2. **Emoji Display**: Show different emotions on hub display
3. **Motor Explorer**: Make a motor run in different ways (speed, angle, time)
4. **Button Counter**: Count button presses and show on display

### Intermediate Projects
1. **Line Following Robot**: Use color sensor to follow a line
2. **Obstacle Avoider**: Use distance sensor to avoid walls
3. **Dance Robot**: Create choreographed movement routine
4. **Spirit Level**: Use tilt sensor to show when surface is level
5. **Menu System**: Create a program selector with multiple modes

### Advanced Projects
1. **Remote Control Robot**: Control with another hub or controller
2. **Maze Solver**: Navigate through a maze autonomously
3. **Sumo Robot**: Push opponent out of ring
4. **Drawing Robot**: Use motors to draw shapes

## Code Quality Guidelines for Students

### Good Practices to Encourage:
1. **Comments**: Explain what code does
   ```python
   # Initialize the hub
   hub = PrimeHub()
   ```

2. **Descriptive Names**: Use clear variable names
   ```python
   # Good
   left_motor = Motor(Port.C)
   # Less clear
   m1 = Motor(Port.C)
   ```

3. **Organization**: Group related code together
   ```python
   # Setup section
   hub = PrimeHub()
   motor = Motor(Port.A)

   # Main program section
   motor.run(500)
   wait(2000)
   motor.stop()
   ```

4. **Testing**: Test small parts before combining
5. **Incremental Changes**: Make one change at a time

### Common Mistakes to Watch For:
1. Forgetting to import modules
2. Using wrong port letters
3. Forgetting `wait()` or `await` keywords
4. Mixing up angles (degrees) and distances (mm)
5. Not initializing hub before using it
6. Infinite loops without exit conditions

## How to Help Students Debug

1. **Read Error Messages Together**: Explain what they mean
2. **Check the Basics**:
   - Are motors plugged into correct ports?
   - Is code spelling/capitalization correct?
   - Are all imports at the top?
3. **Add Print Statements**: Help students see what's happening
4. **Simplify**: Break complex code into smaller testable pieces
5. **Compare to Examples**: Look at reference code for patterns

## Season Management Workflow

### IMPORTANT: PyBricks Import Limitation
**PyBricks MicroPython does NOT support subdirectories or package imports.** All Python files must be in a flat structure in the same directory. This is a known limitation (GitHub Issue #1602).

All imports must be simple module imports:
```python
# CORRECT - flat imports
import mission_01_square_drive
from robot_controller import RobotController
from season_config import SeasonDefaults

# INCORRECT - will not work on hub
from missions import mission_01_square_drive
from .shared import RobotController
```

### Creating a New Season

**For Students - Use the automated scripts!**

1. **Create Season** - Run `python new_season.py`:
   - Asks about season name, team name
   - Asks where motors are plugged in (ports)
   - Asks for robot measurements (wheel diameter, axle track)
   - Generates folder with `season_config.py` customized for their robot
   - Creates empty `season_menu.py` ready for missions
   - Copies shared utility files

2. **Add Missions** - From season folder, run `python ../new_mission.py`:
   - Asks for mission name and description
   - Asks for speed settings
   - Creates mission file from template with helpful code examples
   - **Automatically updates `season_menu.py`** (imports, dict, hub_menu options)
   - Students just need to fill in the mission logic!

3. **Code Mission** - Edit the generated mission file:
   - Template includes helpful examples in comments
   - Shows how to drive, turn, display, wait, use attachments
   - Students uncomment and modify examples they need

4. **Upload and Test**:
   - Upload `season_menu.py` to SPIKE Prime hub (PyBricks automatically uploads imported files!)
   - All `.py` files must be in the same folder on the computer (flat structure)
   - Run `season_menu.py` on the hub
   - Use hub buttons to select and run missions

### For AI Assistants Helping Students

**If a student asks about creating a season or mission:**
1. Direct them to use `new_season.py` or `new_mission.py` scripts
2. Explain they answer simple questions and everything is generated
3. Show them `STUDENT_GUIDE.md` for complete walkthrough
4. Do NOT tell them to manually copy/edit template files

**If a student asks about mission code:**
1. Ask if they want Simple or Guided template (new_mission.py prompts for this)
2. **Simple template** = minimal with quick-start examples (for experienced students)
3. **Guided template** = full examples with detailed comments (recommended for beginners)
4. Guide them to use `robot.drivebase` directly - this is the primary FLL pattern
5. Remind them about flat imports (no subdirectories)
6. All files must be in same folder - PyBricks auto-uploads imported files when uploading season_menu.py

**Important: Use Direct DriveBase Commands**
- Real FLL missions use `robot.drivebase.straight()` and `robot.drivebase.turn()`
- This is more precise and easier to understand than helper libraries
- Example: `robot.drivebase.straight(427)` to drive exact distance to target
- Students should write straightforward navigation code, not use abstraction layers

**If helping debug:**
1. Check all `.py` files are in same folder on computer (PyBricks auto-uploads via imports)
2. Check they uploaded `season_menu.py` to hub and ran it
3. Check imports are flat (no `from missions.` or `from shared.`)
4. Check ports in `season_config.py` match physical robot
5. Check wheel measurements in `season_config.py` are accurate

### Example Mission Template Structure

Every generated mission includes helpful guidance:
```python
# TODO: ADD YOUR MISSION LOGIC HERE

# --- BASIC DRIVING ---
# Most missions just need these simple movements:

# Drive straight forward 300mm:
#   robot.drivebase.straight(300)
#
# Turn right 90 degrees:
#   robot.drivebase.turn(90)
#
# Example mission - drive to target and back:
#   robot.drivebase.straight(500)    # Drive forward 500mm
#   robot.drivebase.turn(180)        # Turn around
#   robot.drivebase.straight(500)    # Drive back 500mm

# --- ATTACHMENTS (if you have them) ---
# Run attachment motor:
#   if robot.left_attachment:
#       robot.left_attachment.run(500)
#       from pybricks.tools import wait
#       wait(1000)
#       robot.left_attachment.stop()

# --- DISPLAY (optional) ---
# Show countdown:
#   robot.display.show_countdown(3)

# --- ADVANCED: LINE FOLLOWING (if you have color sensors) ---
# Square on a black line for precise positioning:
#   from line_movements import LineMovements
#   line_moves = LineMovements(robot)
#   line_moves.square_on_line()
```

**Template Styles:**
- **Simple**: Quick-start section + minimal examples (good for experienced students)
- **Guided**: Quick-start + comprehensive examples organized by category (default)
- Students choose when running `new_mission.py`

Students use direct `robot.drivebase` API - simple, clear, and precise!

## Available Resources in This Project

Students can explore these files for learning:
- `season_example/` - Complete working example with 4 missions
- `STUDENT_GUIDE.md` - Complete guide for creating seasons and missions
- `reference_code/misc_examples/motor_example.py` - Basic motor control
- `reference_code/misc_examples/drive_base_example.py` - Robot driving
- `reference_code/misc_examples/tilt_sensor_example.py` - Using the IMU sensor
- `reference_code/menu_example/` - Multi-file program organization

## Units and Measurements Reference

Help students understand these units:
- **Distance**: millimeters (mm) - 1000mm = 1 meter
- **Speed**: mm/s (millimeters per second) or deg/s (degrees per second)
- **Angles**: degrees (°) - 360° = full circle
- **Time**: milliseconds (ms) - 1000ms = 1 second
- **Color**: Named colors (Color.RED) or custom (Color(h=180, s=100, v=100))
- **Brightness**: Percentage 0-100%

## Safety and Best Practices

Remind students:
1. Always have a way to stop the robot (center button)
2. Start with slow speeds when testing
3. Clear the area around the robot before running
4. Check motor/sensor connections before uploading code
5. Save work frequently
6. Test on the floor, not on tables where robot might fall

## Using AI Assistant Tools

When students need help beyond the local reference files, use the Context7 MCP tool to access up-to-date PyBricks documentation:

**Available PyBricks Libraries:**

1. **Pybricks MicroPython API** - `/pybricks/pybricks-api`
   - Official API documentation (247 code snippets, Trust Score: 8)
   - Best for: Specific API methods, parameters, and return values

2. **Pybricks Platform Docs** - `/websites/pybricks_en`
   - Complete platform documentation (394 code snippets, Trust Score: 7.5)
   - Best for: Tutorials, getting started guides, platform features

**How to use it:**
1. Use `mcp__context7__get-library-docs` with the appropriate library ID
2. Specify a topic when students have specific questions (e.g., "motors", "sensors", "display")
3. Provide code examples that match the student's skill level
4. Choose the API library for technical details, or the platform docs for broader guidance

**Example scenarios:**
- Student asks: "How do I use a color sensor?" → Fetch from `/websites/pybricks_en` with topic "color sensor"
- Student asks: "What parameters does motor.run() take?" → Fetch from `/pybricks/pybricks-api` with topic "motor run"
- Student asks: "Can I make the robot follow a line?" → Fetch from `/websites/pybricks_en` with topic "line following"
- Student asks: "How do I play music?" → Fetch from `/pybricks/pybricks-api` with topic "speaker notes"

This ensures you provide accurate, current PyBricks information while maintaining age-appropriate explanations.

## Additional Learning Resources

Point students to:
- [Official PyBricks documentation](https://docs.pybricks.com)
- [PyBricks examples on GitHub](https://github.com/pybricks/pybricks-micropython)
- Python basics tutorials (for general Python concepts)

## Benefits of the Season Management System

### For Students
- ✅ **No configuration errors** - Scripts generate everything correctly
- ✅ **Focus on learning** - Write robot logic, not boilerplate setup
- ✅ **Can't break the menu** - Auto-updated when adding missions
- ✅ **Helpful examples** - Mission template has code they can uncomment/modify
- ✅ **Robot-specific** - Config matched to their exact robot
- ✅ **Team collaboration** - Multiple students can easily add missions

### For Educators/Mentors
- ✅ **Dramatically lower barrier to entry** - 2 minutes vs 15+ minutes of error-prone setup
- ✅ **Consistent structure** - All teams use same organization
- ✅ **Easy to help debug** - Know exactly where to look
- ✅ **Progressive learning** - Template guides without prescribing
- ✅ **Version control friendly** - Clean separation of missions

### What Problems This Solves
**Old way (error-prone):**
- Copy folder → Edit config (miss fields) → Delete examples → Edit menu imports → Edit menu dict → Update hub_menu() → Fix syntax errors → Hope it works

**New way (foolproof):**
- `python new_season.py` (answer 6 questions) → `python ../new_mission.py` (answer 4 questions) → Edit mission → Upload → Works!

## Encouragement Philosophy

When students struggle:
- Emphasize that mistakes are part of learning
- Celebrate when code works, even partially
- Point out what they did right before correcting errors
- Show how even experienced programmers debug and iterate
- Encourage peer learning and collaboration
- Make it fun and connect to their interests
- **Direct them to the automated scripts** - Don't make them fight with setup!

Remember: The goal is to build confidence and curiosity, not just working code!
