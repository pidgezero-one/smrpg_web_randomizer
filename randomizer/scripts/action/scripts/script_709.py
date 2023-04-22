"""A0709_BOOSTER_HILL_BARREL"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(2),
        FaceSouthwest(),
        FixedFCoordOn(),
        SetAllSpeeds(FASTER),
        TransferToXYZF(x=2, y=48, z=0, direction=EAST),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        SetVarToRandom(PRIMARY_TEMP_700C, 30),
        Inc(PRIMARY_TEMP_700C),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(1),
        EndLoop(),
        PlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
        WalkSouthwestPixels(8),
        JmpIfObjectWithinRange(
            comparing_npc=NPC_4,
            usually=0,
            tiles=3,
            destinations=["ACTION_709_set_bit_18"],
            identifier="ACTION_709_db_14",
        ),
        JumpToHeight(24),
        Walk1StepSoutheast(),
        Jmp(["ACTION_709_db_14"]),
        SetBit(TEMP_7043_1, identifier="ACTION_709_set_bit_18"),
        Jmp(["ACTION_708_jump_to_height_20"]),
    ]
)
