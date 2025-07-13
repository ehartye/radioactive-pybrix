# Menu Example - Multi-File Robot Pattern Display

This is a simple multi-file project that demonstrates how to use the Pybricks menu system to select between different display patterns on a SPIKE Prime or MINDSTORMS Robot Inventor hub.

## Files Overview

- `menu.py` - Main menu program that provides pattern selection
- `circle_pattern.py` - Displays animated circle patterns
- `heart_pattern.py` - Displays animated heart patterns  
- `spiral_pattern.py` - Displays an animated spiral filling pattern
- `arrow_pattern.py` - Displays rotating arrow patterns

## How to Use

1. **Download all files to your robot hub** by running the `menu.py` program. This will automatically download all the pattern files as well due to the import statements.

2. **Run the menu program** - When you start `menu.py`, you'll see a letter on the hub display:
   - **C** - Circle pattern
   - **H** - Heart pattern
   - **S** - Spiral pattern
   - **A** - Arrow pattern

3. **Navigate the menu**:
   - Use the **left and right buttons** to cycle through the pattern options
   - Press the **center button** to select and run a pattern
   - Press the **start button** to return to the menu after a pattern finishes

## Pattern Descriptions

### Circle Pattern (C)
- Displays three different circular patterns in sequence
- Animates through filled circle, circle with center dot, and sparse circle
- Ends with the built-in circle icon

### Heart Pattern (H)
- Shows an animated heart shape with different fill patterns
- Cycles through solid heart, heart with holes, and outline heart
- Ends with the built-in heart icon

### Spiral Pattern (S)
- Creates an animated spiral that fills the display from outside to inside
- Shows a smooth progression of pixels lighting up in a spiral pattern
- Demonstrates more complex animation sequences

### Arrow Pattern (A)
- Displays arrows pointing in four directions: up, right, down, left
- Rotates through all directions in a continuous cycle
- Ends with an upward-pointing arrow

## Technical Notes

- All patterns use the 5x5 LED matrix of the hub display
- Pixel values: 0 = off, 100 = full brightness
- Each pattern is self-contained and can be run independently for testing
- The menu system follows the Pybricks multi-program approach using import statements
- Uses `hub.display.icon()` method to display custom pixel patterns

## Testing Individual Patterns

You can test each pattern individually by running them directly:
- Run `circle_pattern.py` to test the circle animation
- Run `heart_pattern.py` to test the heart animation
- Run `spiral_pattern.py` to test the spiral animation
- Run `arrow_pattern.py` to test the arrow animation

Remember to download the `menu.py` program again after testing to ensure all files are available on the hub.
