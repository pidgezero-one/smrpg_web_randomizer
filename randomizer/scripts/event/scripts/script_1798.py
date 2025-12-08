# pylint: disable=C0301

"""E1798_LANDS_END_CLIFF_MOUSE_HINT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialogForDuration(
            dialog_id=DI1234_MONSTRO_MOUSE_TEMPLE_HINT, duration=1, sync=False
        ),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASJumpToHeight(108),
                ASShiftSouthSteps(4),
                ASWalkSouthwestSteps(3),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ]),
        Return(),
    ]
)
