"""A0572_MELODY_BAY_TADPOLE_INCORRECT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST),
        SetSpriteSequence(index=10, is_sequence=True, looping=True),
        Pause(12),
        VisibilityOff(),
        Return(),
    ]
)
