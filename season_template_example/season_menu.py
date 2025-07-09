"""
Season Menu System
Main menu for selecting and running season missions
"""

from pybricks.tools import hub_menu
from pybricks.hubs import PrimeHub
from pybricks.parameters import Color
from pybricks.tools import wait

# import missions  # Import all missions package
from missions import mission_01_square_drive
from missions import mission_02_circle_drive
from missions import mission_03_square_display
from missions import mission_04_triangle_combo
from season_config import SeasonInfo, SeasonDefaults

class SeasonMenu:
    """Main season menu controller"""
    
    def __init__(self):
        self.hub = PrimeHub()
        self.missions = {
            "1": {
                "name": "Square Drive",
                "description": "Drive robot in square pattern",
                "run_function": mission_01_square_drive
            },
            "2": {
                "name": "Circle Drive", 
                "description": "Drive robot in circle pattern",
                "run_function": mission_02_circle_drive
            },
            "3": {
                "name": "Square Display",
                "description": "Display square pattern on screen",
                "run_function": mission_03_square_display
            },
            "4": {
                "name": "Triangle Combo",
                "description": "Drive triangle while displaying pattern",
                "run_function": mission_04_triangle_combo
            }
        }
    
    def show_welcome(self):
        """Display welcome message and season info"""
        print("=" * 50)
        print(f"Welcome to {SeasonInfo.NAME}")
        print(f"Version: {SeasonInfo.VERSION}")
        print(f"Description: {SeasonInfo.DESCRIPTION}")
        print("=" * 50)
        
        # Show welcome on display
        self.hub.light.on(Color.BLUE)
        self.hub.display.text("SEASON")
        wait(2000)
        self.hub.display.off()
    
    def show_mission_list(self):
        """Display available missions"""
        print("\nAvailable Missions:")
        print("-" * 30)
        for key, mission in self.missions.items():
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
            
            try:
                # Execute the mission
                mission["run_function"]()
                
                # Success feedback
                print(f"Mission {mission_key} completed successfully!")
                self.hub.light.on(SeasonDefaults.MISSION_SUCCESS_COLOR)
                self.hub.speaker.beep(800, 200)
                
            except Exception as e:
                # Error feedback
                print(f"Mission {mission_key} failed: {e}")
                self.hub.light.on(SeasonDefaults.MISSION_ERROR_COLOR)
                self.hub.speaker.beep(200, 500)
                
                # Ask if user wants to retry
                print("Press center button to retry, or continue to menu...")
                # Note: In a real implementation, you might want to add button handling here
                
            finally:
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
            
            # Show menu on display
            self.hub.display.text("MENU")
            
            # Get user selection
            print("\nSelect mission (1-4) or Q to quit:")
            selected = hub_menu("1", "2", "3", "4", "Q")
            
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

def run_quick_demo():
    """
    Run a quick demonstration of all missions
    Useful for testing or showing off the season
    """
    print("=== Quick Demo: All Missions ===")
    
    hub = PrimeHub()
    hub.light.on(Color.YELLOW)
    hub.display.text("DEMO")
    wait(2000)
    
    missions = [
        ("Mission 1", missions.mission_01_square_drive.run),
        ("Mission 2", missions.mission_02_circle_drive.run),
        ("Mission 3", missions.mission_03_square_display.run),
        ("Mission 4", missions.mission_04_triangle_combo.run)
    ]
    
    for i, (name, run_func) in enumerate(missions):
        print(f"\n--- Demo {i+1}/4: {name} ---")
        hub.display.number(i+1)
        wait(1000)
        
        try:
            run_func()
            print(f"{name} demo completed")
        except Exception as e:
            print(f"{name} demo failed: {e}")
        
        # Brief pause between missions
        if i < len(missions) - 1:
            wait(2000)
    
    print("\n=== Demo Complete ===")
    hub.display.text("DONE")
    hub.light.on(Color.GREEN)
    wait(2000)
    hub.display.off()
    hub.light.off()

def run_custom_sequence():
    """
    Run a custom sequence of missions
    Example of how to create mission sequences
    """
    print("=== Custom Sequence: Shape Showcase ===")
    
    hub = PrimeHub()
    hub.light.on(Color.MAGENTA)
    hub.display.text("SEQ")
    wait(2000)
    
    # Custom sequence: display first, then drive
    sequence = [
        ("Square Display", missions.mission_03_square_display.run),
        ("Square Drive", missions.mission_01_square_drive.run),
        ("Circle Drive", missions.mission_02_circle_drive.run),
        ("Triangle Combo", missions.mission_04_triangle_combo.run)
    ]
    
    for i, (name, run_func) in enumerate(sequence):
        print(f"\n--- Sequence {i+1}/4: {name} ---")
        
        # Show progress
        hub.display.number(i+1)
        wait(1000)
        
        try:
            run_func()
            print(f"{name} sequence completed")
        except Exception as e:
            print(f"{name} sequence failed: {e}")
            # Continue with next mission even if one fails
        
        # Brief pause between missions
        if i < len(sequence) - 1:
            wait(1500)
    
    print("\n=== Custom Sequence Complete ===")
    hub.display.text("DONE")
    hub.light.on(Color.GREEN)
    wait(2000)
    hub.display.off()
    hub.light.off()

# Allow direct execution
if __name__ == "__main__":
    main()
