"""A0710_BOOSTER_HILL_BARREL"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(2),
        FaceSouthwest(),
        FixedFCoordOn(),
        SetAllSpeeds(FASTER),
        TransferToXYZF(x=3, y=46, z=0, direction=EAST),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        SetVarToRandom(PRIMARY_TEMP_700C, 30),
        Inc(PRIMARY_TEMP_700C),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(1),
        EndLoop(),
        JmpIfBitSet(TEMP_7044_4, ["ACTION_710_shift_southwest_pixels_14"]),
        PlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
        WalkSouthwestPixels(8, identifier="ACTION_710_shift_southwest_pixels_14"),
        JmpIfObjectWithinRange(
            comparing_npc=NPC_5,
            usually=0,
            tiles=3,
            destinations=["ACTION_710_set_bit_19"],
            identifier="ACTION_710_db_15"),
        JumpToHeight(24),
        Walk1StepSoutheast(),
        Jmp(["ACTION_710_db_15"]),
        SetBit(TEMP_7043_2, identifier="ACTION_710_set_bit_19"),
        Jmp(["ACTION_708_jump_to_height_20"]),
    ]
)
