"""A0185_CHEST_SLOT_MACHINE_ROLLER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
        SetPriority(3),
        SetVarToConst(FACTORY_FALL_2, 2, identifier="ACTION_185_set_2"),
        SetSpriteSequence(index=3, is_sequence=True, looping=True),
        Pause(7),
        SetVarToConst(FACTORY_FALL_2, 1),
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        Pause(7),
        SetVarToConst(FACTORY_FALL_2, 0),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        Pause(7),
        Jmp(["ACTION_185_set_2"]),
    ]
)
