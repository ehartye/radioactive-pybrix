# FLL Launch Strategies Research
## Improving Robot Accuracy and Consistency

**Research Date:** November 2024
**Focus:** How FIRST LEGO League teams ensure consistent robot launches and handle competition table variations

---

## Executive Summary

FLL teams face two critical accuracy challenges:
1. **Starting Position Consistency** - Ensuring the robot launches from the exact same position/orientation each time
2. **Table Variations** - Adapting to different table structures and mat inconsistencies at competitions

This research document compiles strategies used by successful FLL teams to address these challenges through mechanical design, alignment techniques, sensor usage, and programming approaches.

---

## 1. Starting Position / Launch Strategies

### 1.1 Alignment Jigs (Most Common)

**What is a Jig?**
- A guide made from LEGO parts that helps position the robot before launch
- Ensures the robot starts in the same position and orientation every time
- Increases consistency between different operators

**Advantages:**
- ✅ Most reliable method for consistent starting position
- ✅ Reduces operator variability
- ✅ Quick to use during competition
- ✅ Can encode exact position and heading

**Disadvantages:**
- ❌ Must be brought to tournaments and practice
- ❌ Requires construction time
- ❌ Can only be made from LEGO parts (per rules)

**Implementation Tips:**
- Design jig to align against base area walls (south and west walls)
- Include alignment points for both robot position AND heading
- Make it quick to insert/remove the robot
- Practice with all team members so everyone can use it consistently

### 1.2 Hash Mark Alignment

**What is it?**
- Teams align robot to the hash marks printed around the edge of the base area
- Uses the mat's existing markings as visual guides

**Advantages:**
- ✅ No extra equipment needed
- ✅ Works on any official FLL mat
- ✅ Simple to explain and teach

**Disadvantages:**
- ❌ Less precise than jigs
- ❌ More operator-dependent
- ❌ Hash marks may vary between mats

**Best for:** Teams without time to build jigs, or as backup method

### 1.3 Wall Alignment

**What is it?**
- Robot has flat sides (bumpers) that align against the south and west walls
- May be manual (operator positions) or automatic (robot self-aligns)

**Manual Wall Alignment:**
- Robot designed with completely flat back side
- Operator pushes robot against walls to align
- Simple and effective

**Automatic Self-Alignment:**
- Robot drives itself to the walls and squares up
- Uses motors to push against walls until aligned
- Can use touch sensors to detect wall contact
- More sophisticated: one motor stops when touch sensor hits, other continues until both aligned

**Advantages:**
- ✅ Highly consistent if robot has good bumpers
- ✅ Self-alignment eliminates operator error
- ✅ Can re-align during mission runs

**Disadvantages:**
- ❌ Requires robot design consideration
- ❌ Self-alignment uses match time
- ❌ May not work if walls are inconsistent

**Design Tips:**
- Build completely flat bumpers on robot sides
- Consider adding touch sensors for automatic alignment
- Test on multiple tables to ensure bumpers work with wall variations

### 1.4 Combined Approach

**Most successful teams use multiple methods:**
- Jig for initial positioning
- Flat sides for wall alignment as backup
- Train all team members on both methods

---

## 2. Accuracy Techniques During Missions

### 2.1 Gyro/IMU Sensor (Critical for Accuracy)

