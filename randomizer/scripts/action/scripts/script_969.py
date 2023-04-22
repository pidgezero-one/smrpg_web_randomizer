"""A0969_ENDING_CREDITS_CASTLE_DIRECTOR"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(FASTEST),
        Walk1StepNorthwest(),
        Walk1StepNortheast(),
        StartLoopNTimes(5),
        SetSpriteSequence(index=4, sprite_offset=2, looping=False),
        Pause(46),
        EndLoop(),
        SetSpriteSequence(
            index=13, sprite_offset=2, is_mold=True, is_sequence=True, looping=True
        ),
        Pause(32),
        SetSpriteSequence(
            index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(56),
        ResetProperties(),
        SetWalkingSpeed(FAST),
        SetSequenceSpeed(VERY_FAST),
        WalkSouthwestSteps(2),
        WalkSouthwestPixels(8),
        Walk1StepNorthwest(),
        Pause(64),
        SetSequenceSpeed(NORMAL),
        SetSpriteSequence(index=5, is_sequence=True, looping=True),
        Return(),
    ]
)
