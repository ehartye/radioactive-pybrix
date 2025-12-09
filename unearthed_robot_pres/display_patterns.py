"""
Display Patterns
Common display patterns and utilities for robot screen display
"""

from pybricks.tools import wait
from pybricks.parameters import Icon
from season_config import SeasonDefaults


class DisplayPatterns:
    """Collection of display patterns for robot missions"""
    
    def __init__(self, hub, delay=None):
        """
        Initialize display patterns
        
        Args:
            hub: PrimeHub instance
            delay: Override default display delay (ms)
        """
        self.hub = hub
        self.delay = delay or SeasonDefaults.DISPLAY_DELAY
    
    def clear_display(self):
        """Clear the display"""
        self.hub.display.off()
    
    def show_icon(self, icon, duration=None):
        """Show a built-in icon for specified duration"""
        self.hub.display.icon(icon)
        if duration:
            wait(duration)
    
    def animate_square(self, cycles=3):
        """Animate a square pattern on the display"""
        patterns = [
            # Outer square
            [
                [100, 100, 100, 100, 100],
                [100, 0, 0, 0, 100],
                [100, 0, 0, 0, 100],
                [100, 0, 0, 0, 100],
                [100, 100, 100, 100, 100]
            ],
            # Inner square
            [
                [0, 0, 0, 0, 0],
                [0, 100, 100, 100, 0],
                [0, 100, 0, 100, 0],
                [0, 100, 100, 100, 0],
                [0, 0, 0, 0, 0]
            ],
            # Center dot
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 100, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        ]
        
        for cycle in range(cycles):
            for pattern in patterns:
                self.hub.display.icon(pattern)
                wait(self.delay)
        
        # End with square icon
        self.hub.display.icon(Icon.SQUARE)
    
    def animate_circle(self, cycles=3):
        """Animate a circle pattern on the display"""
        patterns = [
            # Outer circle
            [
                [0, 100, 100, 100, 0],
                [100, 0, 0, 0, 100],
                [100, 0, 0, 0, 100],
                [100, 0, 0, 0, 100],
                [0, 100, 100, 100, 0]
            ],
            # Inner circle
            [
                [0, 0, 0, 0, 0],
                [0, 100, 100, 100, 0],
                [0, 100, 0, 100, 0],
                [0, 100, 100, 100, 0],
                [0, 0, 0, 0, 0]
            ],
            # Center dot
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 100, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        ]
        
        for cycle in range(cycles):
            for pattern in patterns:
                self.hub.display.icon(pattern)
                wait(self.delay)
        
        # End with circle icon
        self.hub.display.icon(Icon.CIRCLE)
    
    def animate_triangle(self, cycles=3):
        """Animate a triangle pattern on the display"""
        patterns = [
            # Outer triangle
            [
                [0, 0, 100, 0, 0],
                [0, 100, 0, 100, 0],
                [100, 0, 0, 0, 100],
                [100, 100, 100, 100, 100],
                [0, 0, 0, 0, 0]
            ],
            # Inner triangle
            [
                [0, 0, 0, 0, 0],
                [0, 0, 100, 0, 0],
                [0, 100, 0, 100, 0],
                [0, 100, 100, 100, 0],
                [0, 0, 0, 0, 0]
            ],
            # Center dot
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 100, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
        ]
        
        for cycle in range(cycles):
            for pattern in patterns:
                self.hub.display.icon(pattern)
                wait(self.delay)
        
        # End with triangle icon
        self.hub.display.icon(Icon.TRIANGLE_UP)
    
    def show_progress_bar(self, percent):
        """
        Show progress bar on display
        
        Args:
            percent: Progress percentage (0-100)
        """
        filled_pixels = int((percent / 100) * 25)  # 5x5 = 25 pixels
        pattern = [[0 for _ in range(5)] for _ in range(5)]
        
        # Fill pixels row by row
        pixel_count = 0
        for row in range(5):
            for col in range(5):
                if pixel_count < filled_pixels:
                    pattern[row][col] = 100
                pixel_count += 1
        
        self.hub.display.icon(pattern)
    
    def show_countdown(self, seconds):
        """Show countdown on display"""
        for i in range(seconds, 0, -1):
            self.hub.display.number(i)
            wait(1000)
        
        # Show GO signal
        self.hub.display.icon(Icon.ARROW_RIGHT)
        wait(500)
    
    def show_completion_checkmark(self):
        """Show completion checkmark pattern"""
        checkmark = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 100],
            [0, 0, 0, 100, 0],
            [100, 0, 100, 0, 0],
            [0, 100, 0, 0, 0]
        ]
        
        self.hub.display.icon(checkmark)
        wait(1000)
    
    def show_error_x(self):
        """Show error X pattern"""
        error_x = [
            [100, 0, 0, 0, 100],
            [0, 100, 0, 100, 0],
            [0, 0, 100, 0, 0],
            [0, 100, 0, 100, 0],
            [100, 0, 0, 0, 100]
        ]
        
        self.hub.display.icon(error_x)
        wait(1000)
