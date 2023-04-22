# pylint: disable=C0301

"""E3126_MIMIC_2_CHEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MIMIC_2_CLEARED, ["EVENT_3126_special_val_2_"]),
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
            packet=P004_MIMIC_POOF_ON_DEFEAT, destinations=["EVENT_3126_pause_11"]
        ),
        Pause(8, identifier="EVENT_3126_pause_11"),
        Pause(12),
        PlaySound(sound=SO000_SILENCE, channel=6),
        SetVarToConst(PRIMARY_TEMP_7000, 513),
        RunEventAsSubroutine(E0353_BOSS_BATTLE),
        JmpIfBitSet(GAME_OVER, ["EVENT_3126_reset_and_choose_game_30"]),
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
                        "EVENT_3126_action_queue_sync_25_SUBSCRIPT_object_memory_clear_bit_9"
                    ],
                ),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=False),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASSequenceLoopingOff(),
                ASReturn(),
                ASObjectMemoryClearBit(
                    arg_1=0x30,
                    bits=[4],
                    identifier="EVENT_3126_action_queue_sync_25_SUBSCRIPT_object_memory_clear_bit_9",
                ),
                ASSequenceLoopingOff(),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=False),
                ASReturn(),
            ],
        ),
        ClearBit(UNKNOWN_MIMIC_BIT),
        JmpIfBitSet(RUN_AWAY, ["EVENT_3126_ret_29"]),
        SetBit(UNKNOWN_MIMIC_BIT),
        SetBit(MIMIC_2_CLEARED),
        SetSyncActionScript(MEM_70A8, A0015_DO_NOTHING),
        SetVarToConst(PRIMARY_TEMP_7000, 513),
        SetVarToConst(PRIMARY_TEMP_7000, 513),
        RunEventAsSubroutine(E0253_NPC_QUEST_1_GRANT),
        SetVarToConst(PRIMARY_TEMP_7000, 513),
        JmpToEvent(E0170_MIMIC_2_GRANT_STAR_PIECE_CONTAINER),
        Return(),
        SetVarToConst(PRIMARY_TEMP_7000, 513, identifier="EVENT_3126_special_val_2_"),
        JmpToEvent(E0245_CHEST_3_GRANT),
        Return(identifier="EVENT_3126_ret_29"),
        ResetAndChooseGame(identifier="EVENT_3126_reset_and_choose_game_30"),
    ]
)
