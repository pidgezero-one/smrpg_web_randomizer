# pylint: disable=C0301

"""E0554_ROSE_TOWN_OCCUPIED_EXTERIOR_YELLOW_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0813_CANT_MOVE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
