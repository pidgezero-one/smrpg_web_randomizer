# E3391_VOLCANO_1ST_SAVE_ROOM_LOWER_CHEST

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
