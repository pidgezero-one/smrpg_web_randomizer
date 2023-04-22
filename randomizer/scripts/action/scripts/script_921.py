"""A0921_SEQ_1_FALLING"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FloatingOn(),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        JumpToHeight(height=0, silent=True),
        Pause(1, identifier="ACTION_921_pause_5"),
        Jmp(["ACTION_921_pause_5"]),
    ]
)
