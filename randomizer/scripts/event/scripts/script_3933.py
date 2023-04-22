# pylint: disable=C0301

"""E3933_GET_RING"""

from randomizer.scripts.event.script_imports import *
from randomizer.entities.items.items import Ring

script = EventScript(
    [
        PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
        RunDialog(
            dialog_id=DI2097_GOT_RING,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Inc(WEDDING_GEAR_COUNTER),
        AddToInventory(Ring),
        Return(),
    ]
)
