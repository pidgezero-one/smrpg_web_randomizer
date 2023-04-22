# pylint: disable=C0301

"""E2533_STAR_HILL_2ND_ROOM_WISH_IN_FRONT_OF_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO110_ABSTRACT_MUSIC, channel=6),
        RunDialog(
            dialog_id=DI3108_WISH_4,
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
