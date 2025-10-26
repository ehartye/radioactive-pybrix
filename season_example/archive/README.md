# Alternative Mission Examples

These are variant missions that demonstrate alternative approaches to the main missions. They are not registered in the season menu but can be studied as reference examples or used in your own seasons.

## What's in this Archive?

### mission_01_square_drive.py
Alternative to the main `mission_01_drive_to_target.py` that drives the robot in a square pattern.

**What it demonstrates:**
- Driving in geometric patterns (square)
- Using loops to repeat movements
- Pausing at corners for precision
- Display updates synchronized with movement

**How to use it:**
- Copy to your season folder
- Add to `season_menu.py` to make it selectable
- Or run it directly for testing: `python mission_01_square_drive.py`

### mission_02_circle_drive.py
Alternative to `mission_02_attachment_demo.py` that uses the `curve()` method to drive in circular patterns.

**What it demonstrates:**
- Driving in curves and circles using `robot.drivebase.curve()`
- Creating figure-eight patterns
- Coordinating display animations with circular movement

**How to use it:**
- Copy to your season folder
- Experiment with different radius values
- Try the `run_figure_eight()` function for advanced patterns

### mission_03_square_display.py
Alternative to `mission_03_display_feedback.py` focused on square display patterns and animations.

**What it demonstrates:**
- Creating custom 5x5 LED patterns
- Animating sequences of patterns
- Using display without any robot movement (great for testing!)
- Progress indicators and visual feedback

**How to use it:**
- Great for learning display programming without moving the robot
- Copy patterns to use in your own missions
- Experiment with creating new patterns

### mission_04_triangle_combo.py
Advanced mission that combines triangle driving with synchronized display patterns.

**What it demonstrates:**
- Driving equilateral triangles (120-degree turns)
- Synchronizing display with movement
- Complex mission with multiple helper functions
- Pattern variants and customization

**How to use it:**
- Study for advanced techniques
- See how to organize complex missions with helper functions
- Learn about synchronized vs. parallel animations

## How to Use These Examples

### Option 1: Study as Reference
Read the code to learn different approaches and techniques. These examples show:
- Different ways to create movement patterns
- How to organize complex missions
- Advanced use of display patterns
- Helper function design patterns

### Option 2: Copy to Your Season
If you want to use one of these missions in your season:

1. Copy the mission file to your season folder
2. Edit `season_menu.py` to add the mission:
   ```python
   import mission_01_square_drive  # Add import

   # Add to missions dict:
   "5": {
       "name": "Square Drive",
       "description": "Drive in a square pattern",
       "run_function": mission_01_square_drive
   }

   # Update hub_menu options: hub_menu("1", "2", "3", "4", "5", "Q")
   ```

### Option 3: Run Directly for Testing
All missions support standalone execution:
```bash
python mission_01_square_drive.py
```

## Learning Tips

1. **Start simple**: Begin with `mission_03_square_display.py` since it doesn't move the robot
2. **Compare approaches**: Look at how square drive differs from the main missions
3. **Experiment**: Modify the configurations and see what happens
4. **Mix and match**: Take patterns from one mission and use them in another

## Why These Aren't in the Main Menu

These missions were created as teaching examples and alternatives. The main 4 missions (drive_to_target, attachment_demo, display_feedback, line_following) cover the core FLL patterns. These archived missions show alternative approaches but would be redundant in the default menu.

## Technical Note

All these missions have been updated to use the current API:
- Single parameter signature: `def run(robot):`
- Access display via `robot.display.*`
- Use direct `robot.drivebase.*` commands instead of deprecated shape_movements module

Happy coding! 🤖
