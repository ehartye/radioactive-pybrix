# Season Template Example

A comprehensive template for organizing robot missions in a season-based structure with shared utilities and modular design.

## Overview

This template demonstrates a well-organized approach to creating robot seasons with multiple missions. It features:

- **Hierarchical Configuration**: Base season config with per-mission overrides
- **Shared Utilities**: Common robot control, display patterns, and movement functions
- **Modular Missions**: Self-contained missions with `run()` functions for repeatability
- **Menu System**: Interactive mission selection with continuous operation support
- **Example Missions**: Demonstrations of robot driving in shapes and displaying patterns

## Project Structure

```
season_template_example/
├── season_config.py              # Base season configuration
├── shared/                       # Shared logic between missions
│   ├── __init__.py
│   ├── robot_controller.py       # Common robot control functions
│   ├── display_patterns.py       # Shared display pattern utilities
│   └── shape_movements.py        # Common shape driving logic
├── missions/                     # Individual mission modules
│   ├── __init__.py
│   ├── mission_01_square_drive.py    # Drive in square pattern
│   ├── mission_02_circle_drive.py    # Drive in circle pattern
│   ├── mission_03_square_display.py # Display square on screen
│   └── mission_04_triangle_combo.py # Drive triangle + display
├── season_menu.py               # Main menu system for mission selection
└── README.md                    # This documentation
```

## Quick Start

### Running the Season Menu

```python
from season_template_example.season_menu import main

# Start the interactive menu
main()
```

### Running Individual Missions

```python
from season_template_example.missions import mission_01_square_drive

# Run a specific mission
mission_01_square_drive.run()
```

### Running Demo Sequences

```python
from season_template_example.season_menu import run_quick_demo, run_custom_sequence

# Run all missions in sequence
run_quick_demo()

# Run custom mission sequence
run_custom_sequence()
```

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
from shared.robot_controller import RobotController
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
from shared.display_patterns import DisplayPatterns

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
from shared.shape_movements import ShapeMovements

movements = ShapeMovements(robot)
movements.drive_square(side_length=300)
movements.drive_circle(radius=200)
```

## Mission Examples

### Mission 01: Square Drive

Drives the robot in a square pattern with configurable size and speed.

**Features:**
- Precise 90-degree turns
- Configurable side length
- Optional corner pauses
- Progress display
- Custom size function

**Usage:**
```python
from missions.mission_01_square_drive import run, run_with_custom_size

run()  # Default 300mm square
run_with_custom_size(500)  # Custom 500mm square
```

### Mission 02: Circle Drive

Drives the robot in a circle pattern with configurable radius and direction.

**Features:**
- Smooth circular motion
- Configurable radius and direction
- Optional return to start
- Figure-eight pattern support
- Display animation sync

**Usage:**
```python
from missions.mission_02_circle_drive import run, run_with_custom_radius, run_figure_eight

run()  # Default 200mm radius clockwise
run_with_custom_radius(150, clockwise=False)  # Custom counter-clockwise
run_figure_eight()  # Figure-eight pattern
```

### Mission 03: Square Display

Displays animated square patterns on the robot's screen without driving.

**Features:**
- Multi-cycle animations
- Pattern variants
- Custom timing control
- Interactive progress display
- Static pattern showcase

**Usage:**
```python
from missions.mission_03_square_display import run, run_with_custom_timing, run_interactive_display

run()  # Default animation
run_with_custom_timing(200, 10)  # 200ms delay, 10 cycles
run_interactive_display()  # Interactive mode
```

### Mission 04: Triangle Combo

Combines triangle driving with triangle display patterns for synchronized operation.

**Features:**
- Synchronized display with movement
- Multiple execution modes
- Custom triangle sizes
- Multi-triangle sequences
- Return-to-start option

**Usage:**
```python
from missions.mission_04_triangle_combo import run, run_with_custom_size, run_multi_triangle_combo

run()  # Default synchronized combo
run_with_custom_size(400)  # Custom 400mm triangle
run_multi_triangle_combo()  # Multiple triangles
```

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
