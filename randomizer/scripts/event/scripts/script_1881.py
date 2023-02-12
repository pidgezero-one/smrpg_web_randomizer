# E1881_KEEP_INVISIBLE_FLOOR_COIN_2

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PrioritySet(
            mainscreen=[LAYER_1, LAYER_2, NPC_SPRITES],
            subscreen=[LAYER_3],
            colour_math=[LAYER_1, LAYER_2, NPC_SPRITES, HALF_INTENSITY],
        ),
        SetVarToConst(TIMER_701E, 8),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E1843_KEEP_INVISIBLE_FLOOR_SHOW_FLOOR, timer_var=TIMER_701E
        ),
        JmpToEvent(E0240_FREESTANDING_2_GRANT),
    ]
)
