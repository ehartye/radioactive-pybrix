#!/usr/bin/env python3
"""
SPIKE Prime Season Creator
Interactive script to create a new season folder with custom configuration
"""

import os
import shutil
import re

def sanitize_folder_name(name):
    """Convert name to valid folder name"""
    # Replace spaces with underscores, remove special chars
    name = re.sub(r'[^\w\s-]', '', name.lower())
    name = re.sub(r'[-\s]+', '_', name)
    return name

def get_input(prompt, default=None, valid_options=None):
    """Get user input with optional default and validation"""
    if default:
        prompt_text = f"{prompt} [{default}]: "
    else:
        prompt_text = f"{prompt}: "

    while True:
        value = input(prompt_text).strip()

        # Use default if no input
        if not value and default:
            return default

        # Validate if options provided
        if valid_options and value.upper() not in [opt.upper() for opt in valid_options]:
            print(f"  ❌ Please choose from: {', '.join(valid_options)}")
            continue

        if value:
            return value

        if not default:
            print("  ❌ This field is required")


def get_yes_no(prompt, default="n"):
    """Get yes/no input"""
    result = get_input(f"{prompt} (y/n)", default, ["y", "n", "yes", "no"])
    return result.lower() in ["y", "yes"]


def main():
    print("=" * 50)
    print("🤖 SPIKE Prime Season Creator")
    print("=" * 50)
    print("\nLet's set up your new season!\n")

    # Season info
    print("📋 SEASON INFORMATION")
    season_name = get_input("Season name", "My Season")
    team_name = get_input("Team name", "")
    if not team_name:
        team_name = "Unnamed Team"
    description = get_input("Short description", f"{season_name} missions")

    # Create folder name
    folder_name = sanitize_folder_name(season_name)
    print(f"\n  📁 Season folder will be: {folder_name}/")

    # Robot hardware
    print("\n📍 ROBOT HARDWARE SETUP")
    print("  Where are your motors plugged in?")

    left_wheel_port = get_input("  Left wheel motor port (A/B/C/D/E/F)", "C",
                                  ["A", "B", "C", "D", "E", "F"]).upper()
    right_wheel_port = get_input("  Right wheel motor port (A/B/C/D/E/F)", "D",
                                   ["A", "B", "C", "D", "E", "F"]).upper()

    # Validate ports are different
    if left_wheel_port == right_wheel_port:
        print("  ❌ Error: Left and right wheels can't use the same port!")
        return

    # Test direction
    print("\n🔄 MOTOR DIRECTIONS")
    print("  We'll start with standard directions.")
    print("  If your robot drives backward, you can change this in season_config.py")
    left_wheel_dir = "COUNTERCLOCKWISE"
    right_wheel_dir = "CLOCKWISE"

    # Attachments
    print("\n🔧 OPTIONAL ATTACHMENTS")
    has_attachments = get_yes_no("  Does your robot have attachment motors?", "n")

    if has_attachments:
        left_attach_port = get_input("  Left attachment port (A/B/C/D/E/F)", "E",
                                      ["A", "B", "C", "D", "E", "F"]).upper()
        right_attach_port = get_input("  Right attachment port (A/B/C/D/E/F)", "F",
                                       ["A", "B", "C", "D", "E", "F"]).upper()
    else:
        left_attach_port = "E"
        right_attach_port = "F"

    # Sensors
    has_sensors = get_yes_no("  Does your robot have color sensors?", "n")
    if has_sensors:
        left_sensor_port = get_input("  Left sensor port (A/B/C/D/E/F)", "A",
                                      ["A", "B", "C", "D", "E", "F"]).upper()
        right_sensor_port = get_input("  Right sensor port (A/B/C/D/E/F)", "B",
                                       ["A", "B", "C", "D", "E", "F"]).upper()
    else:
        left_sensor_port = "A"
        right_sensor_port = "B"

    # Robot measurements
    print("\n📏 ROBOT MEASUREMENTS")
    print("  Measure your robot to get accurate movements")
    wheel_diameter = get_input("  Wheel diameter in mm", "56")
    axle_track = get_input("  Distance between wheels (axle track) in mm", "80")

    # Validate numbers
    try:
        wheel_diameter = int(wheel_diameter)
        axle_track = int(axle_track)
    except ValueError:
        print("  ❌ Error: Measurements must be numbers!")
        return

    # Create season folder
    print("\n" + "=" * 50)
    print("Creating your season...")
    print("=" * 50)

    if os.path.exists(folder_name):
        overwrite = get_yes_no(f"\n  ⚠️  Folder '{folder_name}' already exists. Overwrite?", "n")
        if not overwrite:
            print("  Cancelled.")
            return
        shutil.rmtree(folder_name)

    os.makedirs(folder_name)
    print(f"✅ Created folder: {folder_name}/")

    # Copy shared utility files
    template_dir = "season_template"
    for util_file in ["robot_controller.py", "display_patterns.py", "shape_movements.py"]:
        shutil.copy(
            os.path.join(template_dir, util_file),
            os.path.join(folder_name, util_file)
        )
    print("✅ Copied shared utilities")

    # Generate season_config.py from template
    with open(os.path.join(template_dir, "season_config.py.template"), "r") as f:
        config_template = f.read()

    config_content = config_template.format(
        LEFT_WHEEL_PORT=left_wheel_port,
        RIGHT_WHEEL_PORT=right_wheel_port,
        LEFT_ATTACHMENT_PORT=left_attach_port,
        RIGHT_ATTACHMENT_PORT=right_attach_port,
        LEFT_SENSOR_PORT=left_sensor_port,
        RIGHT_SENSOR_PORT=right_sensor_port,
        LEFT_WHEEL_DIR=left_wheel_dir,
        RIGHT_WHEEL_DIR=right_wheel_dir,
        WHEEL_DIAMETER=wheel_diameter,
        AXLE_TRACK=axle_track,
        SEASON_NAME=season_name,
        TEAM_NAME=team_name,
        SEASON_DESCRIPTION=description
    )

    with open(os.path.join(folder_name, "season_config.py"), "w") as f:
        f.write(config_content)
    print("✅ Generated season_config.py with your robot specs")

    # Generate empty season_menu.py
    with open(os.path.join(template_dir, "season_menu.py.template"), "r") as f:
        menu_template = f.read()

    menu_content = menu_template.format(
        MISSION_IMPORTS="# No missions yet - use new_mission.py to add missions",
        MISSION_DICT="            # No missions yet",
        MISSION_RANGE="none yet",
        MISSION_OPTIONS='"Q"'
    )

    with open(os.path.join(folder_name, "season_menu.py"), "w") as f:
        f.write(menu_content)
    print("✅ Created season_menu.py (empty, ready for missions)")

    # Create README
    readme_content = f"""# {season_name}

**Team:** {team_name}

## Robot Configuration

- Left wheel: Port {left_wheel_port}
- Right wheel: Port {right_wheel_port}
- Wheel diameter: {wheel_diameter}mm
- Axle track: {axle_track}mm

## Quick Start

1. **Add your first mission:**
   ```bash
   python ../new_mission.py
   ```

2. **Upload to hub:**
   - Upload ALL .py files to your SPIKE Prime hub

3. **Run the menu:**
   - Run season_menu.py on your hub
   - Use LEFT/RIGHT buttons to select mission
   - Press CENTER to run

## Missions

(Missions will be listed here as you add them)

## Notes

- Edit season_config.py to adjust speeds and settings
- Each mission is in its own file (mission_XX_name.py)
- The menu is automatically updated when you add missions
"""

    with open(os.path.join(folder_name, "README.md"), "w") as f:
        f.write(readme_content)
    print("✅ Created README.md")

    # Success!
    print("\n" + "=" * 50)
    print("🎉 Your season is ready!")
    print("=" * 50)
    print("\n📍 Next steps:")
    print(f"  1. cd {folder_name}")
    print("  2. python ../new_mission.py")
    print("  3. Edit your mission file to add robot movements")
    print("  4. Upload all .py files to your SPIKE Prime hub")
    print("  5. Run season_menu.py\n")
    print(f"💡 Tip: Check {folder_name}/README.md for more info!")
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Cancelled by user.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
