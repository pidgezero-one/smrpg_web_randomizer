"""A0731_MINES_CROCO"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetAllSpeeds(FAST),
        ClearSolidityBits(cant_pass_walls=True),
        JmpIfBitSet(
            MINES_BOSS_1_DEFEATED,
            ["ACTION_730_clear_solidity_bits_54"],
            identifier="ACTION_731_jmp_if_bit_set_4"),
        VisibilityOff(),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        JmpIfVarEqualsConst(
            MINES_MIDBOSS_POSITION, 27, ["ACTION_731_transfer_to_xyzf_30"]
        ),
        SetBit(TEMP_7044_6),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 23, ["ACTION_731_pause_15"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 25, ["ACTION_731_pause_18"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 19, ["ACTION_731_pause_21"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 21, ["ACTION_731_pause_24"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 17, ["ACTION_731_pause_27"]),
        Pause(100, identifier="ACTION_731_pause_15"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 25),
        Jmp(["ACTION_731_jmp_if_bit_set_4"]),
        Pause(200, identifier="ACTION_731_pause_18"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 19),
        Jmp(["ACTION_731_jmp_if_bit_set_4"]),
        Pause(100, identifier="ACTION_731_pause_21"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 21),
        Jmp(["ACTION_731_jmp_if_bit_set_4"]),
        Pause(200, identifier="ACTION_731_pause_24"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 17),
        Jmp(["ACTION_731_jmp_if_bit_set_4"]),
        Pause(200, identifier="ACTION_731_pause_27"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 27),
        Jmp(["ACTION_731_jmp_if_bit_set_4"]),
        TransferToXYZF(
            x=10, y=31, z=0, direction=EAST, identifier="ACTION_731_transfer_to_xyzf_30"
        ),
        JmpIfBitSet(TEMP_7044_6, ["ACTION_731_face_northeast_38"]),
        SetWalkingSpeed(FASTEST),
        WalkNortheastSteps(2),
        SetWalkingSpeed(FAST),
        SetBit(TEMP_7044_6),
        VisibilityOn(),
        Jmp(["ACTION_731_object_memory_clear_bit_41"]),
        Pause(1, identifier="ACTION_731_face_northeast_38"),
        FaceNortheast(),
        VisibilityOn(),
        WalkNortheastSteps(2),
        ObjectMemoryClearBit(
            arg_1=0x30, bits=[4], identifier="ACTION_731_object_memory_clear_bit_41"
        ),
        SetSolidityBits(cant_walk_through=True),
        PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
        WalkNortheastSteps(3),
        WalkNorthwestSteps(10),
        FaceSoutheast(),
        SequenceLoopingOn(),
        JumpToHeight(48),
        Pause(32),
        SequenceLoopingOff(),
        WalkSouthwestSteps(6),
        WalkNorthwestSteps(5),
        SetVarToConst(MINES_MIDBOSS_POSITION, 23),
        Jmp(["ACTION_731_jmp_if_bit_set_4"]),
        JmpIfBitSet(UNUSED_7056_4, ["ACTION_731_ret_59"]),
        VisibilityOff(),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        Return(identifier="ACTION_731_ret_59"),
    ]
)
