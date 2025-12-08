# pylint: disable=C0301

"""E3872_NIMBUS_CASTLE_5_DOOR_ROOM_LEFT_GUARD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2385_NIMBUS_BOSS_2_IS_STILL_THERE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
