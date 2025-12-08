# pylint: disable=C0301

"""E1546_LANDS_END_FIRST_TWO_CHESTS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNIVERSAL_CHEST_ANIMATION_BIT, ["EVENT_1546_ret_11"]),
        SetBit(UNIVERSAL_CHEST_ANIMATION_BIT),
        FreezeCamera(),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftNorthSteps(2),
                ASSetWalkingSpeed(NORMAL),
            ]),
        SetVarToConst(TIMER_701C, 40),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E1543_CHEST_CAMERA_SHIFT, timer_var=TIMER_701C
        ),
        JmpToEvent(E0172_CHEST_1_CONTAINER, identifier="EVENT_1546_ret_11"),
    ]
)
