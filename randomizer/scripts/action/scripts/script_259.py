"""A0259_NIMBUS_PINWHEEL_RIGHT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfRandom1of2(
            ["ACTION_259_pause_2"], identifier="ACTION_259_jmp_if_random_above_128_0"
        ),
        Pause(60),
        Pause(30, identifier="ACTION_259_pause_2"),
        SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
        SetBit(TEMP_7043_6),
        Pause(120),
        ClearBit(TEMP_7043_6),
        ResetProperties(),
        Jmp(["ACTION_259_jmp_if_random_above_128_0"]),
    ]
)
