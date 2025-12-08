# pylint: disable=C0301

"""E0463_FREE_COOKIE_YOSHI"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO063_YOSHI_TALK, channel=6),
        JmpIfBitClear(TEMP_7044_5, ["EVENT_463_enable_controls_until_return_16"]),
        RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI),
        JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["EVENT_463_store_item_amount_7000_21"]),
        JmpIfBitSet(GOT_FREE_COOKIES, ["EVENT_463_run_background_event_14"]),
        SetBit(GOT_FREE_COOKIES),
        RunDialog(
            dialog_id=DI0938_TAKE_MY_COOKIES,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
        Pause(10),
        PlaySound(sound=SO063_YOSHI_TALK, channel=6),
        RunBackgroundEvent(
            event_id=E0469_YOSTER_ISLE_BACKGROUND,
            return_on_level_exit=True,
            bit_7=True,
            identifier="EVENT_463_run_background_event_14"),
        Return(),
        EnableControlsUntilReturn(
            [LEFT, RIGHT, DOWN, UP, A, Y, B],
            identifier="EVENT_463_enable_controls_until_return_16"),
        Pause(32),
        Return(),
        StoreItemAmountTo7000(
            YoshiCookie, identifier="EVENT_463_store_item_amount_7000_21"
        ),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=UNKNOWN_70D8, to_var=PRIMARY_TEMP_7000),
        AddVarTo7000(SECONDARY_TEMP_7024),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_463_play_sound_30"]),
        RunDialog(
            dialog_id=DI0904_BABY_YOSHI_HINT,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True),
        CloseDialog(),
        RunBackgroundEvent(
            event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, bit_7=True
        ),
        Return(),
        PlaySound(
            sound=SO027_FOUND_AN_ITEM, channel=6, identifier="EVENT_463_play_sound_30"
        ),
        SetVarToConst(PRIMARY_TEMP_7000, 3),
        RunDialog(
            dialog_id=DI0943_GOT_X_COOKIES,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        StartLoopNTimes(2),
        AddToInventory(YoshiCookie),
        EndLoop(),
        RunBackgroundEvent(
            event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, bit_7=True
        ),
        Return(),
    ]
)
