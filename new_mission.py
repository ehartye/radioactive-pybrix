#!/usr/bin/env python3
"""
SPIKE Prime Mission Creator
Interactive script to add a new mission to an existing season

Usage:
    # Interactive mode (will find and list season folders)
    python new_mission.py

    # Specify season folder
    python new_mission.py --season path/to/season_folder

    # Headless mode (for AI/scripting)
    python new_mission.py --season path/to/season --name "Mission Name" \
        --description "Description" --speed 200 --turn-rate 60 --template guided
"""

import os
import re
import sys
import argparse


def find_season_folders(search_dir="."):
    """Find all season folders (containing season_menu.py) in search_dir"""
    season_folders = []

    # Check current directory first
    if os.path.exists(os.path.join(search_dir, "season_menu.py")):
        season_folders.append(os.path.abspath(search_dir))

    # Check subdirectories
    try:
        for item in os.listdir(search_dir):
            item_path = os.path.join(search_dir, item)
            if os.path.isdir(item_path):
                menu_path = os.path.join(item_path, "season_menu.py")
                config_path = os.path.join(item_path, "season_config.py")
                if os.path.exists(menu_path) and os.path.exists(config_path):
                    season_folders.append(os.path.abspath(item_path))
    except PermissionError:
        pass

    return season_folders


