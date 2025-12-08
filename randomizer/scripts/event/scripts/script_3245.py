# pylint: disable=C0301

"""E3245_SHIP_BARREL_PUZZLE_HINT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetSyncActionScript(MEM_70A8, A0340_SHIP_PUZZLE_HINT_VANISH),
        RunDialog(
            dialog_id=DI1669_BARREL_PUZZLE_HINT,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Return(),
    ]
)
