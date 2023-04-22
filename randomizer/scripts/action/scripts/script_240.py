"""A0240_SMITHY_COMPONENT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(index=2, is_sequence=True, looping=True),
        Pause(45),
        PlaySound(sound=SO145_BLACKSMITH_HAMMER_STRIKE, channel=4),
        SetBit(TEMP_7044_6),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        Return(),
    ]
)
