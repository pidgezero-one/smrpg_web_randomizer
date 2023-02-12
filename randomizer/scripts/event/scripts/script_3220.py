# E3220_SHIP_BARREL_PUZZLE_BARREL_MOVEMENT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToObjectCoord(object=MEM_70A8, coord=COORD_Z, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3220_clear_bit_4"]),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASClearSolidityBits(bit_4=True, cant_walk_through=True),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASSequencePlaybackOn(),
                ASSetAllSpeeds(VERY_SLOW),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASShiftSouthwestPixels(4),
                ASSetAllSpeeds(SLOW),
                ASShiftSouthwestPixels(8),
                ASSetAllSpeeds(NORMAL),
                ASJumpToHeight(height=48, silent=True),
                ASShiftSouthwestPixels(20),
                ASFaceSoutheast(),
                ASFixedFCoordOn(),
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                ),
                ASPlaySound(sound=SO109_BIG_SHELL_HIT, channel=4),
                ASSequenceLoopingOff(),
                ASSequencePlaybackOff(),
                ASSetSolidityBits(bit_4=True, cant_walk_through=True),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
                ASReturn(),
                ASCopyVarToVar(from_var=TEMP_7032, to_var=PRIMARY_TEMP_700C),
                ASFaceEast7C(),
                ASSequenceLoopingOff(),
                ASSequencePlaybackOff(),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
                ASReturn(),
            ],
        ),
        Return(),
        ClearBit(TEMP_7044_6, identifier="EVENT_3220_clear_bit_4"),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSet700CToObjectCoord(object=DUMMY_0X07, coord=COORD_F, pixel=True),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    1,
                    ["EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_8"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    0,
                    ["EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_8"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    2,
                    ["EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_8"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    5,
                    ["EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_15"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    4,
                    ["EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_15"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    6,
                    ["EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_15"],
                ),
                ASJmp(["EVENT_3220_action_queue_sync_5_SUBSCRIPT_ret_21"]),
                ASFixedFCoordOn(
                    identifier="EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_8"
                ),
                ASSequenceLoopingOn(),
                ASPause(5),
                ASSequenceLoopingOff(),
                ASFixedFCoordOff(),
                ASSetBit(TEMP_7044_6),
                ASJmp(["EVENT_3220_action_queue_sync_5_SUBSCRIPT_ret_21"]),
                ASFixedFCoordOn(
                    identifier="EVENT_3220_action_queue_sync_5_SUBSCRIPT_fixed_f_coord_on_15"
                ),
                ASSequenceLoopingOn(),
                ASPause(5),
                ASSequenceLoopingOff(),
                ASFixedFCoordOff(),
                ASSetBit(TEMP_7044_6),
                ASReturn(identifier="EVENT_3220_action_queue_sync_5_SUBSCRIPT_ret_21"),
            ],
        ),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASSet700CToObjectCoord(object=MARIO, coord=COORD_F, pixel=True),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    1,
                    ["EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_9"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    0,
                    ["EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_9"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    2,
                    ["EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_9"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    5,
                    [
                        "EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_21"
                    ],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    4,
                    [
                        "EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_21"
                    ],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    6,
                    [
                        "EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_21"
                    ],
                ),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
                ASJmp(
                    [
                        "EVENT_3220_action_queue_async_6_SUBSCRIPT_sequence_looping_off_37"
                    ]
                ),
                ASSetSpriteSequence(
                    index=5,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    identifier="EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_9",
                ),
                ASShiftNorthwestPixels(1),
                ASSetSpriteSequence(
                    index=4, is_mold=True, is_sequence=True, looping=True
                ),
                ASShiftNorthwestPixels(1),
                ASSetSpriteSequence(
                    index=3, is_mold=True, is_sequence=True, looping=True
                ),
                ASShiftNorthwestPixels(1),
                ASSetSpriteSequence(
                    index=2, is_mold=True, is_sequence=True, looping=True
                ),
                ASShiftNorthwestPixels(1),
                ASSetSpriteSequence(
                    index=1, is_mold=True, is_sequence=True, looping=True
                ),
                ASShiftNorthwestPixels(1),
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                ),
                ASJmp(
                    [
                        "EVENT_3220_action_queue_async_6_SUBSCRIPT_object_memory_clear_bit_32"
                    ]
                ),
                ASSetSpriteSequence(
                    index=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    identifier="EVENT_3220_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_21",
                ),
                ASShiftSoutheastPixels(1),
                ASSetSpriteSequence(
                    index=2, is_mold=True, is_sequence=True, looping=True
                ),
                ASShiftSoutheastPixels(1),
                ASSetSpriteSequence(
                    index=3, is_mold=True, is_sequence=True, looping=True
                ),
                ASShiftSoutheastPixels(1),
                ASSetSpriteSequence(
                    index=4, is_mold=True, is_sequence=True, looping=True
                ),
                ASShiftSoutheastPixels(1),
                ASSetSpriteSequence(
                    index=5, is_mold=True, is_sequence=True, looping=True
                ),
                ASShiftSoutheastPixels(1),
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                ),
                ASObjectMemoryClearBit(
                    arg_1=0x30,
                    bits=[4],
                    identifier="EVENT_3220_action_queue_async_6_SUBSCRIPT_object_memory_clear_bit_32",
                ),
                ASSet700CToObjectCoord(
                    object=DUMMY_0X07, coord=COORD_Y, pixel=True, bit_7=True
                ),
                ASJmpIfVarNotEqualsConst(
                    PRIMARY_TEMP_700C,
                    21,
                    [
                        "EVENT_3220_action_queue_async_6_SUBSCRIPT_sequence_looping_off_37"
                    ],
                ),
                ASSetBit(TEMP_7044_5),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASSequenceLoopingOff(
                    identifier="EVENT_3220_action_queue_async_6_SUBSCRIPT_sequence_looping_off_37"
                ),
                ASSequencePlaybackOff(),
            ],
        ),
        JmpIfBitClear(TEMP_7044_5, ["EVENT_3220_ret_11"]),
        SetSyncActionScript(NPC_2, A0336_SHIP_BARREL_PUZZLE_BUTTON),
        Inc(TEMP_70AE),
        ClearBit(TEMP_7044_6),
        Return(identifier="EVENT_3220_ret_11"),
    ]
)
