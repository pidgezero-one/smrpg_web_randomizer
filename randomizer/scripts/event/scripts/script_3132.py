# pylint: disable=C0301

"""E3132_MOLEVILLE_MINERS_SONG"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(PRIMARY_TEMP_7000, 1607),
        StartLoopNTimes(7),
        RunDialog(
            dialog_id=PRIMARY_TEMP_7000,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        ActionQueueSync(
            target=NPC_2, subscript=[ASJumpToHeight(height=64, silent=True)]
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[ASPause(10), ASJumpToHeight(height=64, silent=True)]),
        ActionQueueSync(
            target=NPC_4,
            subscript=[ASPause(20), ASJumpToHeight(height=64, silent=True)]),
        ActionQueueSync(
            target=NPC_5,
            subscript=[ASPause(30), ASJumpToHeight(height=64, silent=True)]),
        Inc(PRIMARY_TEMP_7000),
        EndLoop(),
        RunDialog(
            dialog_id=DI1615_MOLEVILLE_BLUES_8,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Return(),
    ]
)
