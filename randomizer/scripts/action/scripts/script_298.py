"""A0298_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_ITEM_PATH_BASE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ClearSolidityBits(
            bit_4=True,
            cant_pass_npcs=True,
            cant_walk_through=True,
            bit_7=True,
            identifier="ACTION_298_clear_solidity_bits_0"),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        SetBit(MIDAS_BOTTOM_LEFT_TUNNEL_ITEM),
        SetVRAMPriority(PRIORITY_3),
        SetPriority(3),
        SetSpriteSequence(index=2, looping=False),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(VERY_FAST),
        AddZCoord1Step(),
        Pause(24),
        VisibilityOff(),
        Db(bytearray(b"\xfd\xf2")),
        Return(),
    ]
)
