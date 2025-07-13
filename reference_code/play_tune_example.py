from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub()

# Define the notes for the Star Wars theme
star_wars_theme = [
    "G4/4", "G4/4", "G4/4", "C5/2", "G5/2",
    "F5/4", "E5/4", "D5/4", "C6/2", "G5/2",
    "F5/4", "E5/4", "D5/4", "C6/2", "G5/2",
    "F5/4", "E5/4", "F5/4", "D5/2",
]

# Define the notes for the Cantina Band theme
hub.speaker.play_notes(star_wars_theme, tempo=180)

# Wait for the song to finish before exiting
wait(2000)
