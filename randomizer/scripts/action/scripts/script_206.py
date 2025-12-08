"""A0206_CASINO_SLOT_MACHINE_ROLLER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
        SetPriority(3),
        SetSpriteSequence(
            index=0,
            is_sequence=True,
            looping=True,
            identifier="ACTION_206_set_sprite_sequence_2"),
        SetVarToConst(FACTORY_FALL_3, 0),
        JmpIfBitSet(DIRECTIONAL_7045_2, ["ACTION_206_pause_8"]),
        JmpIfBitSet(DIRECTIONAL_7045_3, ["ACTION_206_pause_10"]),
        Pause(7),
        Jmp(["ACTION_206_set_sprite_sequence_11"]),
        Pause(4, identifier="ACTION_206_pause_8"),
        Jmp(["ACTION_206_set_sprite_sequence_11"]),
        Pause(9, identifier="ACTION_206_pause_10"),
        SetSpriteSequence(
            index=3,
            is_sequence=True,
            looping=True,
            identifier="ACTION_206_set_sprite_sequence_11"),
        SetVarToConst(FACTORY_FALL_3, 2),
        JmpIfBitSet(DIRECTIONAL_7045_2, ["ACTION_206_pause_17"]),
        JmpIfBitSet(DIRECTIONAL_7045_3, ["ACTION_206_pause_19"]),
        Pause(7),
        Jmp(["ACTION_206_set_sprite_sequence_20"]),
        Pause(4, identifier="ACTION_206_pause_17"),
        Jmp(["ACTION_206_set_sprite_sequence_20"]),
        Pause(9, identifier="ACTION_206_pause_19"),
        SetSpriteSequence(
            index=1,
            is_sequence=True,
            looping=True,
            identifier="ACTION_206_set_sprite_sequence_20"),
        SetVarToConst(FACTORY_FALL_3, 1),
        JmpIfBitSet(DIRECTIONAL_7045_2, ["ACTION_206_pause_26"]),
        JmpIfBitSet(DIRECTIONAL_7045_3, ["ACTION_206_pause_28"]),
        Pause(7),
        Jmp(["ACTION_206_set_sprite_sequence_2"]),
        Pause(4, identifier="ACTION_206_pause_26"),
        Jmp(["ACTION_206_set_sprite_sequence_2"]),
        Pause(9, identifier="ACTION_206_pause_28"),
        Jmp(["ACTION_206_set_sprite_sequence_2"]),
    ]
)
