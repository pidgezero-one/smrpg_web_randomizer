# pylint: disable=C0301

"""E0932_FAT_YOSHI"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO129_BABY_YOSHI, channel=6),
        JmpIfBitClear(TEMP_7044_5, ["EVENT_932_enable_controls_until_return_36"]),
        RunEventAsSubroutine(E0456_YOSHI_TALKS_TO_OTHER_YOSHI),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalkToXYCoords(x=14, y=62),
            ],
        ),
        StartAsyncEmbeddedActionScript(
            target=NPC_9, prefix=0xF1, subscript=[ASSetSequenceSpeed(FAST)]
        ),
        RememberLastObject(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=6, sprite_offset=6, is_sequence=True, looping=True
                ),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        ActionQueueAsync(target=NPC_9, subscript=[ASFaceNorthwest()]),
        SetSyncActionScript(NPC_9, A0119_SLOW_SEQUENCE_LOOP),
        StoreItemAmountTo7000(YoshiCookie),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_932_close_dialog_28"]),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
        RunDialog(
            dialog_id=DI2365_PROMPT_TO_FEED_BABY_YOSHI,
            above_object=MEM_70A8,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfDialogOptionBSelected(["EVENT_932_close_dialog_28"]),
        RunDialog(
            dialog_id=DI2366_HOW_MANY_COOKIES_TO_FEED_BABY,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        SetBit(TEMP_7042_0),
        JmpToSubroutine(["EVENT_930_enable_controls_until_return_85"]),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=14, sprite_offset=1, is_sequence=True, looping=True
                ),
                ASPlaySound(sound=SO061_DEEP_UHOH, channel=4),
                ASPause(54),
                ASResetProperties(),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        SetObjectMemoryToVar(SECONDARY_TEMP_7024),
        RemoveOneOfItemFromInventory(YoshiCookie),
        EndLoop(),
        CopyVarToVar(from_var=FED_COOKIES, to_var=PRIMARY_TEMP_7000),
        AddVarTo7000(SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=FED_COOKIES),
        CompareVarToConst(PRIMARY_TEMP_7000, 21),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_932_set_bit_39"]),
        Pause(30, identifier="EVENT_932_pause_26"),
        PlaySound(sound=SO129_BABY_YOSHI, channel=6),
        CloseDialog(identifier="EVENT_932_close_dialog_28"),
        RunBackgroundEvent(
            event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, bit_7=True
        ),
        ClearBit(TEMP_7042_0),
        ClearBit(TEMP_7043_4),
        ClearBit(TEMP_7043_5),
        ClearBit(TEMP_7043_6),
        ClearBit(TEMP_7043_7),
        Return(),
        EnableControlsUntilReturn(
            [LEFT, RIGHT, DOWN, UP, A, Y, B],
            identifier="EVENT_932_enable_controls_until_return_36",
        ),
        Pause(32),
        Return(),
        SetBit(UNKNOWN_7084_1, identifier="EVENT_932_set_bit_39"),
        SetVarToConst(FED_COOKIES, 0),
        Jmp(["EVENT_932_pause_26"]),
    ]
)
