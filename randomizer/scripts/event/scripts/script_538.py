# pylint: disable=C0301

"""E0538_ROSE_TOWN_PINK_TOAD_IN_HOUSE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0875_MIDAS_CAVE_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
