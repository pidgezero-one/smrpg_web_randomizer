# pylint: disable=C0301

"""E0566_ROSE_TOWN_LIBERATED_GRANDPA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0862_PROUD_OF_GRANDSONS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
