# E2493_MIMIC_3

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=CHEST_COIN_SIZE),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASShiftNorthSteps(2)],
        ),
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
            packet=P004_MIMIC_POOF_ON_DEFEAT, destinations=["EVENT_2493_pause_12"]
        ),
        Pause(32, identifier="EVENT_2493_pause_12"),
        StopEmbeddedActionScript(MEM_70A8),
        SetVarToConst(PRIMARY_TEMP_7000, 514),
        RunEventAsSubroutine(E0353_BOSS_BATTLE),
        JmpIfBitSet(GAME_OVER, ["EVENT_2493_reset_and_choose_game_26"]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASShiftSouthSteps(2), ASSetWalkingSpeed(NORMAL)],
        ),
        FadeInFromBlack(sync=False),
        SetBit(MIMIC_3_CLEARED),
        SetBit(UNKNOWN_MIMIC_BIT),
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
                        "EVENT_2493_action_queue_sync_25_SUBSCRIPT_object_memory_clear_bit_9"
                    ],
                ),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASSequenceLoopingOff(),
                ASReturn(),
                ASObjectMemoryClearBit(
                    arg_1=0x30,
                    bits=[4],
                    identifier="EVENT_2493_action_queue_sync_25_SUBSCRIPT_object_memory_clear_bit_9",
                ),
                ASSequenceLoopingOff(),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=False),
                ASReturn(),
            ],
        ),
        JmpIfBitSet(RUN_AWAY, ["EVENT_2493_ret_25"]),
        DisableObjectTrigger(MEM_70A8),
        DisableTriggerOfObjectAt70A8InCurrentLevel(),
        StopEmbeddedActionScript(MEM_70A8),
        SetAsyncActionScript(MEM_70A8, A0015_DO_NOTHING),
        SetVarToConst(PRIMARY_TEMP_7000, 514),
        JmpToEvent(E0171_MIMIC_3_GRANT_STAR_PIECE_CONTAINER),
        Return(identifier="EVENT_2493_ret_25"),
        ResetAndChooseGame(identifier="EVENT_2493_reset_and_choose_game_26"),
    ]
)
