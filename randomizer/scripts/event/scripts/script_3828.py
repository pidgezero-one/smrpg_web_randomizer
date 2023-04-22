# pylint: disable=C0301

"""E3828_GRANT_ITEM_FLOWER_SOUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO085_FLOWER, channel=6),
        RunDialog(
            dialog_id=PRIMARY_TEMP_7000,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        AddToInventory(ITEM_ID),
        Return(),
    ]
)
