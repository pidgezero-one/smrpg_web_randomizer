# pylint: disable=C0301

"""E1137_SEASIDE_OCCUPIED_HEALTH_STORE_OCCUPANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
