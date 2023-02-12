# E1543_CHEST_CAMERA_SHIFT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftSouthSteps(2),
                ASSetWalkingSpeed(NORMAL),
                ASClearBit(UNIVERSAL_CHEST_ANIMATION_BIT),
            ],
        ),
        UnfreezeCamera(),
        Return(),
    ]
)
