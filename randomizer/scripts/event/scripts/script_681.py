# pylint: disable=C0301

"""E0681_MARRYMORE_LIBERATED_EXTERIOR_KID"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseActionScript(NPC_8),
        ActionQueueAsync(
            target=NPC_8, subscript=[ASClearSolidityBits(cant_walk_through=True)]
        ),
        Pause(1, identifier="EVENT_681_pause_2"),
        JmpIfObjectInAir(NPC_8, ["EVENT_681_pause_2"]),
        RunDialog(
            dialog_id=DI2198_MARRYMORE_PHOTO,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ActionQueueAsync(
            target=NPC_8, subscript=[ASSetSolidityBits(cant_walk_through=True)]
        ),
        ResumeActionScript(NPC_8),
        Return(),
    ]
)
