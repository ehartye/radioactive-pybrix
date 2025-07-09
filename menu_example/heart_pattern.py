from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Icon

# Initialize the hub
hub = PrimeHub()

# Display a heart pattern sequence
patterns = [
    [
        [0, 100, 0, 100, 0],
        [100, 100, 100, 100, 100],
        [100, 100, 100, 100, 100],
        [0, 100, 100, 100, 0],
        [0, 0, 100, 0, 0]
    ],
    [
        [0, 100, 0, 100, 0],
        [100, 0, 100, 0, 100],
        [100, 100, 100, 100, 100],
        [0, 100, 100, 100, 0],
        [0, 0, 100, 0, 0]
    ],
    [
        [0, 100, 0, 100, 0],
        [100, 0, 100, 0, 100],
        [100, 0, 100, 0, 100],
        [0, 100, 0, 100, 0],
        [0, 0, 100, 0, 0]
    ]
]

# Show the heart pattern animation
for i in range(2):
    for pattern in patterns:
        hub.display.icon(pattern)
        wait(600)

# End with a heart icon
hub.display.icon(Icon.HEART)
wait(2000)
hub.display.off()
