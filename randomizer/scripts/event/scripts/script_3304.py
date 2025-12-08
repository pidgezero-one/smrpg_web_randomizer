# pylint: disable=C0301

"""E3304_SHIP_1ST_GREAPER_ROOM_HINT_NOTE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1675_SHIP_GREAPER_1_NOTE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
