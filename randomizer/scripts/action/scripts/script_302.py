"""A0302_MINES_FINAL_BOSS_ROOM_TINY_HENCHMAN_EXPLODE_BASE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(10, identifier="ACTION_302_pause_0"),
        SetSolidityBits(cant_walk_through=True),
        SetSolidityBits(bit_4=True),
        SetSpriteSequence(index=2, is_sequence=True, looping=False),
        PlaySound(sound=SO089_LIT_FUSE, channel=4),
        Pause(16),
        StopSound(),
        SetBit(TEMP_7043_0),
        Pause(1),
        ClearBit(TEMP_7043_0),
        Pause(3),
        VisibilityOff(),
        ClearBit(TEMP_7043_1),
        Pause(12),
        ClearSolidityBits(cant_walk_through=True),
        ClearSolidityBits(bit_4=True),
        TransferToXYZF(x=4, y=55, z=0, direction=EAST),
        Return(),
    ]
)
