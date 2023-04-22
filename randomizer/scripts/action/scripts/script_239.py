"""A0239_ENDING_CREDITS_CROCO"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(index=2, is_sequence=True, looping=True),
        Pause(18),
        ResetProperties(),
        Pause(10),
        FaceSoutheast(),
        Pause(2),
        FaceNortheast(),
        SetWalkingSpeed(VERY_SLOW),
        WalkNortheastSteps(2),
        WalkNortheastPixels(10),
        FaceNorthwest(),
        Pause(90),
        WalkNortheastSteps(6),
        Return(),
    ]
)
