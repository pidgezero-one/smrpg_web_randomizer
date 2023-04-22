# pylint: disable=C0301

"""E0345_MUSHROOM_KINGDOM_TOADSTOOLS_ROOM_GUARD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2320_TOADSTOOL_ROOM_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
