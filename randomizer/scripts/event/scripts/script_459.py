# pylint: disable=C0301

"""E0459_UPPER_RIGHT_YOSHI"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO063_YOSHI_TALK, channel=6),
        JmpIfBitClear(TEMP_7044_5, ["EVENT_459_enable_controls_until_return_7"]),
        RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI),
        RunDialog(
            dialog_id=DI0901_YOSHI_RACE_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        RunBackgroundEvent(
            event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, bit_7=True
        ),
        Return(),
        EnableControlsUntilReturn(
            [LEFT, RIGHT, DOWN, UP, A, Y, B],
            identifier="EVENT_459_enable_controls_until_return_7",
        ),
        Pause(32),
        Return(),
    ]
)
