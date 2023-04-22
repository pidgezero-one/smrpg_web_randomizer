# pylint: disable=C0301

"""E0270_TRAMPOLINE_OR_PIPE_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASAddZCoord1Step(),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        Return(),
    ]
)
