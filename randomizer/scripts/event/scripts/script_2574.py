# pylint: disable=C0301

"""E2574_TOWER_FIRST_STAIRCASE_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7042_0),
        FreezeCamera(),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftZUpSteps(2),
                ASSetWalkingSpeed(NORMAL),
                ASShiftZDownSteps(2),
                ASClearBit(TEMP_7042_0),
            ]),
        UnfreezeCamera(),
        JmpToEvent(E0172_CHEST_1_CONTAINER),
    ]
)
