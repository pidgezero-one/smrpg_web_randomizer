# pylint: disable=C0301

"""E3078_MIMIC_OR_SLOT_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=CHEST_COIN_SIZE),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=False),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\xc0\x03\x80\xff")),
                ASPause(8),
                ASBPL262728(),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
            ],
        ),
        Set70107015ToObjectXYZ(MEM_70A8),
        CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 608),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
        ClearBit(MIMIC_3_CLEARED),
        PlaySound(sound=SO014_FLOWER, channel=6),
        CreatePacketAt7010(
            packet=P004_MIMIC_POOF_ON_DEFEAT, destinations=["EVENT_3078_pause_11"]
        ),
        Pause(8, identifier="EVENT_3078_pause_11"),
        Pause(12),
        PlaySound(sound=SO000_SILENCE, channel=6),
        JmpIfVarEqualsConst(BATTLE_PACK_ID, 156, ["EVENT_3078_start_battle_18"]),
        JmpIfVarEqualsConst(BATTLE_PACK_ID, 157, ["EVENT_3078_start_battle_20"]),
        JmpIfVarEqualsConst(BATTLE_PACK_ID, 158, ["EVENT_3078_jmp_if_bit_set_22"]),
        JmpIfVarEqualsConst(BATTLE_PACK_ID, 159, ["EVENT_3078_jmp_if_bit_set_22"]),
        StartBattleAtBattlefield(
            156, BF21_KERO_SEWERS, identifier="EVENT_3078_start_battle_18"
        ),
        Jmp(["EVENT_3078_jmp_if_bit_set_22"]),
        StartBattleAtBattlefield(
            157, BF04_SUNKEN_SHIP, identifier="EVENT_3078_start_battle_20"
        ),
        Jmp(["EVENT_3078_jmp_if_bit_set_22"]),
        JmpIfBitSet(
            GAME_OVER,
            ["EVENT_3078_reset_and_choose_game_30"],
            identifier="EVENT_3078_jmp_if_bit_set_22",
        ),
        FadeInFromBlack(sync=False),
        SetBit(MIMIC_3_CLEARED),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%@\x00\x80\xff")),
                ASPause(8),
                ASBPL262728(),
                ASJmpIfBitSet(
                    RUN_AWAY,
                    [
                        "EVENT_3078_action_queue_sync_25_SUBSCRIPT_object_memory_clear_bit_9"
                    ],
                ),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=False),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASSequenceLoopingOff(),
                ASReturn(),
                ASObjectMemoryClearBit(
                    arg_1=0x30,
                    bits=[4],
                    identifier="EVENT_3078_action_queue_sync_25_SUBSCRIPT_object_memory_clear_bit_9",
                ),
                ASSequenceLoopingOff(),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=False),
                ASReturn(),
            ],
        ),
        ClearBit(UNKNOWN_MIMIC_BIT),
        JmpIfBitSet(RUN_AWAY, ["EVENT_3078_ret_29"]),
        SetBit(UNKNOWN_MIMIC_BIT),
        Return(identifier="EVENT_3078_ret_29"),
        ResetAndChooseGame(identifier="EVENT_3078_reset_and_choose_game_30"),
    ]
)
