# E2604_ABYSS_CHEST_BEFORE_1ST_BOSS

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftNorthSteps(2),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        JmpToEvent(E0172_CHEST_1_CONTAINER),
        Return(),
    ]
)
