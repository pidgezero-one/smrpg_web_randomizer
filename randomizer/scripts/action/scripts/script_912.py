"""A0912_POOF_WHEN_MIMIC_3_DEFEATED"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FloatingOff(),
        VisibilityOff(),
        SetSpriteSequence(index=4, is_sequence=True, looping=True),
        Pause(9),
        VisibilityOn(),
        Pause(1, identifier="ACTION_912_pause_5"),
        JmpIfBitClear(MIMIC_3_CLEARED, ["ACTION_912_pause_5"]),
        JmpIfBitSet(RUN_AWAY, ["ACTION_912_pause_10"]),
        SetSpriteSequence(index=6, is_sequence=True, looping=True),
        Pause(18),
        Pause(6, identifier="ACTION_912_pause_10"),
        VisibilityOff(),
        Return(),
    ]
)
