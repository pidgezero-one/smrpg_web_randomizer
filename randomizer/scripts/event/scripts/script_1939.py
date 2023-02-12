# E1939_KEEP_ROTATING_ROOM_CHEST_4

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNIVERSAL_CHEST_ANIMATION_BIT, ["EVENT_1939_inc_7"]),
        SetBit(UNIVERSAL_CHEST_ANIMATION_BIT),
        FreezeCamera(),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftNorthSteps(2),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        SetVarToConst(TIMER_701C, 40),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E1543_CHEST_CAMERA_SHIFT, timer_var=TIMER_701C
        ),
        ReactivateObject70A8TriggerIfMarioOnTopOfIt(),
        JmpToEvent(E0175_CHEST_4_CONTAINER, identifier="EVENT_1939_inc_7"),
        Return(),
    ]
)
