# Miscellaneous Code Examples

This folder contains **advanced examples** that demonstrate concepts beyond basic FLL missions. These are for learning and exploration, not required for competition programming.

## What's in Here

### shape_movements_example.py
**Purpose**: Demonstrates how to create a custom movement library that extends robot capabilities.

**Concepts Shown**:
- Creating a class that wraps RobotController
- Implementing complex movements (circles, polygons, figure-eights)
- Using math to calculate arc movements
- Building reusable movement functions

**When to Use**:
- ❌ **NOT** for typical FLL missions (too complex, not precise enough)
- ✅ For learning about code organization and extensibility
- ✅ For demonstration/exhibition runs
- ✅ As inspiration for creating your own utility libraries

**FLL Reality Check**:
Real FLL missions need **precise** movements to specific positions:
```python
# Real FLL mission pattern:
robot.drivebase.straight(427)  # Exact distance to target
robot.drivebase.turn(-23)      # Precise angle alignment
robot.left_attachment.run_angle(500, 180)  # Deploy mechanism
```

NOT geometric shapes:
```python
# ShapeMovements (fun demo, not practical):
movements.drive_square(side_length=300)
movements.drive_circle(radius=200)
```

**How to Use**:
1. Copy `shape_movements_example.py` to your season folder if you want to experiment
2. Import it in your mission: `from shape_movements_example import ShapeMovements`
3. Create instance: `movements = ShapeMovements(robot)`
4. Call methods: `movements.drive_square(300)`

---

### Other Examples in This Folder

**motor_example.py**
- Basic motor control
- Running motors at different speeds
- Measuring motor angles and speed

**drive_base_example.py**
- Creating and using DriveBase
- Straight driving and turning
- Using settings for speed control

**tilt_sensor_example.py**
- Reading IMU/gyro data
- Detecting tilt angles
- Checking which side is up

**gyro_drive_example.py**
- Using gyro for accurate turns
- Heading control
- Drift correction

**multi_motor_example.py**
- Controlling multiple motors
- Coordinated movements
- Parallel operations

---

## When to Use These Examples

✅ **Use these when**:
- Learning new PyBricks concepts
- Understanding how something works
- Experimenting with ideas
- Building your own utility libraries

❌ **Don't use these as**:
- Templates for FLL missions (too complicated)
- Required code to copy (they're optional)
- The "right way" to do things (direct commands are often better)

## Better Starting Points

For practical FLL mission code, look at:
- **`season_example/`** folder - Realistic FLL-style missions
- **`season_template/_template_mission.py`** - Mission template with helpful examples
- **`STUDENT_GUIDE.md`** - Step-by-step guide for creating missions

---

## Learning Progression

1. **Start Here**: `season_example/` - Learn from working FLL-style missions
2. **Then Try**: These misc examples - Explore advanced concepts
3. **Finally**: Create your own utilities based on what you learned!

Remember: The best code is code that **works reliably** and is **easy to understand**. Simple is better than complex for competition robotics!
