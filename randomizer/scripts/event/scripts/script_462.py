# pylint: disable=C0301

"""E0462_YOSHI_MOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO063_YOSHI_TALK, channel=6),
        JmpIfBitClear(TEMP_7044_5, ["EVENT_462_enable_controls_until_return_7"]),
        RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI),
        JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["EVENT_471_run_event_as_subroutine_19"]),
        RunDialog(
            dialog_id=DI0921_BABY_YOSHI_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        RunBackgroundEvent(
            event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, bit_7=True
        ),
        Return(),
        EnableControlsUntilReturn(
            [LEFT, RIGHT, DOWN, UP, A, Y, B],
            identifier="EVENT_462_enable_controls_until_return_7"),
        Pause(32),
        Return(),
        JmpToEvent(
            E0931_INITATIE_YOSHI_RACE_FOR_GAMBLING,
            identifier="EVENT_462_jmp_to_event_10"),
    ]
)
