"""A0732_MINES_CROCO"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetAllSpeeds(FAST),
        ClearSolidityBits(cant_pass_walls=True),
        JmpIfBitSet(
            MINES_BOSS_1_DEFEATED,
            ["ACTION_730_clear_solidity_bits_54"],
            identifier="ACTION_732_jmp_if_bit_set_3",
        ),
        VisibilityOff(),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        JmpIfVarEqualsConst(
            MINES_MIDBOSS_POSITION, 23, ["ACTION_732_transfer_to_xyzf_29"]
        ),
        SetBit(TEMP_7044_6),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 25, ["ACTION_732_pause_14"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 19, ["ACTION_732_pause_17"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 21, ["ACTION_732_pause_20"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 17, ["ACTION_732_pause_23"]),
        JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 27, ["ACTION_732_pause_26"]),
        Pause(200, identifier="ACTION_732_pause_14"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 19),
        Jmp(["ACTION_732_jmp_if_bit_set_3"]),
        Pause(100, identifier="ACTION_732_pause_17"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 21),
        Jmp(["ACTION_732_jmp_if_bit_set_3"]),
        Pause(200, identifier="ACTION_732_pause_20"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 17),
        Jmp(["ACTION_732_jmp_if_bit_set_3"]),
        Pause(200, identifier="ACTION_732_pause_23"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 27),
        Jmp(["ACTION_732_jmp_if_bit_set_3"]),
        Pause(200, identifier="ACTION_732_pause_26"),
        SetVarToConst(MINES_MIDBOSS_POSITION, 25),
        Jmp(["ACTION_732_jmp_if_bit_set_3"]),
        TransferToXYZF(
            x=18,
            y=123,
            z=0,
            direction=EAST,
            identifier="ACTION_732_transfer_to_xyzf_29",
        ),
        JmpIfBitSet(TEMP_7044_6, ["ACTION_732_face_northwest_37"]),
        SetWalkingSpeed(FASTEST),
        WalkNorthwestSteps(2),
        SetWalkingSpeed(FAST),
        SetBit(TEMP_7044_6),
        VisibilityOn(),
        Jmp(["ACTION_732_object_memory_clear_bit_40"]),
        Pause(1, identifier="ACTION_732_face_northwest_37"),
        FaceNorthwest(),
        VisibilityOn(),
        WalkNorthwestSteps(2),
        ObjectMemoryClearBit(
            arg_1=0x30, bits=[4], identifier="ACTION_732_object_memory_clear_bit_40"
        ),
        SetSolidityBits(cant_walk_through=True),
        PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
        WalkNorthwestSteps(5),
        SequenceLoopingOn(),
        Pause(32),
        SequenceLoopingOff(),
        WalkSouthwestSteps(3),
        WalkNorthwestSteps(2),
        WalkSouthwestSteps(4),
        SetVarToConst(MINES_MIDBOSS_POSITION, 25),
        Jmp(["ACTION_732_jmp_if_bit_set_3"]),
    ]
)
