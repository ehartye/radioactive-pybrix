# Season Example - FLL-Realistic Missions

A complete working example season with 4 FLL-realistic missions that demonstrate common robotics competition patterns.

## Overview

This example season demonstrates a well-organized approach to creating robot seasons with multiple missions. It features:

- **Hierarchical Configuration**: Base season config with per-mission overrides
- **Shared Utilities**: Common robot control, display patterns, and line-following functions
- **Modular Missions**: Self-contained missions with `run(robot)` functions
- **Menu System**: Interactive mission selection with continuous operation support
- **FLL-Realistic Missions**: Practical examples of navigation, attachments, feedback, and sensors

## Project Structure

**Important:** PyBricks MicroPython does not support subdirectories for imports. All files must be in a flat structure in the same directory.

```
season_example/
├── season_menu.py                    # ⭐ Main menu - START HERE!
├── season_config.py                  # Base configuration (ports, speeds, etc.)
├── robot_controller.py               # Common robot control functions
├── display_patterns.py               # Shared display pattern utilities
├── line_movements.py                 # Line detection and following functions
├── mission_01_drive_to_target.py     # Mission 1: Navigate to target and return
├── mission_02_attachment_demo.py     # Mission 2: Use attachment motors
├── mission_03_display_feedback.py    # Mission 3: Display/lights/sounds feedback
├── mission_04_line_following.py      # Mission 4: Line detection and squaring
├── archive/                          # Alternative mission examples (not in menu)
│   ├── README.md                     # Documentation for archived missions
│   ├── mission_01_square_drive.py    # Alternative: Drive in square pattern
│   ├── mission_02_circle_drive.py    # Alternative: Drive in circles
│   ├── mission_03_square_display.py  # Alternative: Display patterns
│   └── mission_04_triangle_combo.py  # Alternative: Triangle driving + display
├── QUICKSTART.md                     # 5-minute getting started guide
├── INSTRUCTIONS.md                   # How to add new missions
└── README.md                         # This documentation
```

**⚠️ All main files (not archive/) must be uploaded together to your SPIKE Prime hub.**

## Quick Start

**New to this template?** Read [QUICKSTART.md](QUICKSTART.md) for a 5-minute walkthrough!

### Running the Season Menu

1. Upload ALL `.py` files to your SPIKE Prime hub
2. Run `season_menu.py` on your hub
3. Use LEFT/RIGHT buttons to select a mission
4. Press CENTER button to run it

### Running Individual Missions

You can also test missions individually during development:

```python
# In season_menu.py or directly on hub
import mission_01_drive_to_target

# Run a specific mission
mission_01_drive_to_target.run()
```

**Note:** Individual mission execution requires you to initialize the robot yourself. The season menu handles this automatically.

## Configuration System

### Base Season Configuration

The `season_config.py` file contains:

- **Hardware Configuration**: Robot ports, directions, and specifications
- **Season Defaults**: Default settings for all missions
- **Season Information**: Metadata about the season

### Mission-Specific Overrides

Each mission can override base settings:

```python
# Mission-specific configuration overrides
MISSION_CONFIG = {
    "drive_speed": 150,        # Override default speed
    "turn_rate": 45,           # Override default turn rate
    "square_size": 300,        # Mission-specific parameter
    "show_progress": True,     # Mission-specific feature
}
```

## Shared Utilities

### Robot Controller

The `RobotController` class provides:

- Centralized robot initialization
- Configuration merging (base + mission overrides)
- Common robot operations (reset, measurements, signals)
- Automatic cleanup and error handling

```python
from robot_controller import RobotController
from season_config import SeasonDefaults

robot = RobotController(SeasonDefaults, MISSION_CONFIG)
robot.initialize()
# Use robot...
robot.cleanup()
```

### Display Patterns

The `DisplayPatterns` class offers:

- Animated shape patterns (square, circle, triangle)
- Progress indicators and countdowns
- Success/error feedback displays
- Custom pattern support

```python
from display_patterns import DisplayPatterns

display = DisplayPatterns(robot.hub)
display.animate_square(cycles=3)
display.show_completion_checkmark()
```

### Shape Movements

The `ShapeMovements` class provides:

- Geometric movement functions (square, circle, triangle)
- Advanced patterns (figure-eight, zigzag, spiral)
- Configurable parameters (size, speed, pauses)
- Return-to-start functionality

```python
from shape_movements import ShapeMovements

movements = ShapeMovements(robot)
movements.drive_square(side_length=300)
movements.drive_circle(radius=200)
```

## Main Missions (In Menu)

These are the 4 FLL-realistic missions registered in `season_menu.py`:

### Mission 01: Drive to Target

Navigate to a precise position and return home - demonstrates the basic FLL pattern.

