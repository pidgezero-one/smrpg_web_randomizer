# pylint: disable=C0301

"""E3939_RIVER_SHOES"""

from randomizer.scripts.event.script_imports import *
from randomizer.entities.items.items import Shoes

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2096_GOT_SHOES,
            above_object=BOWSER,
            closable=False,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        AddToInventory(Shoes),
        Inc(WEDDING_GEAR_COUNTER),
        Return(),
    ]
)
