# pylint: disable=C0301

"""E3875_NIMBUS_UNUSED_DIALOG"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2388_FERTILIZER_LOCATION_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
