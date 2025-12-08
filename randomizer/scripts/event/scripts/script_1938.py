# pylint: disable=C0301

"""E1938_KEEP_ROTATING_ROOM_CHEST_3"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNIVERSAL_CHEST_ANIMATION_BIT, ["EVENT_1938_inc_7"]),
        SetBit(UNIVERSAL_CHEST_ANIMATION_BIT),
        FreezeCamera(),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftNorthSteps(2),
                ASSetWalkingSpeed(NORMAL),
            ]),
        SetVarToConst(TIMER_701C, 40),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E1543_CHEST_CAMERA_SHIFT, timer_var=TIMER_701C
        ),
        ReactivateObject70A8TriggerIfMarioOnTopOfIt(),
        JmpToEvent(E0174_CHEST_3_CONTAINER, identifier="EVENT_1938_inc_7"),
        Return(),
    ]
)
