"""A0733_MINES_CROCO"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetAllSpeeds(FAST),
        ClearSolidityBits(cant_pass_walls=True),
        JmpIfBitSet(
            MINES_BOSS_1_DEFEATED,
            ["ACTION_730_clear_solidity_bits_54"],
            identifier="ACTION_733_jmp_if_bit_set_3",
        ),
        VisibilityOff(),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        JmpIfVarEqualsConst(
            MINES_MIDBOSS_POSITION, 25, ["ACTION_733_transfer_to_xyzf_29"]
        ),
        SetBit(TEMP_7044_6),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 19, ["ACTION_733_pause_14"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 21, ["ACTION_733_pause_17"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 17, ["ACTION_733_pause_20"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 27, ["ACTION_733_pause_23"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 23, ["ACTION_733_pause_26"]),
        Pause(100, identifier="ACTION_733_pause_14"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 21),
        Jmp(["ACTION_733_jmp_if_bit_set_3"]),
        Pause(200, identifier="ACTION_733_pause_17"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 17),
        Jmp(["ACTION_733_jmp_if_bit_set_3"]),
        Pause(200, identifier="ACTION_733_pause_20"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 27),
        Jmp(["ACTION_733_jmp_if_bit_set_3"]),
        Pause(200, identifier="ACTION_733_pause_23"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 23),
        Jmp(["ACTION_733_jmp_if_bit_set_3"]),
        Pause(100, identifier="ACTION_733_pause_26"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 25),
        Jmp(["ACTION_733_jmp_if_bit_set_3"]),
        TransferToXYZF(
            x=27, y=88, z=0, direction=EAST, identifier="ACTION_733_transfer_to_xyzf_29"
        ),
        JmpIfBitSet(TEMP_7044_6, ["ACTION_733_face_southwest_37"]),
        SetWalkingSpeed(FASTEST),
        WalkSouthwestSteps(2),
        SetWalkingSpeed(FAST),
        SetBit(TEMP_7044_6),
        VisibilityOn(),
        Jmp(["ACTION_733_object_memory_clear_bit_40"]),
        Pause(1, identifier="ACTION_733_face_southwest_37"),
        FaceSouthwest(),
        VisibilityOn(),
        WalkSouthwestSteps(2),
        ObjectMemoryClearBit(
            arg_1=0x30, bits=[4], identifier="ACTION_733_object_memory_clear_bit_40"
        ),
        SetSolidityBits(cant_walk_through=True),
        PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
        WalkSouthwestSteps(2),
        SequenceLoopingOn(),
        Pause(8),
        FaceNorthwest(),
        Pause(8),
        FaceSoutheast(),
        Pause(8),
        SequenceLoopingOff(),
        WalkSouthwestSteps(3),
        WalkSoutheastSteps(2),
        WalkSouthwestSteps(4),
        SetVarToConst(MINES_MIDBOSS_POSITION, 19),
        Jmp(["ACTION_733_jmp_if_bit_set_3"]),
    ]
)
