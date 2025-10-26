# Student Guide: Creating Your Robot Season

Welcome! This guide will help you create and organize your SPIKE Prime robot programs for the season.

## 🎓 New to Python and PyBricks? Start Here!

**Before following this guide, take our interactive training quiz:**

```bash
python training/launch_training.py
```

This fun quiz teaches you everything you need to know before you start:
- What Python is and why we use it
- What PyBricks is and how it controls robots
- How our project tools work
- Key programming concepts

**After the quiz, come back here to create your first season!**

## Overview

This repository provides tools to help you:
1. **Create a new season** with your robot's specific configuration
2. **Add missions** quickly without copy-pasting or editing menus manually
3. **Organize your code** so everything stays clean and easy to find

## Quick Start (5 Minutes)

### Step 1: Create Your Season (2 minutes)

Run the season creator and answer a few simple questions:

```bash
python new_season.py
```

You'll be asked:
- Season name (e.g., "Fall 2024 Competition")
- Team name
- Where your motors are plugged in (ports)
- Your robot's measurements (wheel diameter, distance between wheels)

**That's it!** The script creates a folder with everything configured for your robot.

### Step 2: Create Your First Mission (2 minutes)

Go into your new season folder and create a mission:

```bash
cd fall_2024_competition  # Or whatever you named your season
python ../new_mission.py
```

You'll be asked:
- Mission name (e.g., "Drive to Target")
- Short description
- Speed settings
- **Template style**: Simple (minimal) or Guided (full examples) - **choose Guided if you're new!**

**Done!** The script creates a mission file and updates your menu automatically.

#### Template Styles

You'll choose one of two template styles:

1. **Simple Template** (for experienced students)
   - Minimal comments
   - Quick-start examples at the top
   - Best when you know what you're doing

2. **Guided Template** (recommended for beginners)
   - Quick-start examples PLUS detailed examples
   - Organized by category (driving, attachments, sensors, etc.)
   - Helpful when learning or exploring new features

**Tip**: Start with Guided, then switch to Simple once you're comfortable!

### Step 3: Add Your Code (5-10 minutes)

1. Open the new mission file (e.g., `mission_01_drive_to_target.py`)
2. Look for the section that says `TODO: ADD YOUR MISSION LOGIC HERE`
3. Read the helpful examples in the comments
4. Add your robot movements!

Example:
```python
# Drive forward 500mm
robot.drivebase.straight(500)

# Turn right 90 degrees
robot.drivebase.turn(90)

# Drive forward another 300mm
robot.drivebase.straight(300)
```

### Step 4: Test on Your Robot (2 minutes)

1. Connect your SPIKE Prime hub
2. Upload **ALL** `.py` files from your season folder to the hub
3. Run `season_menu.py` on your hub
4. Use LEFT/RIGHT buttons to select your mission
5. Press CENTER button to run it!

## The Easy Workflow

```
┌─────────────────────────────────────┐
│  1. Run: python new_season.py       │  ← Do this ONCE per season
│     Answer questions about robot    │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  2. cd your_season_folder           │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  3. Run: python ../new_mission.py   │  ← Do this for EACH mission
│     Answer questions about mission  │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  4. Edit mission_XX_name.py         │
│     Add your robot code             │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  5. Upload to hub & test!           │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  Repeat steps 3-5 for each mission  │
└─────────────────────────────────────┘
```

## What You Get

After running `new_season.py`, your folder will contain:

```
your_season/
├── season_config.py          # Your robot's settings (auto-generated!)
├── season_menu.py            # Mission selector (auto-updated!)
├── robot_controller.py       # Helper code (don't edit)
├── display_patterns.py       # Helper code (don't edit)
├── line_movements.py         # Line following helper (optional, don't edit)
└── README.md                 # Info about your season
```

After running `new_mission.py`, you'll also have:

```
your_season/
├── mission_01_your_name.py   # Your mission code
├── mission_02_another.py     # Another mission
└── ...                       # More missions as you add them
```

## Example: Creating a Season

Let's walk through creating a season for a competition:

```bash
$ python new_season.py
```

```
🤖 SPIKE Prime Season Creator
==============================

Let's set up your new season!

📋 SEASON INFORMATION
Season name: Fall Competition
Team name: RoboWarriors
Short description [Fall Competition missions]: Our awesome competition runs

  📁 Season folder will be: fall_competition/

📍 ROBOT HARDWARE SETUP
  Where are your motors plugged in?
  Left wheel motor port (A/B/C/D/E/F) [C]: C
  Right wheel motor port (A/B/C/D/E/F) [D]: D

🔄 MOTOR DIRECTIONS
  We'll start with standard directions.
  If your robot drives backward, you can change this in season_config.py

🔧 OPTIONAL ATTACHMENTS
  Does your robot have attachment motors? (y/n) [n]: n

  Does your robot have color sensors? (y/n) [n]: n

📏 ROBOT MEASUREMENTS
  Measure your robot to get accurate movements
  Wheel diameter in mm [56]: 56
  Distance between wheels (axle track) in mm [80]: 95

==================================================
Creating your season...
==================================================
✅ Created folder: fall_competition/
✅ Copied shared utilities
✅ Generated season_config.py with your robot specs
✅ Created season_menu.py (empty, ready for missions)
✅ Created README.md

==================================================
🎉 Your season is ready!
==================================================

📍 Next steps:
  1. cd fall_competition
  2. python ../new_mission.py
  3. Edit your mission file to add robot movements
  4. Upload all .py files to your SPIKE Prime hub
  5. Run season_menu.py
```

