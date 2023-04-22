# pylint: disable=C0301

"""E1929_KEEP_INVISIBLE_FLOOR_COIN_4"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PrioritySet(
            mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES],
            subscreen=[LAYER_L3],
            colour_math=[LAYER_L1, LAYER_L2, NPC_SPRITES, HALF_INTENSITY],
        ),
        SetVarToConst(TIMER_701E, 8),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E1843_KEEP_INVISIBLE_FLOOR_SHOW_FLOOR, timer_var=TIMER_701E
        ),
        JmpToEvent(E0238_FREESTANDING_4_GRANT),
    ]
)
