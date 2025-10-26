# Claude Code Slash Commands for SPIKE Prime

This directory contains AI-assisted slash commands for helping students create and plan robot missions using Claude Code.

## Available Commands

### `/new-season` - AI-Guided Season Creation

Helps students create a new season folder with conversational guidance and explanations.

**What it does:**
- Asks about season name, team name, robot configuration
- Explains WHY each piece of information is needed (teaching moment)
- Helps with port identification and measurements
- Creates season folder using `new_season.py` script
- Guides student to next steps

**When to use:**
- Student is creating their first season (needs extra guidance)
- Student is confused about ports or measurements
- Student prefers conversational interface
- Student wants to understand what they're configuring

**Advantages over `python new_season.py`:**
- More educational and explanatory
- Can answer questions during setup
- Validates and catches common mistakes
- Teaches concepts as you go

### `/new-mission` - AI-Guided Mission Planning

Helps students plan and create missions with mission design guidance and structure suggestions.

**What it does:**
- Asks "What do you want your robot to do?" and explores objectives
- Breaks down complex missions into steps
- Suggests appropriate approaches (line following, attachments, etc.)
- Helps think through mission structure before coding
- Creates mission file using `new_mission.py` script
- Offers to continue helping with code implementation

**When to use:**
- Student knows what they want but not how to do it
- Student's mission idea is complex (help break it down)
- Student wants help planning before coding
- Student is learning mission design patterns

**Advantages over `python new_mission.py`:**
- Helps with mission planning and structure
- Teaches FLL mission patterns
- Breaks down complex objectives
- Can continue helping with implementation
- Encourages good problem-solving habits

## How Students Use These

Students with Claude Code installed can use these instead of the Python scripts:

**Traditional way:**
```bash
python new_season.py         # Answer questions
cd my_season/
python ../new_mission.py     # Answer questions
# Edit mission file
```

**AI-assisted way:**
```bash
# In Claude Code terminal/chat
/new-season                  # Conversational setup
cd my_season/
/new-mission                 # Guided planning + setup
# AI can continue helping with code
```

## Teaching Philosophy

These commands are designed to:

1. **Encourage exploration** - Ask questions to understand objectives
2. **Teach concepts** - Explain WHY things work, not just HOW
3. **Build confidence** - Positive reinforcement and guidance
4. **Develop planning skills** - Help break down problems
5. **Promote good practices** - Suggest simple, testable approaches

## Educational Value

### `/new-season` teaches:
- Robot configuration concepts (ports, motors, sensors)
- Physical measurements and calibration
- Why configuration matters for accuracy

### `/new-mission` teaches:
- Mission planning and decomposition
- Common FLL mission patterns
- Trade-offs (precision vs speed, simple vs complex)
- Testing strategies
- How to structure code logically

## For Educators and Mentors

**Encourage students to use these when:**
- They're stuck on "What should I do?"
- They need help breaking down a complex mission
- They're learning mission design patterns
- They want conversational help and explanations

**Keep Python scripts for:**
- Quick, efficient workflow for experienced students
- Situations without internet/Claude Code access
- When students just want to get it done fast

**Both approaches:**
- Use the same underlying Python scripts
- Generate identical output
- Are fully compatible

## Implementation Notes

These slash commands:
- Use the existing `new_season.py` and `new_mission.py` scripts under the hood
- Gather information conversationally via `AskUserQuestion` tool
- Run the scripts with Bash tool, providing answers
- Follow up with guidance and offers of continued help
- Maintain age-appropriate, encouraging tone throughout

## Future Enhancements

Potential additions:
- `/mission-help` - Get help with specific coding patterns
- `/debug-mission` - Help debug a mission that's not working
- `/calibrate-robot` - Guide through robot calibration process
- `/plan-season` - Help plan multiple missions for a competition

## Questions or Issues?

These are custom commands specific to this learning project. They wrap the existing Python automation scripts with AI-guided conversation and teaching.
