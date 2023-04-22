# pylint: disable=C0301

"""E3648_NIMBUS_OCCUPIED_NORTHEAST_HOUSE_RIGHT_GUY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2467_GARRO_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
