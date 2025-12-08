# pylint: disable=C0301

"""E3873_NIMBUS_CASTLE_5_DOOR_ROOM_RIGHT_GUARD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2386_NIMBUS_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
