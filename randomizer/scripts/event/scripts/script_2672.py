# pylint: disable=C0301

"""E2672_TOWER_KNIFE_GUY_MINIGAME_BUSINESS_LOGIC"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_2672_set_2"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASDb(bytearray(b"\xc8\x94")),
                ASAddConstToVar(Y_COORD_2, 2),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPause(
                    1, identifier="EVENT_2672_action_queue_async_1_SUBSCRIPT_pause_3"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2672_action_queue_async_1_SUBSCRIPT_pause_3"]
                ),
                ASDb(bytearray(b"\x98")),
                ASFaceNorth(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        SetVarToConst(TEMP_70AE, 20, identifier="EVENT_2672_set_2"),
        ResumeActionScript(NPC_0),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASTransferXYZFPixels(x=244, y=1, z=0, direction=EAST),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASTransferXYZFPixels(x=12, y=1, z=0, direction=EAST),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        RememberLastObject(),
        Pause(10),
        SetSyncActionScript(NPC_0, A0893_KNIFE_GUY_HIDING),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(index=16, is_mold=True, looping=True),
                ASPause(30),
                ASResetProperties(),
            ]),
        CopyVarToVar(from_var=UNKNOWN_70C9, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_702C),
        CompareVarToConst(TEMP_702C, 10),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2672_set_var_to_random_54"]),
        CompareVarToConst(TEMP_702C, 5),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2672_set_var_to_random_48"]),
        SetVarToRandom(TEMP_702A, 5, identifier="EVENT_2672_set_var_to_random_43"),
        CompareVarToConst(TEMP_702A, 1),
        JmpIfComparisonResultIsLesser(["EVENT_2672_set_var_to_random_43"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASLoadMemory(TEMP_702A),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=False),
                ASPause(16),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=False),
                ASPause(16),
                ASEndLoop(),
                ASJmpIfRandom1of2(
                    [
                        "EVENT_2672_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_13"
                    ]
                ),
                ASSetSpriteSequence(index=16, is_mold=True, looping=True),
                ASPause(30),
                ASSetBit(TEMP_7044_5),
                ASClearBit(TEMP_7044_6),
                ASJmp(["EVENT_2672_jmp_47"]),
                ASSetSpriteSequence(
                    index=0,
                    is_sequence=True,
                    looping=False,
                    identifier="EVENT_2672_action_queue_async_46_SUBSCRIPT_set_sprite_sequence_13"),
                ASPause(16),
                ASSetSpriteSequence(index=16, is_mold=True, looping=True),
                ASPause(30),
                ASSetBit(TEMP_7044_6),
                ASClearBit(TEMP_7044_5),
            ]),
        Jmp(["EVENT_2672_action_queue_async_59"], identifier="EVENT_2672_jmp_47"),
        SetVarToRandom(TEMP_702A, 7, identifier="EVENT_2672_set_var_to_random_48"),
        CompareVarToConst(TEMP_702A, 1),
        JmpIfComparisonResultIsLesser(["EVENT_2672_set_var_to_random_48"]),
        SetBit(TEMP_7043_7),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(FASTER),
                ASLoadMemory(TEMP_702A),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=False),
                ASPause(14),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=False),
                ASPause(14),
                ASEndLoop(),
                ASJmpIfRandom1of2(
                    [
                        "EVENT_2672_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_13"
                    ]
                ),
                ASSetSpriteSequence(index=16, is_mold=True, looping=True),
                ASPause(30),
                ASSetBit(TEMP_7044_5),
                ASClearBit(TEMP_7044_6),
                ASJmp(["EVENT_2672_jmp_53"]),
                ASSetSpriteSequence(
                    index=0,
                    is_sequence=True,
                    looping=False,
                    identifier="EVENT_2672_action_queue_async_52_SUBSCRIPT_set_sprite_sequence_13"),
                ASPause(14),
                ASSetSpriteSequence(index=16, is_mold=True, looping=True),
                ASPause(30),
                ASSetBit(TEMP_7044_6),
                ASClearBit(TEMP_7044_5),
            ]),
        Jmp(["EVENT_2672_action_queue_async_59"], identifier="EVENT_2672_jmp_53"),
        SetVarToRandom(TEMP_702A, 7, identifier="EVENT_2672_set_var_to_random_54"),
        CompareVarToConst(TEMP_702A, 1),
        JmpIfComparisonResultIsLesser(["EVENT_2672_set_var_to_random_54"]),
        SetBit(TEMP_7044_0),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASLoadMemory(TEMP_702A),
                ASSetSpriteSequence(index=0, is_mold=True, looping=True),
                ASPause(3),
                ASSetSpriteSequence(index=2, is_mold=True, looping=True),
                ASPause(3),
                ASSetSpriteSequence(index=4, is_mold=True, looping=True),
                ASPause(3),
                ASSetSpriteSequence(index=6, is_mold=True, looping=True),
                ASPause(3),
                ASSetSpriteSequence(index=8, is_mold=True, looping=True),
                ASPause(3),
                ASSetSpriteSequence(index=10, is_mold=True, looping=True),
                ASPause(3),
                ASSetSpriteSequence(index=12, is_mold=True, looping=True),
                ASPause(3),
                ASSetSpriteSequence(index=14, is_mold=True, looping=True),
                ASPause(3),
                ASEndLoop(),
                ASJmpIfRandom1of2(
                    [
                        "EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_27"
                    ]
                ),
                ASSetSpriteSequence(index=0, is_mold=True, looping=True),
                ASPause(1),
                ASSetSpriteSequence(index=16, is_mold=True, looping=True),
                ASPause(30),
                ASSetBit(TEMP_7044_5),
                ASClearBit(TEMP_7044_6),
                ASJmp(["EVENT_2672_action_queue_async_59"]),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    looping=True,
                    identifier="EVENT_2672_action_queue_async_58_SUBSCRIPT_set_sprite_sequence_27"),
                ASPause(3),
                ASSetSpriteSequence(index=2, is_mold=True, looping=True),
                ASPause(3),
                ASSetSpriteSequence(index=4, is_mold=True, looping=True),
                ASPause(3),
                ASSetSpriteSequence(index=6, is_mold=True, looping=True),
                ASPause(3),
                ASSetSpriteSequence(index=8, is_mold=True, looping=True),
                ASPause(3),
                ASSetSpriteSequence(index=10, is_mold=True, looping=True),
                ASPause(1),
                ASSetSpriteSequence(index=16, is_mold=True, looping=True),
                ASPause(30),
                ASSetBit(TEMP_7044_6),
                ASClearBit(TEMP_7044_5),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASSetSequenceSpeed(NORMAL)],
            identifier="EVENT_2672_action_queue_async_59"),
        SetSyncActionScript(NPC_0, A0893_KNIFE_GUY_HIDING),
        RunDialog(
            dialog_id=DI2550_WHICH_HAND,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        DisableObjectTrigger(NPC_0),
        ActionQueueSync(
            target=NPC_2, subscript=[ASSetSolidityBits(cant_jump_through=True)]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASSetSolidityBits(cant_jump_through=True)]
        ),
        SetBit(TEMP_7043_2),
        RememberLastObject(),
        Return(),
        CloseDialog(identifier="EVENT_2672_close_1"),
        PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
        Inc(UNKNOWN_70C9),
        CopyVarToVar(from_var=UNKNOWN_70C9, to_var=PRIMARY_TEMP_7000),
        RunEventAsSubroutine(E2671_TOWER_KNIFE_GUY_CHECK_IF_SIDEQUEST_COMPLETED),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2672_jmp_if_bit_set_137"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 255, ["EVENT_2672_set_132"]),
        ClearBit(TEMP_7043_2),
        ClearBit(TEMP_7044_4),
        Jmp(["EVENT_2672_consolation_grant"]),
        CloseDialog(identifier="EVENT_2672_close_2"),
        PlaySound(sound=SO088_WRONG_SIGNAL, channel=6),
        CopyVarToVar(from_var=UNKNOWN_70C9, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2672_clear_bit_84"]),
        Dec(PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70C9),
        ClearBit(TEMP_7043_2, identifier="EVENT_2672_clear_bit_84"),
        JmpIfBitSet(TEMP_7044_5, ["EVENT_2672_set_action_script_sync_89"]),
        SetSyncActionScript(NPC_0, A0894_KNIFE_GUY_HOLDING_BALL),
        Pause(90),
        Jmp(["EVENT_2672_set_action_script_sync_91"]),
        SetSyncActionScript(
            NPC_0,
            A0895_KNIFE_GUY_HOLDING_BALL,
            identifier="EVENT_2672_set_action_script_sync_89"),
        Pause(90),
        SetSyncActionScript(
            NPC_0,
            A0892_KNIFE_GUY_DEFAULT,
            identifier="EVENT_2672_set_action_script_sync_91"),
        Jmp(["EVENT_2672_clear_bit_144"]),
        RunEventAsSubroutine(
            E2670_TOWER_KNIFE_GUY_CONSOLATION_PRIZE,
            identifier="EVENT_2672_consolation_grant"),
        Jmp(["EVENT_2672_clear_bit_144"]),
        SetVarToConst(ITEM_ID, RedEssence, identifier="EVENT_2672_set_132"),
        RunEventAsSubroutine(E0160_NPC_QUEST_GRANT_ITEM),
        Jmp(["EVENT_2672_clear_bit_144"]),
        JmpIfBitSet(
            KNIFE_GUY_PRIZE_GRANTED,
            ["EVENT_2672_consolation_grant"],
            identifier="EVENT_2672_jmp_if_bit_set_137"),
        SetBit(KNIFE_GUY_PRIZE_GRANTED),
        RunDialog(
            dialog_id=DI0038_KNIFE_GUY_PRIZE_GRANT,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        ClearBit(TEMP_7043_2, identifier="EVENT_2672_clear_bit_144"),
        ClearBit(TEMP_7043_3),
        ClearBit(TEMP_7044_5),
        ClearBit(TEMP_7044_6),
        ClearBit(TEMP_7043_4),
        ClearBit(TEMP_7044_4),
        ClearBit(TEMP_7043_7),
        ClearBit(TEMP_7044_0),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASClearSolidityBits(cant_jump_through=True),
                ASTransferXYZFPixels(x=12, y=255, z=0, direction=EAST),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASClearSolidityBits(cant_jump_through=True),
                ASTransferXYZFPixels(x=244, y=255, z=0, direction=EAST),
            ]),
        RememberLastObject(),
        SetSyncActionScript(NPC_0, A0892_KNIFE_GUY_DEFAULT),
        EnableObjectTrigger(NPC_0),
        Return(),
    ]
)
