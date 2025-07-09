from pybricks.hubs import PrimeHub
from pybricks.tools import wait

# Initialize the hub
hub = PrimeHub()

# Display different arrow patterns
patterns = [
    # Arrow pointing up
    [
        [0, 0, 100, 0, 0],
        [0, 100, 100, 100, 0],
        [100, 0, 100, 0, 100],
        [0, 0, 100, 0, 0],
        [0, 0, 100, 0, 0]
    ],
    # Arrow pointing right
    [
        [0, 0, 100, 0, 0],
        [0, 0, 0, 100, 0],
        [100, 100, 100, 100, 100],
        [0, 0, 0, 100, 0],
        [0, 0, 100, 0, 0]
    ],
    # Arrow pointing down
    [
        [0, 0, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [100, 0, 100, 0, 100],
        [0, 100, 100, 100, 0],
        [0, 0, 100, 0, 0]
    ],
    # Arrow pointing left
    [
        [0, 0, 100, 0, 0],
        [0, 100, 0, 0, 0],
        [100, 100, 100, 100, 100],
        [0, 100, 0, 0, 0],
        [0, 0, 100, 0, 0]
    ]
]

# Show the arrow rotation animation
for i in range(3):
    for pattern in patterns:
        hub.display.icon(pattern)
        wait(700)

# End with a final up arrow
hub.display.icon(patterns[0])
wait(2000)
hub.display.off()
