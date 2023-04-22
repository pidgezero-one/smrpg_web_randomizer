"""A0661_PIPE_VAULT_JUMPING_CHOMPWEED"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        SetSequenceSpeed(NORMAL, identifier="ACTION_661_set_animation_speed_1"),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO,
            usually=0,
            tiles=2,
            destinations=["ACTION_661_set_animation_speed_5"],
        ),
        Pause(1),
        Jmp(["ACTION_661_set_animation_speed_1"]),
        SetSequenceSpeed(FAST, identifier="ACTION_661_set_animation_speed_5"),
        JumpToHeight(height=64, silent=True),
        Pause(1, identifier="ACTION_661_pause_7"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_661_pause_7"]),
        Jmp(["ACTION_661_set_animation_speed_1"]),
    ]
)
