# E0269_PIPE_UP_SUBROUTINE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=MARIO,
            subscript=[ASClearSolidityBits(cant_pass_walls=True), ASAddZCoord1Step()],
        ),
        FadeInFromBlack(sync=False),
        RememberLastObject(),
        ActionQueueAsync(
            target=MARIO, subscript=[ASSetSolidityBits(cant_pass_walls=True)]
        ),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ClearBit(TEMP_707C_0),
        Return(),
    ]
)
