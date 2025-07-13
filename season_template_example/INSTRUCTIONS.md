# How to Add a New Mission

This guide will walk you through the process of adding a new mission to the season project. We will create a new mission called "Zigzag Drive" as an example.

## Step 1: Create the New Mission File

First, you need to create a new Python file for your mission inside the `missions/` directory.

1.  Navigate to the `season_template_example/missions/` directory.
2.  Create a new file named `mission_05_zigzag_drive.py`.

Your file structure should now look like this:

```
missions/
├── __init__.py
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

from ..shared.robot_controller import RobotController
from ..shared.display_patterns import DisplayPatterns
from ..shared.shape_movements import ShapeMovements
from ..season_config import SeasonDefaults

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
        movements.drive_straight(config["segment_length"])
        # Turn right or left
        if i % 2 == 0:
            movements.turn_right(90)
        else:
            movements.turn_left(90)

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

## Step 3: Register the New Mission

Now, you need to make the mission available to the rest of the program. Open the `missions/__init__.py` file and add a line to import your new mission's `run` function.

1.  Open `season_template_example/missions/__init__.py`.
2.  Add the following line to the end of the import statements:

```python
from missions.mission_05_zigzag_drive import run as mission_05_zigzag_drive
```

3.  Also, add the new mission to the `__all__` list:

```python
__all__ = [
    'mission_01_square_drive',
    'mission_02_circle_drive', 
    'mission_03_square_display',
    'mission_04_triangle_combo',
    'mission_05_zigzag_drive'  # <-- ADD THIS
]
```

## Step 4: Add the Mission to the Menu

Finally, let's add the new mission to the interactive menu so you can select and run it.

1.  Open `season_template_example/season_menu.py`.
2.  First, import the new mission at the top of the file with the other mission imports:

```python
from missions import mission_04_triangle_combo
from missions import mission_05_zigzag_drive  # <-- ADD THIS
from season_config import SeasonInfo, SeasonDefaults
```

3.  Next, add a new entry to the `self.missions` dictionary inside the `__init__` method of the `SeasonMenu` class:

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
            } # <-- ADD THIS
```

4.  Update the `hub_menu` call in the `main_loop` method to include the new option "5":

```python
            # Get user selection
            print("\nSelect mission (1-5) or Q to quit:")
            selected = hub_menu("1", "2", "3", "4", "5", "Q") # <-- ADD "5"
```

## You're Done!

That's it! You have successfully added a new mission to the project. You can now run the `season_menu.py` file, and you will see "Zigzag Drive" as option 5 in the menu.
