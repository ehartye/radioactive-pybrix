# Quick Start Guide (5 Minutes)

Welcome! This guide will get you up and running with your SPIKE Prime robot in just a few minutes.

## Before You Begin

**Important:** All Python files in this folder should be uploaded together to your SPIKE Prime hub. PyBricks MicroPython requires all files to be in the same directory (no subdirectories).

## Step 1: Hardware Setup (2 minutes)

### Required Motors
1. **Left wheel motor** → Plug into **Port C**
2. **Right wheel motor** → Plug into **Port D**

### Optional Motors (can add later)
- Left attachment → Port E
- Right attachment → Port F
- Color sensors → Ports A and B

**Note:** The template will work fine with just the two wheel motors! Attachment motors are optional and won't cause errors if not connected.

## Step 2: Upload to Your Hub (1 minute)

### Using PyBricks Code Editor (Web or App)

1. Connect your SPIKE Prime hub via USB or Bluetooth
2. Open PyBricks Code: https://code.pybricks.com
3. Create a new project called "Season Template"
4. Upload **ALL Python files** from this folder:
   - `season_menu.py` (the main program)
   - `season_config.py`
   - `robot_controller.py`
   - `display_patterns.py`
   - `shape_movements.py`
   - `mission_01_square_drive.py`
   - `mission_02_circle_drive.py`
   - `mission_03_square_display.py`
   - `mission_04_triangle_combo.py`

5. Run `season_menu.py`

## Step 3: Navigate the Menu (2 minutes)

When `season_menu.py` runs, you'll see:
- Welcome screen with "SEASON" on the hub display
- Blue light on the hub
- Menu with 4 missions to choose from

### Using the Hub Buttons:
- **LEFT/RIGHT buttons**: Choose mission (1-4)
- **CENTER button**: Run selected mission
- **Press Q**: Return to menu (or run another mission)

### What Each Mission Does:

**Mission 1: Square Drive** ⬜
- Drives robot in a square pattern
- Requires: Both wheel motors
- Good for: Testing basic driving

**Mission 2: Circle Drive** ⭕
- Drives robot in a circle
- Requires: Both wheel motors
- Good for: Testing curved movements

**Mission 3: Square Display** 📺
- Shows animated square on hub screen
- Requires: Nothing! (no motors needed)
- Good for: First test if you don't have motors yet

**Mission 4: Triangle Combo** 🔺
- Drives triangle while showing animation
- Requires: Both wheel motors
- Good for: Testing coordinated actions

## Step 4: Try Your First Mission

We recommend starting with **Mission 3 (Square Display)** because:
- ✅ Doesn't require motors to be connected
- ✅ Safe to test anywhere
- ✅ Shows that your hub is working correctly

1. Use LEFT/RIGHT buttons to select "3"
2. Press CENTER button
3. Watch the animated square pattern on the display!

## Step 5: Make Your First Change

Let's customize Mission 1 to make a bigger square:

1. Open `mission_01_square_drive.py`
2. Find line 15:
   ```python
   "square_size": 300,  # Size of square in mm
   ```
3. Change it to:
   ```python
   "square_size": 500,  # Bigger square!
   ```
4. Upload the changed file to your hub
5. Run Mission 1 again and see the difference!

## Troubleshooting

### "Hub not connecting"
- Make sure hub is turned on
- Try USB cable instead of Bluetooth
- Press the hub button to wake it up

### "Import errors" or "Module not found"
- Make sure you uploaded ALL .py files
- All files must be in the same directory (no subdirectories)
- Try uploading all files again

### "Robot drives backward instead of forward"
- This is normal! Motor directions vary by robot design
- Open `season_config.py`
- Change the `Directions` for your motors:
  ```python
  LEFT_WHEEL = Direction.CLOCKWISE  # or COUNTERCLOCKWISE
  RIGHT_WHEEL = Direction.CLOCKWISE  # or COUNTERCLOCKWISE
  ```

### "Robot turns the wrong amount"
- You need to measure your robot!
- Measure wheel diameter in mm (usually 56mm for SPIKE wheels)
- Measure axle track (distance between wheel contact points)
- Update these in `season_config.py`:
  ```python
  WHEEL_DIAMETER = 56  # Your measurement in mm
  AXLE_TRACK = 80      # Your measurement in mm
  ```

### "Attachment motor error"
- Don't worry! Attachment motors are optional
- The code will print a warning but continue working
- Only connect attachments when you actually need them

## Next Steps

Once you have the basics working:

1. **Read `INSTRUCTIONS.md`** to learn how to add your own missions
2. **Experiment with settings** - change speeds, sizes, patterns
3. **Look at the code** - see how each mission works
4. **Create new missions** - combine movements in new ways!

## Need Help?

- Check the main `README.md` for detailed documentation
- Look at the example missions for code patterns
- Experiment and have fun! Mistakes are how we learn.

---

**Remember:** The goal is to learn and experiment. If something doesn't work, that's okay! Read the error messages, make small changes, and try again.

Happy coding! 🤖
