# pylint: disable=C0301

"""E2532_STAR_HILL_2ND_ROOM_WISH_BOTTOM_LEFT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO110_ABSTRACT_MUSIC, channel=6),
        RunDialog(
            dialog_id=DI3111_WISH_7,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        PlaySound(sound=SO000_SILENCE, channel=6),
        Return(),
    ]
)
