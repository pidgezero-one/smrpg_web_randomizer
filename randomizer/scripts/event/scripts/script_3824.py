# E3824_YOSTER_ISLE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(UNKNOWN_70EE, 0),
        SetVarToConst(UNKNOWN_70EB, 0),
        SetVarToConst(UNKNOWN_7100, 0),
        ClearBit(YOSHI_UNKNOWN_7061_7),
        ClearBit(MUSHROOM_DERBY_MANUAL),
        ClearBit(MUSHROOM_DERBY_AUTO),
        SetTempAsyncActionScript(NPC_1, A0803_INC_PALETTE_ROW),
        SetTempAsyncActionScript(NPC_2, A0803_INC_PALETTE_ROW),
        SetTempAsyncActionScript(NPC_5, A0803_INC_PALETTE_ROW),
        SetTempAsyncActionScript(NPC_4, A0803_INC_PALETTE_ROW),
        ActionQueueAsync(
            target=NPC_16,
            subscript=[ASTransferXYZFPixels(x=0, y=252, z=0, direction=EAST)],
        ),
        JmpIfBitSet(COMPLETED_MUSHROOM_DERBY, ["EVENT_3824_pause_action_script_47"]),
        PauseActionScript(NPC_5),
        PauseActionScript(NPC_9),
        StartSyncEmbeddedActionScript(
            target=NPC_9,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=14, y=86, z=0, direction=EAST),
                ASFaceNortheast(),
            ],
        ),
        StartSyncEmbeddedActionScript(
            target=NPC_5,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=21, y=58, z=0, direction=EAST),
                ASFaceNortheast(),
                ASSetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        ActionQueueSync(target=NPC_0, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_2, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_1, subscript=[ASSetPriority(3)]),
        ActionQueueSync(
            target=NPC_12,
            subscript=[
                ASSetSpriteSequence(index=12, is_sequence=True, looping=True),
                ASSetPriority(3),
                ASVisibilityOff(),
            ],
        ),
        RememberLastObject(),
        SetSyncActionScript(NPC_5, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS),
        SetSyncActionScript(NPC_9, A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE),
        JmpIfBitSet(
            YOSTER_ISLE_LIBERATED_1,
            ["EVENT_3824_jmp_if_bit_clear_32"],
            identifier="EVENT_3824_jmp_if_bit_set_28",
        ),
        JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_3824_jmp_if_bit_set_33"]),
        FadeInFromBlack(
            sync=False, identifier="EVENT_3824_fade_in_from_black_async_30"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3824_ret_31"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3824_ret_31"]),
        RunEventAsSubroutine(E3901_YOSTER_ISLE_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3824_ret_31"),
        JmpIfBitClear(
            MARRYMORE_LIBERATED,
            ["EVENT_3824_clear_bit_41"],
            identifier="EVENT_3824_jmp_if_bit_clear_32",
        ),
        JmpIfBitSet(
            UNKNOWN_7084_1,
            ["EVENT_3824_summon_to_current_level_43"],
            identifier="EVENT_3824_jmp_if_bit_set_33",
        ),
        SummonObjectToCurrentLevel(NPC_13),
        ApplyTileModToLevel(use_alternate=True, room_id=R034_YOSTER_ISLE, mod_id=0),
        ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=0),
        ActionQueueAsync(
            target=NPC_13,
            subscript=[
                ASSetSpriteSequence(
                    index=15, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASSetPriority(3),
                ASFloatingOff(),
            ],
        ),
        JmpIfBitSet(
            YOSTER_ISLE_LIBERATED_1,
            ["EVENT_3824_clear_bit_41"],
            identifier="EVENT_3824_jmp_if_bit_set_38",
        ),
        Jmp(["EVENT_3824_fade_in_from_black_async_30"]),
        ClearBit(YOSTER_ISLE_LIBERATED_1, identifier="EVENT_3824_clear_bit_41"),
        Return(),
        SummonObjectToCurrentLevel(
            NPC_11, identifier="EVENT_3824_summon_to_current_level_43"
        ),
        RemoveObjectFromCurrentLevel(NPC_13),
        ActionQueueAsync(
            target=NPC_11,
            subscript=[ASSetPriority(3), ASSequenceLoopingOn(), ASSequencePlaybackOn()],
        ),
        Jmp(["EVENT_3824_jmp_if_bit_set_38"]),
        PauseActionScript(NPC_3, identifier="EVENT_3824_pause_action_script_47"),
        StartSyncEmbeddedActionScript(
            target=NPC_3,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=11, y=82, z=0, direction=EAST),
                ASSetPriority(3),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASTransferToXYZF(x=11, y=83, z=0, direction=EAST),
                ASSetPriority(3),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_10,
            subscript=[
                ASTransferToXYZF(x=9, y=80, z=0, direction=EAST),
                ASTransferXYZFPixels(x=8, y=0, z=0, direction=EAST),
                ASSetPriority(3),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASTransferToXYZF(x=16, y=64, z=0, direction=EAST),
                ASSetPriority(3),
                ASSetObjectMemoryBits(arg_1=0x0B, bits=[1]),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=19, y=60, z=0, direction=EAST),
                ASSetPriority(3),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        ActionQueueAsync(
            target=NPC_12,
            subscript=[
                ASSetSpriteSequence(index=12, is_sequence=True, looping=True),
                ASSetPriority(3),
                ASVisibilityOff(),
            ],
        ),
        SetSyncActionScript(NPC_0, A0677_MUSHROOM_DERBY_UNKNOWN),
        SetSyncActionScript(NPC_3, A0676_MUSHROOM_DERBY_UNKNOWN),
        Jmp(["EVENT_3824_jmp_if_bit_set_28"]),
    ]
)
