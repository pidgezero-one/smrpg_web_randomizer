# pylint: disable=C0301

"""E3942_RIVER_CROWN"""

from randomizer.scripts.event.script_imports import *
from randomizer.entities.items.items import Crown

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2098_GOT_CROWN,
            above_object=BOWSER,
            closable=False,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Inc(WEDDING_GEAR_COUNTER),
        AddToInventory(Crown),
        Return(),
    ]
)
