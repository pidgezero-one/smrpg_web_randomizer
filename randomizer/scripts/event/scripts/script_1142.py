# pylint: disable=C0301

"""E1142_SEASIDE_SHED_GUARD_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
