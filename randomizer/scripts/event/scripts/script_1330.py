# pylint: disable=C0301

"""E1330_TOWER_EXTERIOR_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2811_ITS_LOCKED,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(),
    ]
)
