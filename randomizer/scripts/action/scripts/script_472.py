"""A0472_BANDITS_WAY_5_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(),
        Db(bytearray(b"\xfd\x12")),
        FaceNortheast(),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65512),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(1),
        EndLoop(),
        Pause(3, identifier="ACTION_472_pause_8"),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO, usually=128, tiles=3, destinations=["ACTION_472_db_11"]
        ),
        Jmp(["ACTION_472_pause_8"]),
        UnknownJmp3C(
            0x00, 0x40, ["ACTION_472_visibility_on_13"], identifier="ACTION_472_db_11"
        ),
        Jmp(["ACTION_472_pause_8"]),
        VisibilityOn(identifier="ACTION_472_visibility_on_13"),
        SequenceLoopingOn(),
        SetSolidityBits(bit_4=True),
        SetSolidityBits(cant_walk_through=True),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        PlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
        SetAllSpeeds(FASTER),
        JumpToHeight(108),
        WalkNortheastSteps(3),
        Pause(15),
        FaceNorthwest(),
        SetWalkingSpeed(FAST),
        SetSequenceSpeed(VERY_FAST),
        Walk1StepFDirection(identifier="ACTION_472_walk_1_step_f_direction_26"),
        Pause(15),
        TurnClockwise45DegreesNTimes(6),
        Pause(5),
        TurnClockwise45DegreesNTimes(6),
        Pause(15),
        Jmp(["ACTION_472_walk_1_step_f_direction_26"]),
    ]
)