**What it teaches:**
- Precise straight-line driving with specific distances
- Accurate angle turns for navigation
- Multi-step mission structure (drive → align → approach → return)
- Using display for visual feedback

**FLL Application:** Driving to mission models, approaching targets, returning to base

### Mission 02: Attachment Demo

Use attachment motors for mechanisms like claws, lifts, and spinners.

**What it teaches:**
- Running attachment motors at specific speeds
- Moving to specific angles
- Running until stalled (detecting resistance)
- Combining attachment actions with driving

**FLL Application:** Lifting mission models, operating mechanisms, releasing objects

### Mission 03: Display Feedback

Mission feedback using display, lights, and sounds - no robot movement (great for testing!).

**What it teaches:**
- Showing countdowns and checkmarks
- Using hub lights for status indication
- Playing beeps and tones
- Creating custom display patterns
- Progress bars and animations

**FLL Application:** Visual confirmation of mission steps, debugging without moving robot

### Mission 04: Line Following

Use color sensors for precision positioning with line detection.

**What it teaches:**
- Reading color sensor reflection values
- Detecting black lines
- "Squaring" on a line for precise positioning
- Combining sensors with navigation

**FLL Application:** Precise positioning on competition mat, line following, edge detection

## Alternative Mission Examples (Archived)

The `archive/` folder contains 4 alternative mission examples that demonstrate different patterns:
- **Square Drive** - Geometric patterns with loops
- **Circle Drive** - Using curve() for circular motion
- **Square Display** - Custom LED patterns and animations
- **Triangle Combo** - Synchronized movement and display

See `archive/README.md` for details on these teaching examples.

## Menu System

### Interactive Menu

The season menu provides:

- Mission selection interface
- Mission descriptions
- Success/error feedback
- Continuous operation support
- Emergency error handling

### Custom Sequences

Create custom mission sequences:

```python
def run_my_sequence():
    missions = [
        mission_03_square_display.run,
        mission_01_square_drive.run,
        mission_02_circle_drive.run,
    ]
    
    for mission in missions:
        try:
            mission()
        except Exception as e:
            print(f"Mission failed: {e}")
            # Handle error or continue
```

## Development Guidelines

### Adding New Missions

1. Create new mission file in `missions/` directory
2. Implement `run()` function with proper error handling
3. Use `RobotController` for robot management
4. Add mission to `missions/__init__.py`
5. Update `season_menu.py` with new mission entry

### Mission Template

```python
"""
Mission XX: Description
Brief description of what the mission does
"""

from ..shared.robot_controller import RobotController
from ..shared.display_patterns import DisplayPatterns
from ..shared.shape_movements import ShapeMovements
from ..season_config import SeasonDefaults

# Mission-specific configuration
MISSION_CONFIG = {
    "param1": value1,
    "param2": value2,
}

def run():
    """Main mission execution function"""
    print("=== Mission XX: Description ===")
    
    robot = RobotController(SeasonDefaults, MISSION_CONFIG)
    
    try:
        robot.initialize()
        
        # Initialize utilities
        display = DisplayPatterns(robot.hub)
        movements = ShapeMovements(robot)
        
        robot.mission_start_signal()
        
        # Mission logic here
        
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

### Best Practices

1. **Error Handling**: Always use try/except blocks with proper cleanup
2. **Configuration**: Use mission-specific config overrides
3. **Logging**: Include informative print statements
4. **Modularity**: Keep missions self-contained
5. **Testing**: Allow direct execution for development
6. **Documentation**: Document mission parameters and behavior

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all modules are in the correct directory structure
2. **Robot Initialization**: Check hardware connections and port assignments
3. **Mission Failures**: Review configuration parameters and robot setup
4. **Display Issues**: Verify hub display functionality

### Debugging Tips

1. Run individual missions directly for testing
2. Use print statements for debugging mission flow
3. Check robot measurements after movements
4. Verify configuration overrides are applied correctly

## Extension Ideas

### Additional Missions

- **Mission 05**: Sensor-based navigation
- **Mission 06**: Color detection and sorting
- **Mission 07**: Line following
- **Mission 08**: Obstacle avoidance

### Advanced Features

- **Mission Timing**: Add timing constraints and optimization
- **Mission Scoring**: Implement scoring system for competitions
- **Mission Logging**: Add detailed logging and analytics
- **Mission Validation**: Pre-flight checks and validation

### Integration Examples

- **Tournament Mode**: Automated mission sequences for competitions
- **Training Mode**: Guided mission execution with hints
- **Demo Mode**: Presentation-ready mission showcase
- **Remote Control**: Integration with external control systems

This template provides a solid foundation for organizing complex robot seasons while maintaining clean, modular, and extensible code architecture.
