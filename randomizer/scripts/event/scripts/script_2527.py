# pylint: disable=C0301

"""E2527_STAR_HILL_1ST_ROOM_WISH_IN_FRONT_OF_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO110_ABSTRACT_MUSIC, channel=6),
        RunDialog(
            dialog_id=DI3325_WISH_11,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        PlaySound(sound=SO000_SILENCE, channel=6),
        Return(),
    ]
)
