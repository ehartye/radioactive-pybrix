# How to Add a New Mission

This guide will walk you through the process of adding a new mission to the season project. We will create a new mission called "Zigzag Drive" as an example.

## Important: Flat File Structure

**PyBricks MicroPython does not support subdirectories for imports.** All mission files must be in the same directory as `season_menu.py` and the other files.

## Step 1: Create the New Mission File

Create a new Python file in the `season_template_example/` directory (the same folder as all the other files).

1. Navigate to the `season_template_example/` directory
2. Create a new file named `mission_05_zigzag_drive.py`

Your file structure should now look like this:

```
season_template_example/
├── season_menu.py
├── season_config.py
├── robot_controller.py
├── display_patterns.py
├── shape_movements.py
├── mission_01_square_drive.py
├── mission_02_circle_drive.py
├── mission_03_square_display.py
├── mission_04_triangle_combo.py
└── mission_05_zigzag_drive.py  <-- NEW FILE
```

## Step 2: Write the Mission Code

Open your new `mission_05_zigzag_drive.py` file and add the following code. This code is based on the mission template and defines a simple mission that drives the robot in a zigzag pattern.

```python
"""
Mission 05: Zigzag Drive
Drives the robot in a zigzag pattern.
"""

from robot_controller import RobotController
from display_patterns import DisplayPatterns
from shape_movements import ShapeMovements
from season_config import SeasonDefaults

# Mission-specific configuration
MISSION_CONFIG = {
    "drive_speed": 200,
    "turn_rate": 75,
    "segment_length": 150,
    "segments": 4,
}

def drive_zigzag(movements, config):
    """Drives the robot in a zigzag pattern."""
    for i in range(config["segments"]):
        # Drive forward
        movements.drivebase.straight(config["segment_length"])
        # Turn right or left alternating
        if i % 2 == 0:
            movements.drivebase.turn(90)  # Turn right
        else:
            movements.drivebase.turn(-90)  # Turn left

def run():
    """Main mission execution function"""
    print("=== Mission 05: Zigzag Drive ===")

    robot = RobotController(SeasonDefaults, MISSION_CONFIG)

    try:
        robot.initialize()

        # Initialize utilities
        display = DisplayPatterns(robot.hub)
        movements = ShapeMovements(robot)

        robot.mission_start_signal()

        # --- Mission Logic ---
        display.animate_triangle(cycles=2)
        drive_zigzag(movements, robot.config)
        # ---------------------

        robot.mission_success_signal()
        print("Mission 05 completed successfully!")

    except Exception as e:
        print(f"Mission 05 failed: {e}")
        robot.mission_error_signal()
        raise e

    finally:
        robot.cleanup()

# Allow direct execution for testing
if __name__ == "__main__":
    run()
```

## Step 3: Add the Mission to the Menu

Now let's add the new mission to the interactive menu so you can select and run it.

1. Open `season_menu.py`

2. First, import the new mission at the top of the file with the other mission imports:

```python
# Import all mission modules (flat structure for PyBricks compatibility)
import mission_01_square_drive
import mission_02_circle_drive
import mission_03_square_display
import mission_04_triangle_combo
import mission_05_zigzag_drive  # <-- ADD THIS
from season_config import SeasonInfo, SeasonDefaults
```

3. Next, add a new entry to the `self.missions` dictionary inside the `__init__` method of the `SeasonMenu` class:

```python
            "4": {
                "name": "Triangle Combo",
                "description": "Drive triangle while displaying pattern",
                "run_function": mission_04_triangle_combo
            },
            "5": {
                "name": "Zigzag Drive",
                "description": "Drive robot in a zigzag pattern",
                "run_function": mission_05_zigzag_drive
            }  # <-- ADD THIS
```

4. Update the `hub_menu` call in the `main_loop` method to include the new option "5":

```python
            # Get user selection
            print("\nSelect mission (1-5) or Q to quit:")
            selected = hub_menu("1", "2", "3", "4", "5", "Q")  # <-- ADD "5"
```

## Step 4: Upload and Test

1. Upload ALL `.py` files to your hub (including the new `mission_05_zigzag_drive.py`)
2. Run `season_menu.py`
3. Use LEFT/RIGHT buttons to select mission 5
4. Press CENTER button to run it

## You're Done!

That's it! You have successfully added a new mission to the project. You can now run the `season_menu.py` file, and you will see "Zigzag Drive" as option 5 in the menu.

## Mission Template

Here's a blank template you can copy for new missions:

```python
"""
Mission XX: Your Mission Name
Brief description of what the mission does
"""

from robot_controller import RobotController
from display_patterns import DisplayPatterns
from shape_movements import ShapeMovements
from season_config import SeasonDefaults

# Mission-specific configuration
MISSION_CONFIG = {
    "drive_speed": 150,
    "turn_rate": 45,
    # Add your custom parameters here
}

def run():
    """Main mission execution function"""
    print("=== Mission XX: Your Mission Name ===")

    robot = RobotController(SeasonDefaults, MISSION_CONFIG)

    try:
        robot.initialize()

        # Initialize utilities
        display = DisplayPatterns(robot.hub)
        movements = ShapeMovements(robot)

        robot.mission_start_signal()

        # --- YOUR MISSION LOGIC HERE ---
        # Example: movements.drive_square(side_length=300)
        # Example: display.animate_circle(cycles=3)
        # --------------------------------

        robot.mission_success_signal()
        print("Mission XX completed successfully!")

    except Exception as e:
        print(f"Mission XX failed: {e}")
        robot.mission_error_signal()
        raise e

    finally:
        robot.cleanup()

# Allow direct execution for testing
if __name__ == "__main__":
    run()
```

## Tips

- **Test missions individually first** - Run them directly before adding to the menu
- **Start simple** - Get basic movements working before adding complex logic
- **Use print statements** - They help you debug what's happening
- **Copy from examples** - Look at the existing missions for patterns
- **Experiment!** - Try different speeds, distances, and patterns

## Common Mistakes to Avoid

1. **Wrong imports** - Remember to use flat imports (no `from missions.` or `from shared.`)
2. **Forgetting to upload** - All files must be uploaded to the hub
3. **Not calling `.run()`** - The menu expects a `run()` function in each mission
4. **Skipping initialization** - Always call `robot.initialize()` before using the robot
5. **Not cleaning up** - Always call `robot.cleanup()` in the `finally` block

Happy mission building! 🤖