## Example: Adding a Mission

```bash
$ cd fall_competition
$ python ../new_mission.py
```

```
🎯 SPIKE Prime Mission Creator
==================================================

Let's create a new mission!

📋 MISSION DETAILS
Mission name (e.g., 'Drive to Target'): Navigate Obstacle
Short description [Navigate Obstacle]: Drive around obstacle to target

  📝 This will be Mission #1

⚙️  MISSION CONFIGURATION
Drive speed (mm/s) [200]: 150
Turn rate (degrees/s) [60]: 45

==================================================
Creating mission...
==================================================
✅ Created: mission_01_navigate_obstacle.py
✅ Updated: season_menu.py (added as option 1)

==================================================
🎉 Mission ready to code!
==================================================

📍 Next steps:
  1. Edit mission_01_navigate_obstacle.py
  2. Add your robot logic in the run() function
  3. Upload all .py files to your hub
  4. Run season_menu.py and select mission 1

💡 Tip: Look at the helpful code examples in the file!
```

## Helpful Code Examples

Your mission files come with lots of helpful examples in the comments. Here are some common things you'll want to do:

### Basic Driving (Most Common)
```python
# Drive forward 300mm
robot.drivebase.straight(300)

# Drive backward 200mm (use negative)
robot.drivebase.straight(-200)

# Turn right 90 degrees
robot.drivebase.turn(90)

# Turn left 90 degrees (use negative)
robot.drivebase.turn(-90)
```

### Complete FLL Mission Pattern
Most FLL missions follow this pattern:
```python
# Navigate to target
robot.drivebase.straight(450)    # Drive to position
robot.drivebase.turn(-23)        # Align with target

# Complete task (example: deploy attachment)
if robot.left_attachment:
    robot.left_attachment.run_angle(500, 180)  # Deploy mechanism
    wait(500)
    robot.left_attachment.run_angle(500, -180)  # Retract

# Return home
robot.drivebase.turn(23)          # Turn back
robot.drivebase.straight(-450)    # Return to start
```

### Line Following (Precision Positioning)
For precise alignment on the mat:
```python
from line_movements import LineMovements
line_moves = LineMovements(robot)

# Drive until squared on black line
robot.drivebase.straight(200)     # Approach line
line_moves.square_on_line()       # Square on line (both sensors detect black)
robot.drivebase.straight(150)     # Continue with precise positioning
```

### Display
```python
# Show a number
robot.hub.display.number(5)

# Show text
robot.hub.display.text("GO!")

# Show countdown
display.show_countdown(3)

# Show checkmark when done
display.show_completion_checkmark()
```

### Waiting
```python
from pybricks.tools import wait

# Wait 2 seconds (2000 milliseconds)
wait(2000)
```

## Troubleshooting

### "Robot drives backward instead of forward!"
Open your `season_config.py` and change the motor directions:
```python
class Directions:
    LEFT_WHEEL = Direction.CLOCKWISE  # Try changing these
    RIGHT_WHEEL = Direction.COUNTERCLOCKWISE
```

### "Robot doesn't turn the right amount!"
Measure your robot more carefully and update `season_config.py`:
```python
class Specifications:
    WHEEL_DIAMETER = 56  # Measure your wheel
    AXLE_TRACK = 95      # Measure distance between wheels
```

### "Import errors when I run on the hub"
Make sure you uploaded **ALL** `.py` files, not just your mission file.

### "I want to see a working example"
Check the `season_example/` folder - it has 4 complete example missions you can learn from!

## Tips for Success

1. **Test missions individually first** - Run them directly before adding to the menu
2. **Start simple** - Get basic movements working before adding complex logic
3. **Use print statements** - They help you debug: `print("At checkpoint 1")`
4. **Measure carefully** - Accurate wheel diameter and axle track = accurate movements
5. **Ask for help** - Your teammates and mentors are here to help!

## Advanced: Editing Config Manually

If you need to change settings later, you can edit `season_config.py` directly:

```python
class SeasonDefaults:
    DRIVE_SPEED = 150      # Make robot slower/faster
    TURN_RATE = 45         # Make turns slower/faster
    # ... other settings
```

Each mission can also override these settings in its `MISSION_CONFIG`.

## Need More Help?

- Look at the `season_example/` folder for working examples
- Read the comments in your mission files - they have lots of examples!
- Ask your mentor or teammates
- Check the PyBricks documentation: https://docs.pybricks.com

## Summary

**To create a new season:**
```bash
python new_season.py
```

**To add a mission:**
```bash
cd your_season
python ../new_mission.py
```

**To test:**
1. Edit mission file
2. Upload all .py files to hub
3. Run season_menu.py

That's it! Happy coding! 🤖
