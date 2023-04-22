# pylint: disable=C0301

"""E0655_MARRYMORE_GEAR_GRANT_CROWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
        RemoveObjectFromCurrentLevel(NPC_5),
        RunDialog(
            dialog_id=DI2098_GOT_CROWN,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Inc(WEDDING_GEAR_COUNTER),
        Return(),
    ]
)
