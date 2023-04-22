# pylint: disable=C0301

"""E3653_NIMBUS_SOUTH_HOUSE_GUY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI3589_TOWER_CREVICE_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
