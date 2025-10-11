#!/usr/bin/env python3
"""
SPIKE Prime Mission Creator
Interactive script to add a new mission to an existing season
"""

import os
import re


def sanitize_function_name(name):
    """Convert name to valid Python function/file name"""
    # Replace spaces with underscores, remove special chars
    name = re.sub(r'[^\w\s]', '', name.lower())
    name = re.sub(r'[-\s]+', '_', name)
    return name


def get_input(prompt, default=None):
    """Get user input with optional default"""
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
            return value

        if not default:
            print("  ❌ This field is required")


def get_number(prompt, default):
    """Get numeric input"""
    while True:
        value = get_input(prompt, str(default))
        try:
            return int(value)
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

    content = re.sub(
        r'print\(f"\\nSelect mission \([^)]+\)',
        f'print(f"\\nSelect mission ({mission_range})',
        content
    )

    content = re.sub(
        r'selected = hub_menu\([^)]+\)',
        f'selected = hub_menu({mission_options})',
        content
    )

    # Write updated content
    with open(menu_file, "w") as f:
        f.write(content)


def main():
    print("=" * 50)
    print("🎯 SPIKE Prime Mission Creator")
    print("=" * 50)

    # Check if we're in a season folder
    if not os.path.exists("season_config.py"):
        print("\n❌ Error: Not in a season folder!")
        print("   Run this from inside your season folder")
        print("   Example: cd my_season && python ../new_mission.py")
        return

    if not os.path.exists("season_menu.py"):
        print("\n❌ Error: season_menu.py not found!")
        print("   Make sure you're in a valid season folder")
        return

    print("\nLet's create a new mission!\n")

    # Get mission details
    print("📋 MISSION DETAILS")
    mission_name = get_input("Mission name (e.g., 'Drive to Target')")
    mission_desc = get_input("Short description", f"{mission_name}")

    # Find next mission number
    current_folder = os.getcwd()
    mission_num = find_next_mission_number(current_folder)
    print(f"\n  📝 This will be Mission #{mission_num}")

    # Get configuration
    print("\n⚙️  MISSION CONFIGURATION")
    drive_speed = get_number("Drive speed (mm/s)", 200)
    turn_rate = get_number("Turn rate (degrees/s)", 60)

    # Generate filenames
    sanitized_name = sanitize_function_name(mission_name)
    mission_filename = f"mission_{mission_num:02d}_{sanitized_name}.py"

    print("\n" + "=" * 50)
    print("Creating mission...")
    print("=" * 50)

    # Load template
    template_file = os.path.join("..", "season_template", "_template_mission.py")
    if not os.path.exists(template_file):
        print(f"\n❌ Error: Template not found at {template_file}")
        return

    with open(template_file, "r") as f:
        template_content = f.read()

    # Fill in template
    mission_content = template_content.format(
        MISSION_NUM=mission_num,
        MISSION_NAME=mission_name,
        MISSION_DESCRIPTION=mission_desc,
        DRIVE_SPEED=drive_speed,
        TURN_RATE=turn_rate
    )

    # Write mission file
    with open(mission_filename, "w") as f:
        f.write(mission_content)
    print(f"✅ Created: {mission_filename}")

    # Update menu
    try:
        update_season_menu(current_folder, mission_num, mission_name,
                          mission_desc, mission_filename)
        print(f"✅ Updated: season_menu.py (added as option {mission_num})")
    except Exception as e:
        print(f"⚠️  Warning: Could not auto-update menu: {e}")
        print("   You may need to manually add the mission to season_menu.py")

    # Success!
    print("\n" + "=" * 50)
    print("🎉 Mission ready to code!")
    print("=" * 50)
    print("\n📍 Next steps:")
    print(f"  1. Edit {mission_filename}")
    print("  2. Add your robot logic in the run() function")
    print("  3. Upload all .py files to your hub")
    print("  4. Run season_menu.py and select mission {mission_num}")
    print("\n💡 Tip: Look at the helpful code examples in the file!")
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
