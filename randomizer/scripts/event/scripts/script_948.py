# pylint: disable=C0301

"""E0948_FROGFUCIUS_HINT_EXPANSION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2758_FROGFUCIUS_DEFAULT_STUFF,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
