# pylint: disable=C0301

"""E3354_KEEP_BARREL_COUNT_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(ACTIVE_NPC, 22),
        StartLoopNTimes(7),
        RemoveObjectFromCurrentLevel(MEM_70A8),
        Inc(ACTIVE_NPC),
        EndLoop(),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalkToXYCoords(x=6, y=49),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        JmpToEvent(E3355_KEEP_BARREL_COUNT_LOADER_CONTD),
        Return(),
    ]
)
