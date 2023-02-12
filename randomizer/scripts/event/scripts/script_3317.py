# E3317_MINES_FINAL_CHEST

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
        JmpToEvent(E0173_CHEST_2_CONTAINER),
    ]
)
