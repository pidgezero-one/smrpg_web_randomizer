# pylint: disable=C0301

"""E1971_MUSHROOM_BOY_GRANTS_ROCK_CANDY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO085_FLOWER, channel=6),
        RunDialog(
            dialog_id=DI2938_RECEIVED_ROCK_CANDY,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        AddToInventory(RockCandy),
        Return(),
    ]
)
