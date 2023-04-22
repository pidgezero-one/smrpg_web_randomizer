"""A0336_SHIP_BARREL_PUZZLE_BUTTON"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        Pause(1, identifier="ACTION_336_pause_5"),
        JmpIfVarEqualsConst(TEMP_70AE, 2, ["ACTION_336_pause_5"]),
        JmpIfObjectWithinRange(
            comparing_npc=MARIO, usually=0, tiles=1, destinations=["ACTION_336_pause_5"]
        ),
        JmpIfObjectWithinRange(
            comparing_npc=NPC_0,
            usually=208,
            tiles=0,
            destinations=["ACTION_336_pause_5"],
        ),
        Dec(TEMP_70AE),
        PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        SetVRAMPriority(NORMAL_PRIORITY),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        Return(),
    ]
)
