# pylint: disable=C0301

"""E0542_ROSE_TOWN_OCCUPIED_GRANDMA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0818_KIDS_ARE_SAFE_INDOORS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
