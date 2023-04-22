# pylint: disable=C0301

"""E3242_SHIP_3D_MAZE_HINT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopAllBackgroundEvents(),
        SetSyncActionScript(MEM_70A8, A0340_SHIP_PUZZLE_HINT_VANISH),
        RunDialog(
            dialog_id=DI1666_MAZE_PUZZLE_HINT,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        RunBackgroundEvent(
            event_id=E3212_SHIP_3D_MAZE_FORFEIT_LISTENER, return_on_level_exit=True
        ),
        RunDialog(
            dialog_id=DI1657_3D_MAZE_OVERLAY,
            above_object=Bowser,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
        ),
        Return(),
    ]
)
