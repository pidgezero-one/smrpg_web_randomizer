# pylint: disable=C0301

"""E3649_NIMBUS_OCCUPIED_NORTHEAST_HOUSE_LEFT_WOMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI3590_DUPE_BOSSES_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
