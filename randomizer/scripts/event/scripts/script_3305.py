# pylint: disable=C0301

"""E3305_SHIP_2ND_GREAPER_ROOM_HINT_NOTE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1676_SHIP_GREAPER_2_NOTE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
