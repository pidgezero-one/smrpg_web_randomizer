# pylint: disable=C0301

"""E0739_NIMBUS_LAND_INN_HINT_GUY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1054_SUNKEN_SHIP_HINT,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        Return(),
    ]
)
