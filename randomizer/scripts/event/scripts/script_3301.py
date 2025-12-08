# pylint: disable=C0301

"""E3301_SHIP_BOSS_ROOM_INNER_LEFT_HENCHMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
