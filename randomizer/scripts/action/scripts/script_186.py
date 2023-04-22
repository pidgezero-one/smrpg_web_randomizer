"""A0186_CHEST_SLOT_MACHINE_ROLLER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
        SetPriority(3),
        SetVarToConst(FACTORY_FALL_3, 0, identifier="ACTION_186_set_2"),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        Pause(4),
        SetVarToConst(FACTORY_FALL_3, 2),
        SetSpriteSequence(index=3, is_sequence=True, looping=True),
        Pause(4),
        SetVarToConst(FACTORY_FALL_3, 1),
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        Pause(4),
        Jmp(["ACTION_186_set_2"]),
    ]
)
