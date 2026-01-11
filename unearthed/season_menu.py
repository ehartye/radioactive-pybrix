"""
import mission_03_drive_test
import mission_04_warm_up
Season Menu System
Main menu for selecting and running season missions
"""

from pybricks.tools import hub_menu
from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

# Import all mission modules (flat structure for PyBricks compatibility)
import launch_01_surface_brushing
import launch_02_ship_wreck
import launch_03_whats_on_scale
import launch_04_silo
import launch_05_heavy_lifting
import mission_04_warm_up
from season_config import SeasonInfo, SeasonDefaults

class SeasonMenu:
    """Main season menu controller"""

    def __init__(self):
        self.hub = PrimeHub()
        self.missions = {
            "1": {
                "name": "Surface Brushing",
                "description": "Missions 01, 02, and 14",
                "run_function": launch_01_surface_brushing
            },
            "2": {
                "name": "Ship Wreck",
                "description": "Misions 12 and 15",
                "run_function": launch_02_ship_wreck
            },
            "3": {
                "name": "What's On Scale",
                "description": "Missions 09, 10, and 03",
                "run_function": launch_03_whats_on_scale
            },
            "4": {
                "name": "Silo",
                "description": "Missions 08, 05, 06",
                "run_function": launch_04_silo
            },
            "5": {
                "name": "Heavy Lifting",
                "description": "Mission 07",
                "run_function": launch_05_heavy_lifting
            },
            "6": {
                "name": "warm_up",
                "description": "Prepares robot for first run by warming up motors",
                "run_function": mission_04_warm_up
            }
        }

    def show_welcome(self):
        """Display welcome message and season info"""
        print("=" * 50)
        print(f"Welcome to {SeasonInfo.NAME}")
        print(f"Team: {SeasonInfo.TEAM}")
        print(f"Description: {SeasonInfo.DESCRIPTION}")
        print("=" * 50)

        # Ava deleted a welcoming thingy here because it was taking too much

    def show_mission_list(self):
        """Display available missions"""
        print("\nAvailable Missions:")
        print("-" * 30)
        for key, mission in sorted(self.missions.items()):
            print(f"{key}. {mission['name']}")
            print(f"   {mission['description']}")
        print("Q. Quit")
        print("-" * 30)

    def run_mission(self, mission_key):
        """
        Run a specific mission

        Args:
            mission_key: Key of the mission to run
        """
        if mission_key in self.missions:
            mission = self.missions[mission_key]

            print(f"\n=== Starting Mission {mission_key}: {mission['name']} ===")
            print(f"Description: {mission['description']}")

            # Show mission number on display
            self.hub.display.number(int(mission_key))
            wait(1000)

            # Import required classes for mission execution
            from robot_controller import RobotController
            from display_patterns import DisplayPatterns

            # Get mission config (if the mission defines one)
            mission_module = mission["run_function"]
            mission_config = getattr(mission_module, 'MISSION_CONFIG', {})

            # Initialize robot with mission-specific config
            robot = RobotController(SeasonDefaults, mission_config)

            try:
                # Initialize robot hardware
                robot.initialize()

                # Create display helper
                display = DisplayPatterns(robot.hub)

                # Signal mission start
                robot.mission_start_signal()

                # Execute the mission (pass initialized robot and display)
                mission["run_function"].run(robot, display)

                # Success feedback
                robot.mission_success_signal()
                print(f"Mission {mission_key} completed successfully!")

            except Exception as e:
                # Error feedback
                print(f"Mission {mission_key} failed: {e}")
                robot.mission_error_signal()

                # Show error on display
                from display_patterns import DisplayPatterns
                display = DisplayPatterns(robot.hub)
                display.show_error_x()

            finally:
                # Always clean up robot state
                robot.cleanup()

                # Brief pause before returning to menu
                wait(2000)
                self.hub.light.off()
                self.hub.display.off()
        else:
            print(f"Invalid mission: {mission_key}")
            self.hub.speaker.beep(300, 100)

    def main_loop(self):
        """Main menu loop"""
        self.show_welcome()

        while True:
            self.show_mission_list()

            # Get user selection
            print(f"\nSelect mission (1-5) or Q to quit:")
            selected = hub_menu("1", "2", "3", "4", "4", "5", "Q")

            if selected == "Q":
                print("\nExiting season menu...")
                self.hub.display.text("BYE")
                wait(1000)
                self.hub.display.off()
                self.hub.light.off()
                break
            else:
                self.run_mission(selected)

def main():
    """Main function to start the season menu"""
    try:
        menu = SeasonMenu()
        menu.main_loop()
    except Exception as e:
        print(f"Season menu error: {e}")
        # Emergency cleanup
        hub = PrimeHub()
        hub.light.on(Color.RED)
        hub.speaker.beep(200, 1000)
        hub.display.text("ERR")
        wait(2000)
        hub.display.off()
        hub.light.off()

# Allow direct execution
if __name__ == "__main__":
    main()
