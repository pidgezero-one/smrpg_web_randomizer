# pylint: disable=C0301

"""E0471_BOSHI"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO062_BIG_YOSHI_TALK, channel=6),
        JmpIfBitClear(TEMP_7044_5, ["EVENT_471_enable_controls_until_return_12"]),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_471_run_event_as_subroutine_15"]),
        JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["EVENT_462_jmp_to_event_10"]),
        JmpIfBitSet(GOT_FREE_COOKIES, ["EVENT_471_run_event_as_subroutine_9"]),
        RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI),
        RunDialog(
            dialog_id=DI0906_BOSHI_BEFORE_YOU_BEAT_HIM,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        RunBackgroundEvent(
            event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, bit_7=True
        ),
        Return(),
        RunEventAsSubroutine(
            E0456_YOSHI_TALKS_TO_OTHER_YOSHI,
            identifier="EVENT_471_run_event_as_subroutine_9"),
        JmpToEvent(E0476_INITIATE_MUSHROOM_DERBY_FROM_TALKING_TO_BOSHI),
        EnableControlsUntilReturn(
            [LEFT, RIGHT, DOWN, UP, A, Y, B],
            identifier="EVENT_471_enable_controls_until_return_12"),
        Pause(32),
        Return(),
        RunEventAsSubroutine(
            E0456_YOSHI_TALKS_TO_OTHER_YOSHI,
            identifier="EVENT_471_run_event_as_subroutine_15"),
        RunDialog(
            dialog_id=DI0946_LETS_RACE_AGAIN_SOMETIME,
            above_object=NPC_10,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        RunBackgroundEvent(
            event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, bit_7=True
        ),
        Return(),
        RunEventAsSubroutine(
            E0456_YOSHI_TALKS_TO_OTHER_YOSHI,
            identifier="EVENT_471_run_event_as_subroutine_19"),
        RunDialog(
            dialog_id=DI0909_THAT_CANT_HAPPEN_TWICE,
            above_object=NPC_10,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        RunBackgroundEvent(
            event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, bit_7=True
        ),
        Return(),
    ]
)
