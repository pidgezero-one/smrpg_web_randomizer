# pylint: disable=C0301

"""E3150_ROSE_WAY_SWING_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftNorthSteps(2),
                ASShiftSouthSteps(2),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        JmpToEvent(E0172_CHEST_1_CONTAINER),
    ]
)
