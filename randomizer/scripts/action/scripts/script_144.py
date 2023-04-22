"""A0144_FROGFUCIUS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(120, identifier="ACTION_144_pause_0"),
        Pause(120),
        SetSpriteSequence(index=6, is_mold=True, looping=True),
        Pause(120),
        Pause(30),
        ResetProperties(),
        Pause(60),
        SetSpriteSequence(index=6, is_mold=True, looping=True),
        Pause(6),
        ResetProperties(),
        Pause(12),
        SetSpriteSequence(index=6, is_mold=True, looping=True),
        Pause(6),
        ResetProperties(),
        Pause(20),
        Pause(120),
        Pause(120),
        Pause(120),
        Pause(120),
        Jmp(["ACTION_144_pause_0"]),
    ]
)
