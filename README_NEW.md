# SPIKE Prime Python Learning Repository

A comprehensive learning environment for middle school students working with **LEGO SPIKE Prime** using PyBricks (Python programming).

## 🚀 Quick Start for Students

**Want to create your own robot season? It's super easy!**

```bash
# 1. Create a new season (answer a few questions)
python new_season.py

# 2. Go into your season folder
cd your_season_name

# 3. Add your first mission
python ../new_mission.py

# 4. Edit the mission file and add your code!
```

**That's it!** The scripts handle all the configuration and setup for you.

📖 **Read the [Student Guide](STUDENT_GUIDE.md) for a complete walkthrough!**

## 📁 Repository Structure

```
spike-python-explore/
├── new_season.py           ⭐ Run this to create a new season
├── new_mission.py          ⭐ Run this (from season folder) to add missions
├── STUDENT_GUIDE.md        📖 Complete guide for students
│
├── season_template/        📦 Template files (used by scripts)
│   ├── _template_mission.py
│   ├── season_config.py.template
│   ├── season_menu.py.template
│   └── ... (shared utilities)
│
├── season_example/         📚 Working example with 4 complete missions
│   ├── season_menu.py
│   ├── season_config.py
│   ├── mission_01_square_drive.py
│   ├── mission_02_circle_drive.py
│   ├── mission_03_square_display.py
│   └── mission_04_triangle_combo.py
│
└── reference_docs/         📄 PyBricks documentation excerpts
    └── reference_code/     💻 Additional code examples
```

## 🎯 What Can Students Do?

### 1. Create Custom Seasons
The `new_season.py` script creates a folder configured for your specific robot:
- Your robot's port configuration
- Your wheel measurements
- Your team info
- Empty menu ready for missions

### 2. Add Missions Easily
The `new_mission.py` script:
- Creates a new mission file
- Updates the menu automatically
- Includes helpful code examples in comments
- Assigns the next mission number automatically

### 3. Learn by Example
The `season_example/` folder has 4 complete missions:
- **Mission 1:** Drive in a square
- **Mission 2:** Drive in a circle
- **Mission 3:** Display patterns (no motors needed!)
- **Mission 4:** Drive triangle + display together

## 🛠️ For Educators & Mentors

### Why This Approach?

**Problems with manual setup:**
- ❌ Students copy-paste templates and miss configuration
- ❌ Editing menus manually causes syntax errors
- ❌ Port configurations get mixed up
- ❌ Students waste time on boilerplate instead of learning

**Benefits of this system:**
- ✅ **Zero config errors** - Scripts generate everything correctly
- ✅ **Focus on learning** - Students write robot logic, not setup code
- ✅ **Can't break the menu** - Auto-updated when adding missions
- ✅ **Robot-specific** - Each season is configured for their robot
- ✅ **Progressive disclosure** - Start simple, add complexity as needed

### Teaching Workflow

1. **Day 1:** Students run `new_season.py` as a team
   - Discusses ports, measurements, team name together
   - Creates their season folder

2. **Week 1-2:** Students create simple missions
   - Each student/pair creates their own mission
   - Learn basic driving and display commands
   - Test and debug individually

3. **Week 3-4:** Build competition missions
   - More complex missions using attachments/sensors
   - Combine missions for full competition runs
   - Optimize and tune movements

4. **Competition:** Upload and go!
   - All missions in one menu
   - Easy to select and run
   - Clear organization by number

### Key Features for Education

- **Helpful comments:** Mission templates include examples for common tasks
- **Safe defaults:** Attachment motors are optional (won't error if not connected)
- **Clear structure:** One mission per file, easy to organize
- **Version control friendly:** Each mission is independent
- **Debugging support:** Detailed print statements and error messages

## 📚 Documentation

- **[STUDENT_GUIDE.md](STUDENT_GUIDE.md)** - Complete walkthrough for students
- **[season_example/QUICKSTART.md](season_example/QUICKSTART.md)** - 5-minute guide to example missions
- **[season_example/README.md](season_example/README.md)** - Technical details about structure
- **[season_example/INSTRUCTIONS.md](season_example/INSTRUCTIONS.md)** - Manual mission creation (advanced)

## 🤖 PyBricks Concepts Covered

The examples and templates teach:
- Hub initialization and configuration
- Motor control (speed, position, direction)
- DriveBase for two-wheeled robots
- Display output (numbers, text, icons, patterns)
- Buttons and user input
- IMU/tilt sensor usage
- Hub lights and sounds
- Error handling and cleanup
- Code organization and modularity

## 🔧 Technical Details

### PyBricks Import Limitation
PyBricks MicroPython **does not support subdirectories** for imports. All files must be in a flat structure in the same directory. This repository has been carefully designed to work within this limitation.

### File Organization
Each season folder contains:
- `season_config.py` - Robot-specific configuration
- `season_menu.py` - Mission selector menu
- `mission_XX_name.py` - Individual mission files (auto-numbered)
- `robot_controller.py` - Shared robot utilities
- `display_patterns.py` - Shared display utilities
- `shape_movements.py` - Shared movement utilities

All files must be uploaded together to the SPIKE Prime hub.

## 🎓 Learning Progression

### Beginner (Week 1)
- Run `new_season.py` and `new_mission.py`
- Try `mission_03_square_display` from examples (no motors)
- Make robot drive straight
- Make robot turn

### Intermediate (Weeks 2-3)
- Drive in shapes (square, circle)
- Use display patterns
- Combine movements
- Add waiting/timing

### Advanced (Weeks 4+)
- Use attachment motors
- Read sensors
- Make decisions based on sensor data
- Create complex multi-step missions
- Optimize for speed and accuracy

## ❓ Common Issues

See the **Troubleshooting** section in [STUDENT_GUIDE.md](STUDENT_GUIDE.md) for solutions to:
- Robot driving backward
- Inaccurate turns
- Import errors
- Missing motors/sensors

## 📖 Additional Resources

- [Official PyBricks Documentation](https://docs.pybricks.com)
- [PyBricks Examples on GitHub](https://github.com/pybricks/pybricks-micropython)
- Reference documentation in `reference_docs/`
- Working code examples in `reference_code/`

## 🤝 Contributing

This repository is designed for middle school robotics education. If you have suggestions or improvements, please share them!

## 📝 License

This is an educational resource. Feel free to use and adapt for your robotics team!

---

**Ready to get started? Read the [Student Guide](STUDENT_GUIDE.md)!**

🤖 **Happy Coding!**
