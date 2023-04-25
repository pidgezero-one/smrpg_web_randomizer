# pylint: disable=C0301

"""E3827_GRANT_ITEM_STANDARD_SOUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
        RunDialog(
            dialog_id=PRIMARY_TEMP_7000,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        AddToInventory(ITEM_ID),
        Return(),
    ]
)
