from pybricks.tools import hub_menu

# Make a menu to choose a pattern. Use letters for easy identification.
selected = hub_menu("C", "H", "S", "A")

# Based on the selection, run a pattern program.
if selected == "C":
    import circle_pattern
elif selected == "H":
    import heart_pattern
elif selected == "S":
    import spiral_pattern
elif selected == "A":
    import arrow_pattern
