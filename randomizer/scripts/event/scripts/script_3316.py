# pylint: disable=C0301

"""E3316_SHIP_BOSS_ROOM_LEFTMOST_HENCHMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
