# pylint: disable=C0301

"""E0544_ROSE_TOWN_OCCUPIED_KID_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0816_TOLD_NOT_TO_GO_OUTSIDE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
