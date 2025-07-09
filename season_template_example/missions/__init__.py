"""
Mission modules for the season
Each mission is a self-contained module with a run() function
"""

# Import mission modules so they can be accessed via missions.mission_name
from missions.mission_01_square_drive import run as mission_01_square_drive
from missions.mission_02_circle_drive import run as mission_02_circle_drive
from missions.mission_03_square_display import run as mission_03_square_display
from missions.mission_04_triangle_combo import run as mission_04_triangle_combo

__all__ = [
    'mission_01_square_drive',
    'mission_02_circle_drive', 
    'mission_03_square_display',
    'mission_04_triangle_combo'
]
