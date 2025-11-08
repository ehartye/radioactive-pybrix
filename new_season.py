#!/usr/bin/env python3
"""
SPIKE Prime Season Creator
Interactive script to create a new season folder with custom configuration

Usage:
    # Interactive mode
    python new_season.py

    # Headless mode (for AI/scripting)
    python new_season.py --name "Test Season" --team "Team Test" \
        --left-wheel C --right-wheel D --wheel-diameter 56 --axle-track 80
"""

import os
import shutil
import re
import sys
import argparse

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


def create_season(season_name, team_name, description=None,
                  left_wheel_port="C", right_wheel_port="D",
                  left_attach_port="E", right_attach_port="F",
                  left_sensor_port="A", right_sensor_port="B",
                  wheel_diameter=56, axle_track=80,
                  overwrite=False, quiet=False):
    """
    Create a season folder with configuration

    Args:
        season_name: Name of the season
        team_name: Team name
        description: Season description (defaults to "{season_name} missions")
        left_wheel_port: Port for left wheel motor (A-F, default: C)
        right_wheel_port: Port for right wheel motor (A-F, default: D)
        left_attach_port: Port for left attachment (A-F, default: E)
        right_attach_port: Port for right attachment (A-F, default: F)
        left_sensor_port: Port for left color sensor (A-F, default: A)
        right_sensor_port: Port for right color sensor (A-F, default: B)
        wheel_diameter: Wheel diameter in mm (default: 56)
        axle_track: Distance between wheels in mm (default: 80)
        overwrite: Overwrite existing folder if it exists (default: False)
        quiet: Suppress output (default: False)

    Returns:
        tuple: (success: bool, folder_path: str, message: str)
    """
    def log(msg):
        if not quiet:
            print(msg)

    # Use season name as description if not provided
    if description is None:
        description = f"{season_name} missions"

    # Create folder name
    folder_name = sanitize_folder_name(season_name)

    # Validate ports are different for wheels
    if left_wheel_port == right_wheel_port:
        return False, None, "Left and right wheels can't use the same port!"

    # Standard motor directions
    left_wheel_dir = "COUNTERCLOCKWISE"
    right_wheel_dir = "CLOCKWISE"

    # Check if folder exists
    if os.path.exists(folder_name):
        if not overwrite:
            return False, None, f"Folder '{folder_name}' already exists (use --overwrite to replace)"
        shutil.rmtree(folder_name)

    os.makedirs(folder_name)
    log(f"✅ Created folder: {folder_name}/")

    # Copy shared utility files
    template_dir = "season_template"
    for util_file in ["robot_controller.py", "display_patterns.py", "line_movements.py"]:
        shutil.copy(
            os.path.join(template_dir, util_file),
            os.path.join(folder_name, util_file)
        )
    log("✅ Copied shared utilities")

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
    log("✅ Generated season_config.py with your robot specs")

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
    log("✅ Created season_menu.py (empty, ready for missions)")

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
    log("✅ Created README.md")

    folder_path = os.path.abspath(folder_name)
    return True, folder_path, f"Season '{season_name}' created successfully"


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Create a new season for your SPIKE Prime robot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode
  python new_season.py

  # Headless mode (all options specified)
  python new_season.py --name "Test Season" --team "Team Test" \\
      --left-wheel C --right-wheel D --wheel-diameter 56 --axle-track 80
        """
    )

    parser.add_argument("--name", help="Season name")
    parser.add_argument("--team", help="Team name")
    parser.add_argument("--description", help="Season description")
    parser.add_argument("--left-wheel", choices=["A", "B", "C", "D", "E", "F"],
                       help="Left wheel motor port (default: C)")
    parser.add_argument("--right-wheel", choices=["A", "B", "C", "D", "E", "F"],
                       help="Right wheel motor port (default: D)")
    parser.add_argument("--left-attach", choices=["A", "B", "C", "D", "E", "F"],
                       help="Left attachment port (default: E)")
    parser.add_argument("--right-attach", choices=["A", "B", "C", "D", "E", "F"],
                       help="Right attachment port (default: F)")
    parser.add_argument("--left-sensor", choices=["A", "B", "C", "D", "E", "F"],
                       help="Left color sensor port (default: A)")
    parser.add_argument("--right-sensor", choices=["A", "B", "C", "D", "E", "F"],
                       help="Right color sensor port (default: B)")
    parser.add_argument("--wheel-diameter", type=int,
                       help="Wheel diameter in mm (default: 56)")
    parser.add_argument("--axle-track", type=int,
                       help="Distance between wheels in mm (default: 80)")
    parser.add_argument("--overwrite", action="store_true",
                       help="Overwrite existing season folder")
    parser.add_argument("--quiet", action="store_true",
                       help="Suppress output (for scripting)")

    args = parser.parse_args()

    # Determine if running in headless mode
    headless = bool(args.name and args.team)

    if not headless:
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
            return 1

        # Test direction
        print("\n🔄 MOTOR DIRECTIONS")
        print("  We'll start with standard directions.")
        print("  If your robot drives backward, you can change this in season_config.py")

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
            return 1

        # Create season folder
        print("\n" + "=" * 50)
        print("Creating your season...")
        print("=" * 50)

        overwrite = False
        folder_name = sanitize_folder_name(season_name)
        if os.path.exists(folder_name):
            overwrite = get_yes_no(f"\n  ⚠️  Folder '{folder_name}' already exists. Overwrite?", "n")
            if not overwrite:
                print("  Cancelled.")
                return 0
    else:
        # Headless mode - use arguments
        season_name = args.name
        team_name = args.team
        description = args.description
        left_wheel_port = args.left_wheel or "C"
        right_wheel_port = args.right_wheel or "D"
        left_attach_port = args.left_attach or "E"
        right_attach_port = args.right_attach or "F"
        left_sensor_port = args.left_sensor or "A"
        right_sensor_port = args.right_sensor or "B"
        wheel_diameter = args.wheel_diameter or 56
        axle_track = args.axle_track or 80
        overwrite = args.overwrite

    # Create the season
    success, folder_path, message = create_season(
        season_name, team_name, description,
        left_wheel_port, right_wheel_port,
        left_attach_port, right_attach_port,
        left_sensor_port, right_sensor_port,
        wheel_diameter, axle_track,
        overwrite, args.quiet if headless else False
    )

    if not success:
        if not args.quiet:
            print(f"\n❌ Error: {message}")
        return 1

    if not headless and not args.quiet:
        # Show success message and next steps
        folder_name = os.path.basename(folder_path)
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

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n  Cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
