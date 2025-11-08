#!/usr/bin/env python3
"""
Test script to verify season and mission creation in headless mode
Creates a fake season with 3 test missions
"""

import subprocess
import sys
import os
import shutil

def run_command(cmd, description):
    """Run a command and report results"""
    print(f"  → {description}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"    ❌ Failed!")
        print(f"    stdout: {result.stdout}")
        print(f"    stderr: {result.stderr}")
        return False
    print(f"    ✅ Success")
    return True

def main():
    print("=" * 60)
    print("🧪 Testing Season & Mission Creation (Headless Mode)")
    print("=" * 60)

    # Clean up any existing test season
    test_folder = "test_season_fake"
    if os.path.exists(test_folder):
        print(f"\n🧹 Cleaning up existing {test_folder}/")
        shutil.rmtree(test_folder)

    # Step 1: Create season
    print("\n📦 Step 1: Creating test season")
    season_cmd = [
        "python", "new_season.py",
        "--name", "Test Season Fake",
        "--team", "Fake Test Team",
        "--description", "A fake season for testing",
        "--left-wheel", "B",
        "--right-wheel", "C",
        "--left-attach", "A",
        "--right-attach", "D",
        "--left-sensor", "E",
        "--right-sensor", "F",
        "--wheel-diameter", "62",
        "--axle-track", "110",
        "--overwrite",
        "--quiet"
    ]

    if not run_command(season_cmd, "Creating season"):
        return 1

    # Verify season files exist
    required_files = [
        "season_config.py",
        "season_menu.py",
        "robot_controller.py",
        "display_patterns.py",
        "line_movements.py",
        "README.md"
    ]

    print("\n  📋 Verifying season files:")
    for file in required_files:
        file_path = os.path.join(test_folder, file)
        if os.path.exists(file_path):
            print(f"    ✅ {file}")
        else:
            print(f"    ❌ Missing: {file}")
            return 1

    # Step 2: Add Mission 1
    print("\n📦 Step 2: Adding Mission 1")
    mission1_cmd = [
        "python", "new_mission.py",
        "--season", test_folder,
        "--name", "Square Drive",
        "--description", "Drive in a square pattern",
        "--speed", "250",
        "--turn-rate", "80",
        "--template", "simple",
        "--quiet"
    ]

    if not run_command(mission1_cmd, "Creating mission 1"):
        return 1

    # Step 3: Add Mission 2
    print("\n📦 Step 3: Adding Mission 2")
    mission2_cmd = [
        "python", "new_mission.py",
        "--season", test_folder,
        "--name", "Line Following",
        "--description", "Follow a line using color sensors",
        "--speed", "150",
        "--turn-rate", "45",
        "--template", "guided",
        "--quiet"
    ]

    if not run_command(mission2_cmd, "Creating mission 2"):
        return 1

    # Step 4: Add Mission 3
    print("\n📦 Step 4: Adding Mission 3")
    mission3_cmd = [
        "python", "new_mission.py",
        "--season", test_folder,
        "--name", "Attachment Test",
        "--description", "Test attachment motors",
        "--speed", "300",
        "--turn-rate", "100",
        "--template", "guided",
        "--quiet"
    ]

    if not run_command(mission3_cmd, "Creating mission 3"):
        return 1

    # Verify mission files exist
    print("\n  📋 Verifying mission files:")
    expected_missions = [
        "mission_01_square_drive.py",
        "mission_02_line_following.py",
        "mission_03_attachment_test.py"
    ]

    for mission in expected_missions:
        mission_path = os.path.join(test_folder, mission)
        if os.path.exists(mission_path):
            print(f"    ✅ {mission}")
        else:
            print(f"    ❌ Missing: {mission}")
            return 1

    # Step 5: Verify season_menu.py was updated
    print("\n📋 Step 5: Verifying season_menu.py integration")
    menu_path = os.path.join(test_folder, "season_menu.py")
    with open(menu_path, "r") as f:
        menu_content = f.read()

    checks = [
        ("import mission_01_square_drive", "Mission 1 import"),
        ("import mission_02_line_following", "Mission 2 import"),
        ("import mission_03_attachment_test", "Mission 3 import"),
        ('"1":', "Mission 1 entry"),
        ('"2":', "Mission 2 entry"),
        ('"3":', "Mission 3 entry"),
        ('Square Drive', "Mission 1 name"),
        ('Line Following', "Mission 2 name"),
        ('Attachment Test', "Mission 3 name"),
    ]

    all_passed = True
    for check_str, description in checks:
        if check_str in menu_content:
            print(f"    ✅ {description}")
        else:
            print(f"    ❌ Missing: {description}")
            all_passed = False

    if not all_passed:
        return 1

    # Success!
    print("\n" + "=" * 60)
    print("🎉 All tests passed!")
    print("=" * 60)
    print(f"\n📁 Test season created: {test_folder}/")
    print("📝 Contains:")
    print("   • 1 season configuration")
    print("   • 3 test missions")
    print("   • Fully integrated menu system")
    print("\n💡 You can inspect the files or delete the folder when done.")
    print(f"   To delete: rm -rf {test_folder}/")
    print()

    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n  ❌ Cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
