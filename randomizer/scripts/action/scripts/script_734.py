"""A0734_MINES_CROCO"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetAllSpeeds(FAST),
        ClearSolidityBits(cant_pass_walls=True),
        JmpIfBitSet(
            MINES_BOSS_1_DEFEATED,
            ["ACTION_730_clear_solidity_bits_54"],
            identifier="ACTION_734_jmp_if_bit_set_3",
        ),
        VisibilityOff(),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        JmpIfVarEqualsConst(
            MINES_MIDBOSS_POSITION, 19, ["ACTION_734_transfer_to_xyzf_29"]
        ),
        SetBit(TEMP_7044_6),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 21, ["ACTION_734_pause_14"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 17, ["ACTION_734_pause_17"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 27, ["ACTION_734_pause_20"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 23, ["ACTION_734_pause_23"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 25, ["ACTION_734_pause_26"]),
        Pause(200, identifier="ACTION_734_pause_14"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 17),
        Jmp(["ACTION_734_jmp_if_bit_set_3"]),
        Pause(200, identifier="ACTION_734_pause_17"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 27),
        Jmp(["ACTION_734_jmp_if_bit_set_3"]),
        Pause(200, identifier="ACTION_734_pause_20"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 23),
        Jmp(["ACTION_734_jmp_if_bit_set_3"]),
        Pause(100, identifier="ACTION_734_pause_23"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 25),
        Jmp(["ACTION_734_jmp_if_bit_set_3"]),
        Pause(200, identifier="ACTION_734_pause_26"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 19),
        Jmp(["ACTION_734_jmp_if_bit_set_3"]),
        TransferToXYZF(
            x=4, y=118, z=0, direction=EAST, identifier="ACTION_734_transfer_to_xyzf_29"
        ),
        JmpIfBitSet(TEMP_7044_6, ["ACTION_734_face_southeast_37"]),
        SetWalkingSpeed(FASTEST),
        WalkSoutheastSteps(2),
        SetWalkingSpeed(FAST),
        SetBit(TEMP_7044_6),
        VisibilityOn(),
        Jmp(["ACTION_734_object_memory_clear_bit_40"]),
        Pause(1, identifier="ACTION_734_face_southeast_37"),
        FaceSoutheast(),
        VisibilityOn(),
        WalkSoutheastSteps(2),
        ObjectMemoryClearBit(
            arg_1=0x30, bits=[4], identifier="ACTION_734_object_memory_clear_bit_40"
        ),
        SetSolidityBits(cant_walk_through=True),
        PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
        WalkSoutheastSteps(2),
        SequenceLoopingOn(),
        FixedFCoordOn(),
        JumpToHeight(48),
        Walk1StepSouthwest(),
        FixedFCoordOff(),
        SequenceLoopingOff(),
        WalkSoutheastSteps(2),
        SetVarToConst(MINES_MIDBOSS_POSITION, 21),
        Jmp(["ACTION_734_jmp_if_bit_set_3"]),
    ]
)
