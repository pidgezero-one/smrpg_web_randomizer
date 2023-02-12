# E1914_ABYSS_MACHINE_ARROW_RESET

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MARIO, subscript=[ASSequenceLoopingOff(), ASResetProperties()]
        ),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ClearBit(TEMP_7043_1),
        Return(),
    ]
)
