# pylint: disable=C0301

"""E1866_KEEP_INVISIBLE_FLOOR_CHEST_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNIVERSAL_CHEST_ANIMATION_BIT, ["EVENT_1866_inc_7"]),
        SetBit(UNIVERSAL_CHEST_ANIMATION_BIT),
        PrioritySet(
            mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES],
            subscreen=[LAYER_L3],
            colour_math=[LAYER_L1, LAYER_L2, NPC_SPRITES, HALF_INTENSITY],
        ),
        SetVarToConst(TIMER_701E, 8),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E1843_KEEP_INVISIBLE_FLOOR_SHOW_FLOOR, timer_var=TIMER_701E
        ),
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
        JmpToEvent(E0173_CHEST_2_CONTAINER, identifier="EVENT_1866_inc_7"),
        Return(),
    ]
)
