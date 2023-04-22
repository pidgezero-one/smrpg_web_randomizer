# pylint: disable=C0301

"""E2530_STAR_HILL_1ST_ROOM_WISH_BOTTOM_RIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO110_ABSTRACT_MUSIC, channel=6),
        JmpIfBitSet(UNKNOWN_709A_0, ["EVENT_2530_run_dialog_5"]),
        RunDialog(
            dialog_id=DI3106_WISH_2,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        PlaySound(sound=SO000_SILENCE, channel=6),
        Return(),
        RunDialog(
            dialog_id=DI3275_CONVERTED_WISH,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_2530_run_dialog_5",
        ),
        PlaySound(sound=SO000_SILENCE, channel=6),
        Return(),
    ]
)
