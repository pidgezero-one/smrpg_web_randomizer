# pylint: disable=C0301

"""E3940_RIVER_BROOCH"""

from randomizer.scripts.event.script_imports import *
from randomizer.entities.items.items import Brooch

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2095_GOT_BROOCH,
            above_object=BOWSER,
            closable=False,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Inc(WEDDING_GEAR_COUNTER),
        AddToInventory(Brooch),
        Return(),
    ]
)
