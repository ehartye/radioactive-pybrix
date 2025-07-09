from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Icon

# Initialize the hub
hub = PrimeHub()

# Display a circle pattern sequence
patterns = [
    [
        [100, 100, 100, 100, 100],
        [100, 0, 0, 0, 100],
        [100, 0, 0, 0, 100],
        [100, 0, 0, 0, 100],
        [100, 100, 100, 100, 100]
    ],
    [
        [0, 100, 100, 100, 0],
        [100, 0, 0, 0, 100],
        [100, 0, 100, 0, 100],
        [100, 0, 0, 0, 100],
        [0, 100, 100, 100, 0]
    ],
    [
        [0, 0, 100, 0, 0],
        [0, 100, 0, 100, 0],
        [100, 0, 0, 0, 100],
        [0, 100, 0, 100, 0],
        [0, 0, 100, 0, 0]
    ]
]

# Show the circle pattern animation
for i in range(3):
    for pattern in patterns:
        hub.display.icon(pattern)
        wait(500)

# End with a simple circle icon
hub.display.icon(Icon.CIRCLE)
wait(2000)
hub.display.off()
