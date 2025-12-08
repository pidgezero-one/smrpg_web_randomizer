# pylint: disable=C0301

"""E0524_ROSE_TOWN_OCCUPIED_EXTERIOR_GRANDPA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0789_WATER_PUMP_OCCUPIED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
