# pylint: disable=C0301

"""E3934_GET_CROWN"""

from randomizer.scripts.event.script_imports import *
from randomizer.entities.items.items import Crown

script = EventScript(
    [
        PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
        RunDialog(
            dialog_id=DI2098_GOT_CROWN,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Inc(WEDDING_GEAR_COUNTER),
        AddToInventory(Crown),
        Return(),
    ]
)
