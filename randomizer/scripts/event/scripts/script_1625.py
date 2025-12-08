# pylint: disable=C0301

"""E1625_MOLEVILLE_TOWER_UNLOCK_CONDITION_HINT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1163_BOOSTER_TOWER_DOOR_OPEN,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