def select_season_folder(season_folders):
    """Interactively select a season folder from a list"""
    if not season_folders:
        return None

    if len(season_folders) == 1:
        print(f"\n✓ Found season: {os.path.basename(season_folders[0])}")
        return season_folders[0]

    print("\n📂 Available seasons:")
    for i, folder in enumerate(season_folders, 1):
        folder_name = os.path.basename(folder)
        print(f"  {i}. {folder_name}")

    while True:
        choice = input(f"\nSelect season (1-{len(season_folders)}): ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(season_folders):
                return season_folders[idx]
            print(f"  ❌ Please enter a number between 1 and {len(season_folders)}")
        except ValueError:
            print("  ❌ Please enter a valid number")


def validate_season_folder(folder):
    """Check if folder is a valid season folder"""
    if not os.path.exists(folder):
        return False, f"Folder does not exist: {folder}"

    if not os.path.isdir(folder):
        return False, f"Not a directory: {folder}"

    menu_path = os.path.join(folder, "season_menu.py")
    if not os.path.exists(menu_path):
        return False, f"season_menu.py not found in {folder}"

    config_path = os.path.join(folder, "season_config.py")
    if not os.path.exists(config_path):
        return False, f"season_config.py not found in {folder}"

    return True, "Valid season folder"


def sanitize_function_name(name):
    """Convert name to valid Python function/file name"""
    # Replace spaces with underscores, remove special chars
    name = re.sub(r'[^\w\s]', '', name.lower())
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

        if value:
            # Validate against options if provided
            if valid_options and value not in valid_options:
                print(f"  ❌ Please enter one of: {', '.join(valid_options)}")
                continue
            return value

        if not default:
            print("  ❌ This field is required")


def get_number(prompt, default, min_val=None, max_val=None):
    """Get numeric input with optional range validation"""
    while True:
        value = get_input(prompt, str(default))
        try:
            num = int(value)
            if min_val is not None and num < min_val:
                print(f"  ❌ Value must be at least {min_val}")
                continue
            if max_val is not None and num > max_val:
                print(f"  ❌ Value must be at most {max_val}")
                continue
            return num
        except ValueError:
            print("  ❌ Please enter a valid number")


def find_next_mission_number(folder):
    """Find the next available mission number"""
    existing_missions = []
    for filename in os.listdir(folder):
        if filename.startswith("mission_") and filename.endswith(".py"):
            try:
                # Extract number from mission_XX_name.py
                num_str = filename.split("_")[1]
                existing_missions.append(int(num_str))
            except (IndexError, ValueError):
                continue

    if not existing_missions:
        return 1
    return max(existing_missions) + 1


def find_template_file(template_name, season_folder):
    """Find the template file, searching in multiple locations"""
    # Try relative to season folder
    rel_path = os.path.join(season_folder, "..", "season_template", template_name)
    if os.path.exists(rel_path):
        return os.path.abspath(rel_path)

    # Try relative to script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, "season_template", template_name)
    if os.path.exists(script_path):
        return script_path

    # Try common locations
    cwd_path = os.path.join(os.getcwd(), "season_template", template_name)
    if os.path.exists(cwd_path):
        return cwd_path

    return None


def update_season_menu(folder, mission_num, mission_name, mission_desc, mission_filename):
    """Update season_menu.py to include the new mission"""
    menu_file = os.path.join(folder, "season_menu.py")

    with open(menu_file, "r") as f:
        content = f.read()

    # Extract mission module name (without .py)
    mission_module = mission_filename.replace(".py", "")

    # Add import
    import_line = f"import {mission_module}"
    if "# No missions yet" in content:
        # First mission - replace the placeholder
        content = content.replace(
            "# No missions yet - use new_mission.py to add missions",
            import_line
        )
    else:
        # Add to existing imports - find last import statement
        lines = content.split("\n")
        last_import_idx = 0
        for i, line in enumerate(lines):
            if line.startswith("import mission_"):
                last_import_idx = i

        lines.insert(last_import_idx + 1, import_line)
        content = "\n".join(lines)

    # Add to missions dictionary
    mission_entry = f'''            "{mission_num}": {{
                "name": "{mission_name}",
                "description": "{mission_desc}",
                "run_function": {mission_module}
            }}'''

    if "# No missions yet" in content:
        # First mission - replace placeholder
        content = content.replace(
            "            # No missions yet",
            mission_entry
        )
    else:
        # Add to existing missions - find the closing brace of the dict
        # Insert before the last closing brace
        lines = content.split("\n")
        dict_end_idx = 0
        brace_count = 0
        in_missions_dict = False

        for i, line in enumerate(lines):
            if "self.missions = {" in line:
                in_missions_dict = True
                brace_count = 1
                continue

            if in_missions_dict:
                brace_count += line.count("{") - line.count("}")
                if brace_count == 0:
                    dict_end_idx = i
                    break

        # Add comma to previous entry if it exists
        if dict_end_idx > 0:
            # Find the last '}' before dict_end_idx that's part of a mission entry
            for i in range(dict_end_idx - 1, 0, -1):
                if "}" in lines[i] and "}" not in lines[i].rstrip()[-1]:
                    continue
                if "}" in lines[i]:
                    lines[i] = lines[i].rstrip() + ","
                    break

        # Insert new mission
        indent = "            "
        mission_lines = mission_entry.split("\n")
        for j, mission_line in enumerate(mission_lines):
            lines.insert(dict_end_idx + j, mission_line)

        content = "\n".join(lines)

    # Update hub_menu options and range
    existing_missions = []
    lines = content.split("\n")
    for line in lines:
        if '"' in line and '": {' in line:
            match = re.search(r'"(\d+)":', line)
            if match:
                existing_missions.append(int(match.group(1)))

    existing_missions.sort()
    mission_range = f"1-{max(existing_missions)}" if existing_missions else "none"
    mission_options = ', '.join([f'"{m}"' for m in existing_missions] + ['"Q"'])

    # Update the mission range in the print statement
    # Match either literal \n or actual newline in the f-string
    content = re.sub(
        r'Select mission \([^)]+\) or Q to quit',
        f'Select mission ({mission_range}) or Q to quit',
        content
    )

    # Update the hub_menu options
    content = re.sub(
        r'selected = hub_menu\([^)]+\)',
        f'selected = hub_menu({mission_options})',
        content
    )

    # Write updated content
    with open(menu_file, "w") as f:
        f.write(content)


def create_mission(season_folder, mission_name, mission_desc=None, drive_speed=200,
                   turn_rate=60, template_style="guided", quiet=False):
    """
    Create a mission in the specified season folder

    Args:
        season_folder: Path to season folder
        mission_name: Name of the mission
        mission_desc: Description (defaults to mission_name)
        drive_speed: Drive speed in mm/s (default: 200)
        turn_rate: Turn rate in degrees/s (default: 60)
        template_style: "simple" or "guided" (default: "guided")
        quiet: If True, suppress output (default: False)

    Returns:
        tuple: (success: bool, mission_filepath: str, message: str)
    """
    def log(msg):
        if not quiet:
            print(msg)

    # Validate season folder
    valid, msg = validate_season_folder(season_folder)
    if not valid:
        return False, None, msg

    # Use mission name as description if not provided
    if mission_desc is None:
        mission_desc = mission_name

    # Find next mission number
    mission_num = find_next_mission_number(season_folder)
    log(f"\n  📝 This will be Mission #{mission_num}")

    # Generate filenames
    sanitized_name = sanitize_function_name(mission_name)
    mission_filename = f"mission_{mission_num:02d}_{sanitized_name}.py"
    mission_filepath = os.path.join(season_folder, mission_filename)

    # Determine template
    if template_style.lower() in ["simple", "1"]:
        template_name = "_template_mission_simple.py"
    else:
        template_name = "_template_mission_guided.py"

    # Find template file
    template_file = find_template_file(template_name, season_folder)
    if not template_file:
        return False, None, f"Template not found: {template_name}"

    # Load and fill template
    with open(template_file, "r") as f:
        template_content = f.read()

    mission_content = template_content.format(
        MISSION_NUM=mission_num,
        MISSION_NAME=mission_name,
        MISSION_DESCRIPTION=mission_desc,
        DRIVE_SPEED=drive_speed,
        TURN_RATE=turn_rate
    )

    # Write mission file
    with open(mission_filepath, "w") as f:
        f.write(mission_content)
    log(f"✅ Created: {mission_filename}")

    # Update menu
    try:
        update_season_menu(season_folder, mission_num, mission_name,
                          mission_desc, mission_filename)
        log(f"✅ Updated: season_menu.py (added as option {mission_num})")
    except Exception as e:
        log(f"⚠️  Warning: Could not auto-update menu: {e}")
        log("   You may need to manually add the mission to season_menu.py")

    return True, mission_filepath, f"Mission {mission_num} created successfully"


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Create a new mission for your SPIKE Prime robot season",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode - will find and select season
  python new_mission.py

  # Specify season folder interactively
  python new_mission.py --season my_season_folder

  # Headless mode (all options specified)
  python new_mission.py --season my_season \\
      --name "Drive to Target" \\
      --description "Navigate to target and return" \\
      --speed 200 --turn-rate 60 --template guided
        """
    )

    parser.add_argument("--season", help="Path to season folder")
    parser.add_argument("--name", help="Mission name")
    parser.add_argument("--description", help="Mission description")
    parser.add_argument("--speed", type=int, help="Drive speed (mm/s, default: 200)")
    parser.add_argument("--turn-rate", type=int, help="Turn rate (deg/s, default: 60)")
    parser.add_argument("--template", choices=["simple", "guided"],
                       help="Template style (default: guided)")
    parser.add_argument("--quiet", action="store_true",
                       help="Suppress output (for scripting)")

    args = parser.parse_args()

    # Determine if running in headless mode
    headless = all([args.season, args.name])

    if not headless:
        print("=" * 50)
        print("🎯 SPIKE Prime Mission Creator")
        print("=" * 50)

    # Find season folder
    season_folder = None

    if args.season:
        # Season specified via argument
        season_folder = os.path.abspath(args.season)
        valid, msg = validate_season_folder(season_folder)
        if not valid:
            print(f"\n❌ Error: {msg}")
            return 1
        if not headless:
            print(f"\n✓ Using season: {os.path.basename(season_folder)}")
    else:
        # Find season folders
        season_folders = find_season_folders()

        if not season_folders:
            print("\n❌ No season folders found!")
            print("   A season folder must contain season_menu.py and season_config.py")
            print("\n💡 Create a season first:")
            print("   python new_season.py")
            return 1

        season_folder = select_season_folder(season_folders)
        if not season_folder:
            print("\n❌ No season selected")
            return 1

    # Get mission parameters
    if headless:
        # Headless mode - use arguments
        mission_name = args.name
        mission_desc = args.description or mission_name
        drive_speed = args.speed or 200
        turn_rate = args.turn_rate or 60
        template_style = args.template or "guided"
    else:
        # Interactive mode
        print("\nLet's create a new mission!\n")

        print("📋 MISSION DETAILS")
        mission_name = get_input("Mission name (e.g., 'Drive to Target')")
        mission_desc = get_input("Short description", mission_name)

        print("\n⚙️  MISSION CONFIGURATION")
        print("\n  Robot Drive Speed (how fast the robot moves):")
        print("    • Slow & Careful:  100-150 mm/s")
        print("    • Medium Speed:    200-300 mm/s")
        print("    • Fast:            400-500 mm/s")
        print("    • Racing Speed:    600-800 mm/s")
        drive_speed = get_number("  Choose drive speed (mm/s)", 200, min_val=50, max_val=1000)

        print("\n  Turn Rate (how fast the robot rotates):")
        print("    • Slow & Careful:  30-45 degrees/s")
        print("    • Medium Speed:    60-90 degrees/s")
        print("    • Fast:            120-150 degrees/s")
        print("    • Quick Spin:      200-300 degrees/s")
        turn_rate = get_number("  Choose turn rate (degrees/s)", 60, min_val=10, max_val=500)

        print("\n📋 TEMPLATE STYLE")
        print("  Choose how much help you want:")
        print("    1. Simple  - Minimal template with quick start examples")
        print("    2. Guided  - Full examples with detailed comments (recommended for beginners)")
        template_choice = get_input("  Template style (1/2)", "2", valid_options=["1", "2"])
        template_style = "simple" if template_choice == "1" else "guided"

        print("\n" + "=" * 50)
        print("Creating mission...")
        print("=" * 50)

    # Create the mission
    success, filepath, message = create_mission(
        season_folder, mission_name, mission_desc,
        drive_speed, turn_rate, template_style,
        quiet=args.quiet
    )

    if not success:
        if not args.quiet:
            print(f"\n❌ Error: {message}")
        return 1

    if not headless and not args.quiet:
        # Show success message and next steps
        mission_num = find_next_mission_number(season_folder) - 1  # We just created it
        mission_filename = os.path.basename(filepath)

        print("\n" + "=" * 50)
        print("🎉 Mission ready to code!")
        print("=" * 50)
        print("\n📍 Next steps:")
        print(f"  1. Edit {mission_filename}")
        print("  2. Add your robot logic in the run() function")
        print("  3. Upload all .py files to your hub")
        print(f"  4. Run season_menu.py and select mission {mission_num}")
        print("\n💡 Tip: Look at the helpful code examples in the file!")
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