**What it does:**
- Measures robot heading (which direction it's pointing)
- Enables accurate turns without drift
- Allows straight driving even on uneven surfaces

**Key Techniques:**

**Gyro-Based Turning:**
- Robot resets gyro to 0° at program start
- Turns use gyro feedback instead of motor rotations
- Dramatically more accurate than rotation-based turns
- **Example:** "Turn 90°" using gyro will be precise regardless of:
  - Battery level
  - Motor wear
  - Surface friction
  - Mat inconsistencies

**Gyro-Based Straight Driving:**
- Constantly monitors heading while driving
- Adjusts motor speeds to maintain straight line
- Compensates for:
  - Uneven motors
  - Mat wrinkles
  - Weight distribution
  - Floor slope

**PID Control (Advanced):**
- **P** (Proportional): Corrects current heading error
- **I** (Integral): Corrects accumulated past errors
- **D** (Derivative): Predicts and prevents future errors
- Results in smooth, accurate navigation

**Implementation Notes:**
- PyBricks SPIKE Prime has built-in IMU (gyro + accelerometer)
- In this project, gyro is automatically enabled: `robot.drivebase.use_gyro(True)`
- Students just use `robot.drivebase.straight()` and `robot.drivebase.turn()` - gyro is already working!

### 2.2 Color Sensor Alignment (Game-Changer)

**Why Color Sensors?**
- Mat has black lines throughout
- Sensors can detect lines with extreme precision
- "Resets" position errors - robot corrects itself using lines

**Basic Line Alignment:**
```
Robot drives until sensor sees black line
→ Stops at consistent position every time
→ Eliminates accumulated distance errors
```

**Double Align Technique (Highly Recommended):**

**What is it?**
- Align to a line TWICE in sequence
- Handles mistakes in first alignment
- Described as "probably the maximum level of accuracy you can get with these robots"

**How it works:**
1. Move forward until left sensor detects line → stop left motor
2. Continue until right sensor detects line → stop right motor
3. Robot is now squared on the line
4. Repeat the process a second time to eliminate any slippage

**Why it's powerful:**
- First align might have small errors (wheel slip, momentum)
- Second align corrects those errors
- Result: "extremely precise" positioning
- Works even if mat is shifted or table is warped

**Programming Approach:**
- Use ONLY sensors, no timers or degree counts
- Sensor-based = adapts to any table
- Timer-based = fails if table varies

**Forward Align vs Backward Align:**
- **Forward align:** Drive forward to line, stop when detected
- **Backward align:** Drive backward to line (useful for repositioning)
- Can combine: forward align on one line, backward align on another

**Line Following:**
- One sensor follows edge of line
- Keeps robot on track between mission models
- Can stop at intersections (second line crossing)

**Typical Pattern:**
```
1. Drive from base using gyro (straight/turn)
2. Align to first black line (double align)
3. Drive to mission model
4. Complete mission
5. Align to line again before returning
6. Drive back to base
```

### 2.3 Mechanical Alignment (Attachments)

**Smart Attachment Design:**
- Leading parts that allow attachment to pivot
- If robot approach angle is slightly off, attachment self-corrects
- Less important to be perfect with robot positioning
- Attachment mechanically aligns to mission model

**Example:**
- Hook attachment with angled entry guides
- Even if robot is 5° off, hook slides into correct position
- Reduces programming precision requirements

**Philosophy:**
- "Teams with the most success depend on their robot using field models or walls to guide their robot"
- Attachments should work from multiple angles
- Build forgiveness into mechanical design

### 2.4 Speed vs Accuracy Trade-off

**Research Finding:**
- Slower speeds = more accurate
- Faster speeds = more momentum, overshoot, vibration

**Strategic Approach:**
- Use slower speeds (200-300 mm/s) for precise positioning
- Use faster speeds (400-600 mm/s) for travel between areas
- Slow down before alignment points

**In Practice:**
```python
# Fast travel
robot.drivebase.settings(drive_speed=500)
robot.drivebase.straight(800)

# Slow down for precision
robot.drivebase.settings(drive_speed=200)
robot.drivebase.straight(100)  # Final approach
```

---

## 3. Handling Table/Mat Inconsistencies

### 3.1 Known Inconsistencies

**Mat Issues:**
- Some waviness expected (improves over time)
- Mat length can vary slightly
- Lines may not be perfectly straight
- Mat may shift during competition

**Table Issues:**
- Tables can warp easily
- Border wall heights vary within tolerances
- Table sections may not align out of the box
- Different materials globally = dimensional variations

**Field Models:**
- Must be aligned to mat wireframe per official setup guide
- Some play in positioning exists

### 3.2 Team Strategies

**Pre-Match Table Review:**
- ALWAYS have designated person inspect table before match
- Check for major mat warps
- Note any unusual wall heights
- Identify which lines are straightest for alignment

**Designated Robot Operators:**
- All team members should learn alignment
- Identify who is best at lining up robot
- Position that person at table for consistency
- Have backup operators ready

**Sensor-Based Programming (Not Timer-Based):**

**Why this matters:**
- Timer-based: "Run motors for 2 seconds" → Distance varies by table
- Sensor-based: "Drive until color sensor sees black" → Works on any table

**Example:**
```
❌ BAD (Timer-based):
   Drive forward for 3 seconds
   → May be too far on one table, too short on another

✅ GOOD (Sensor-based):
   Drive forward until color sensor detects black line
   → Same result on every table
```

**Using Field Features:**
- Align to walls when possible
- Use mission models as alignment references
- Touch walls/models to reset position
- Don't rely solely on distance from base

**Simplified Programming:**
- "Multi-mission programs consist mainly of movement blocks and gyro turns"
- Keep programs simple and straightforward
- Avoid overly complex logic that might fail on different tables
- "Intelligently utilize opportunities to align on mission models, walls, lines, etc."

### 3.3 Robot Design Considerations

**Flat Bumpers:**
- Completely flat back/sides for wall alignment
- Works as backup if primary method fails
- Can realign mid-mission

**Robust Attachments:**
- Don't break if they hit walls slightly wrong
- Flexible/forgiving entry guides
- Can handle ±5-10° positioning variance

**Low Center of Gravity:**
- Reduces sensitivity to mat warps
- Less likely to tip on uneven surfaces
- More consistent wheel contact

---

## 4. Complete Strategy Framework

### 4.1 Before Competition

**Robot Design:**
- [ ] Flat back/sides for wall alignment
- [ ] Color sensors mounted for line detection
- [ ] Gyro/IMU calibrated and tested
- [ ] Attachments with mechanical tolerance
- [ ] Low, stable center of gravity

**Programming:**
- [ ] All turns use gyro
- [ ] Straight drives use gyro correction
- [ ] Line alignment at key points
- [ ] Double align on critical missions
- [ ] Sensor-based, not timer-based
- [ ] Speed optimized (slow near alignment points)

**Team Preparation:**
- [ ] Build and test alignment jig
- [ ] All members practice robot placement
- [ ] Identify best robot operator(s)
- [ ] Test on multiple practice tables
- [ ] Practice pre-match table inspection

### 4.2 At Competition

**Pre-Match (3 minutes before):**
1. Designated person inspects table
2. Note any major mat/wall issues
3. Identify best lines for alignment
4. Discuss any strategy adjustments
5. Designated operator gets ready

**During Match:**
1. Use jig/alignment method consistently
2. Trust your sensors, not your eyes
3. If robot seems off, trust the program (it's using sensors)
4. Stay calm - realignment happens during mission

**Between Matches:**
1. Review what worked/didn't work
2. Check battery levels
3. Verify attachments are secure
4. Practice alignment method

### 4.3 The Reliability Mindset

**Key Philosophy from Top Teams:**

> "Using only the sensors, not depending on timers and degrees, is the right way to achieve a consistent and reliable robot."

> "Teams with the most success depend on their robot using field models or walls to guide their robot."

> "Double alignment is a very powerful concept that everybody should have in their toolbox."

**Three Pillars of Accuracy:**
1. **Consistent starting position** (jig, wall, hash marks)
2. **Self-correction during missions** (sensors, alignment)
3. **Simple, robust programming** (gyro, sensors, not timers)

---

## 5. Practical Implementation for This Project

### 5.1 What Students Already Have

**Good news - the RobotController in this project already implements key accuracy features:**

✅ **Gyro enabled by default:** `robot.drivebase.use_gyro(True)` in `robot_controller.py`
✅ **Accurate turns:** `robot.drivebase.turn(90)` uses gyro automatically
✅ **Straight driving:** `robot.drivebase.straight(500)` maintains heading with gyro
✅ **Color sensors:** If configured, available as `robot.left_color_sensor` / `robot.right_color_sensor`

### 5.2 What Students Need to Add

**For Basic Accuracy:**
- Design jig or alignment method for starting position
- Test and calibrate wheel diameter and axle track in `season_config.py`
- Use `robot.drivebase.straight()` and `robot.drivebase.turn()` (gyro is automatic!)

**For Advanced Accuracy:**
- Add color sensors to `season_config.py`
- Implement line alignment in missions
- Use double align technique for critical positioning
- Design flat robot sides for wall alignment

### 5.3 Example: Line Alignment Code

**Simple align to black line:**
```python
def run(robot: RobotController):
    from pybricks.tools import wait

    # Drive forward until left sensor sees black
    if robot.left_color_sensor:
        robot.drivebase.drive(100, 0)  # Start driving
        while robot.left_color_sensor.reflection() > 20:
            wait(10)  # Check every 10ms
        robot.drivebase.stop()
        print("Aligned to line!")
```

**Double align (square on line):**
```python
def align_to_line(robot: RobotController, speed=100):
    """Align both sensors to black line (square up)"""
    if not (robot.left_color_sensor and robot.right_color_sensor):
        print("Need both color sensors for alignment")
        return

    from pybricks.tools import wait

    # First pass - align left, then right
    robot.drivebase.drive(speed, 0)
    while robot.left_color_sensor.reflection() > 20:
        wait(10)
    robot.drivebase.stop()

    robot.drivebase.drive(speed, 0)
    while robot.right_color_sensor.reflection() > 20:
        wait(10)
    robot.drivebase.stop()

    # Second pass - repeat for double align
    robot.drivebase.drive(speed, 0)
    while robot.left_color_sensor.reflection() > 20:
        wait(10)
    robot.drivebase.stop()

    robot.drivebase.drive(speed, 0)
    while robot.right_color_sensor.reflection() > 20:
        wait(10)
    robot.drivebase.stop()

    print("Double aligned to line!")
```

**Using in a mission:**
```python
def run(robot: RobotController):
    # 1. Start from base using jig alignment

    # 2. Drive toward first mission
    robot.drivebase.straight(400)  # Gyro keeps us straight
    robot.drivebase.turn(45)       # Gyro makes turn accurate

    # 3. Align to line for precision
    align_to_line(robot, speed=100)

    # 4. Now we're perfectly positioned - complete mission
    robot.drivebase.straight(150)  # Exact distance to mission model

    # 5. Do mission action
    if robot.left_attachment:
        robot.left_attachment.run_angle(300, 90)

    # 6. Return (align again before leaving)
    robot.drivebase.straight(-150)
    align_to_line(robot, speed=100)
    robot.drivebase.turn(-45)
    robot.drivebase.straight(-400)
```

---

## 6. Key Takeaways

### For Coaches/Mentors:
1. Teach jig creation early - it's the foundation
2. Emphasize sensor-based programming over timers
3. Have students test on multiple tables if possible
4. Train all team members on alignment procedures
5. Build in mechanical tolerance through attachment design

### For Students:
1. **Always** use consistent starting position (jig/wall/hash marks)
2. **Always** use gyro for turns (already enabled in this project!)
3. Use color sensors to realign at critical points
4. Double align before critical missions
5. Slower speeds near alignment points
6. Simple programs are more reliable than complex ones

### For Programmers:
1. Sensors > Timers (always)
2. Gyro turns > Rotation-based turns
3. Line alignment = free position reset
4. Double align = maximum accuracy
5. Speed settings matter - optimize per mission section

---

## 7. Additional Resources

**Recommended Reading:**
- PRIME LESSONS - "Reliability Techniques" (primelessons.org)
- FLLCasts tutorials on color sensor alignment
- FLL Tutorials - "Aligning in Launch Area" by Seshan Brothers
- RoboCatz - "Using the Wall" guide

**Practice Exercises:**
1. Build and test alignment jig
2. Practice gyro turns - measure accuracy
3. Test line following with color sensors
4. Compare timer-based vs sensor-based programming
5. Test on warped mat section deliberately

---

## Conclusion

FLL launch accuracy comes from three strategies working together:

1. **Consistent Starting Position**
   - Jigs (primary)
   - Wall alignment (backup)
   - Hash marks (fallback)

2. **Self-Correction During Missions**
   - Gyro for straight/turn accuracy
   - Color sensors for line alignment
   - Double align for critical positioning

3. **Robust Design & Programming**
   - Sensor-based, not timer-based
   - Mechanical tolerance in attachments
   - Simple, reliable programs
   - Trained operators

Teams that master all three strategies achieve consistent, high-scoring runs regardless of table variations.

**The Bottom Line:** Build a reliable starting method, use sensors to correct during the mission, and keep it simple. That's how winning teams handle accuracy!

---

**Document Version:** 1.0
**Last Updated:** November 2024
**Sources:** FLL competition forums, FLLCasts tutorials, PRIME LESSONS, team strategy guides
