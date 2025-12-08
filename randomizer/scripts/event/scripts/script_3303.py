# pylint: disable=C0301

"""E3303_SHIP_1ST_SAVE_ROOM_HINT_NOTE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1674_SHIP_SAVEROOM_NOTE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
