# pylint: disable=C0301

"""E3941_RIVER_RING"""

from randomizer.scripts.event.script_imports import *
from randomizer.entities.items.items import Ring

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2097_GOT_RING,
            above_object=BOWSER,
            closable=False,
            sync=False,
            multiline=False,
            use_background=False),
        Inc(WEDDING_GEAR_COUNTER),
        AddToInventory(Ring),
        Return(),
    ]
)
