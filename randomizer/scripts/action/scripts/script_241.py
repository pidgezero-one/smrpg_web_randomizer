"""A0241_SMITHY_COMPONENT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(5),
        SequenceLoopingOn(),
        SetAllSpeeds(FAST),
        WalkSouthwestPixels(2),
        SetWalkingSpeed(NORMAL),
        WalkNortheastPixels(2),
        SetWalkingSpeed(SLOW),
        WalkNortheastPixels(1),
        SetSequenceSpeed(SLOW),
        SetWalkingSpeed(NORMAL),
        WalkNorthPixels(2),
        SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
        Pause(15),
        WalkSouthwestPixels(1),
        SetWalkingSpeed(FAST),
        WalkSouthPixels(2),
        Pause(7),
        SetSequenceSpeed(NORMAL),
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        Return(),
    ]
)
