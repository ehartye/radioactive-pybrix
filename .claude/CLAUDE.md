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

### Season Management Tools (Root Level)
- **`new_season.py`**: Interactive script to create a new season folder with robot-specific configuration
- **`new_mission.py`**: Interactive script to add missions to a season (auto-updates menu)
- **`STUDENT_GUIDE.md`**: Complete walkthrough for students to create seasons and missions

### Season Template (`season_template/`)
Template files used by the scripts (students don't edit these directly):
- **`_template_mission.py`**: Mission template with helpful code examples in comments
- **`season_config.py.template`**: Robot configuration template with placeholders
- **`season_menu.py.template`**: Menu system template with placeholders
- **Shared utilities**: `robot_controller.py`, `display_patterns.py`, `shape_movements.py`

### Working Example (`season_example/`)
Complete working example with 4 missions students can learn from:
- **`mission_01_square_drive.py`**: Drive robot in square pattern
- **`mission_02_circle_drive.py`**: Drive robot in circle pattern
- **`mission_03_square_display.py`**: Display patterns (no motors needed - good for testing!)
- **`mission_04_triangle_combo.py`**: Combined driving and display
- **`season_menu.py`**: Mission selector menu
- **`season_config.py`**: Robot-specific configuration

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

## Key PyBricks Concepts to Teach

### 1. Hub Initialization
```python
from pybricks.hubs import PrimeHub
hub = PrimeHub()
```
Always the first step - creates connection to the robot brain.

### 2. Motors
```python
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction

motor = Motor(Port.A)  # Connect to port A
motor.run(500)  # Run at 500 degrees per second
motor.run_angle(500, 360)  # Turn 360 degrees at 500 deg/s
motor.stop()  # Stop and coast freely
```

**Key Teaching Points:**
- Ports: Where motors plug in (A, B, C, D, E, F)
- Speed: Measured in degrees per second
- Angles: 360 degrees = one full rotation
- Direction: Can be reversed when initializing

### 3. Drive Bases (Two-Wheeled Robots)
```python
from pybricks.robotics import DriveBase

left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)

robot.straight(200)  # Drive forward 200mm
robot.turn(90)  # Turn right 90 degrees
robot.drive(100, 0)  # Drive forward at 100 mm/s, no turning
```

**Key Teaching Points:**
- Wheel diameter and axle track need measuring
- Positive values = forward/right, negative = backward/left
- `drive()` keeps going until stopped, `straight()` goes a set distance

### 4. Hub Display
```python
hub.display.number(42)  # Show number
hub.display.text("Hi")  # Show scrolling text
hub.display.icon(Icon.HEART)  # Show built-in icon
hub.display.pixel(2, 2)  # Turn on pixel at row 2, column 2
hub.display.off()  # Clear display
```

### 5. Hub Buttons
```python
from pybricks.parameters import Button

pressed = hub.buttons.pressed()
if Button.LEFT in pressed:
    # Left button was pressed
if Button.CENTER in pressed:
    # Center button was pressed
```

### 6. Tilt/IMU Sensor
```python
pitch, roll = hub.imu.tilt()  # Get tilt angles
up_side = hub.imu.up()  # Which side faces up
heading = hub.imu.heading()  # Compass heading
```

### 7. Hub Light
```python
from pybricks.parameters import Color

hub.light.on(Color.RED)  # Turn on red
hub.light.off()  # Turn off
hub.light.blink(Color.GREEN, [500, 500])  # Blink pattern
```

### 8. Speaker/Sounds
```python
hub.speaker.beep()  # Simple beep
hub.speaker.beep(frequency=800, duration=200)  # Custom beep
```

### 9. Waiting
```python
from pybricks.tools import wait

wait(1000)  # Wait 1000 milliseconds (1 second)
```

## Common Student Challenges

### Challenge 1: "My robot drives backwards!"
**Solution**: Change motor direction when initializing
```python
left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
```

### Challenge 2: "The display is upside down!"
**Solution**: Set display orientation
```python
hub.display.orientation(up=Side.RIGHT)
# Or use auto-orientation
hub.display.orientation(hub.imu.up())
```

### Challenge 3: "My motors are too slow/fast!"
**Solution**: Adjust control limits
```python
motor.control.limits(speed=1000, acceleration=2000, torque=500)
```

### Challenge 4: "The robot doesn't turn the right amount!"
**Solution**: Calibrate wheel diameter and axle track measurements
- Measure wheel diameter with ruler
- Measure axle track (distance between wheel contact points)
- Test and adjust values

### Challenge 5: "I don't know what went wrong!"
**Solution**: Use print statements for debugging
```python
print("Motor angle:", motor.angle())
print("Speed:", motor.speed())
```

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
   - Upload ALL `.py` files to SPIKE Prime hub (must be together!)
   - Run `season_menu.py`
   - Use hub buttons to select and run missions

### For AI Assistants Helping Students

**If a student asks about creating a season or mission:**
1. Direct them to use `new_season.py` or `new_mission.py` scripts
2. Explain they answer simple questions and everything is generated
3. Show them `STUDENT_GUIDE.md` for complete walkthrough
4. Do NOT tell them to manually copy/edit template files

**If a student asks about mission code:**
1. The mission template (`_template_mission.py`) has tons of helpful examples
2. Guide them to uncomment and modify existing examples
3. Remind them about flat imports (no subdirectories)
4. All files must be uploaded together to hub

**If helping debug:**
1. Check they uploaded ALL `.py` files (common mistake)
2. Check imports are flat (no `from missions.` or `from shared.`)
3. Check ports in `season_config.py` match physical robot
4. Check wheel measurements in `season_config.py` are accurate

### Example Mission Template Structure

Every generated mission includes helpful guidance:
```python
# TODO: ADD YOUR MISSION LOGIC HERE

# --- DRIVING EXAMPLES ---
# Drive straight forward 300mm:
#   movements.drivebase.straight(300)
#
# Turn right 90 degrees:
#   movements.drivebase.turn(90)
#
# Drive in a square:
#   movements.drive_square(side_length=300)

# --- DISPLAY EXAMPLES ---
# Show a number:
#   robot.hub.display.number(5)
#
# Show countdown:
#   display.show_countdown(3)

# --- ATTACHMENTS (if you have them) ---
# Run attachment motor:
#   if robot.left_attachment:
#       robot.left_attachment.run(500)
```

Students just uncomment what they need and modify values!

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
