# pylint: disable=C0301

"""E0516_OCCUPIED_ROSE_TOWN_GAZ"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0779_GAZ,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
