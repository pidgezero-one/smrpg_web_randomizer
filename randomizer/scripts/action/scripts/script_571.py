"""A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ClearBit(TEMP_7044_3),
        SetSequenceSpeed(FAST),
        SetSpriteSequence(index=10, is_sequence=True, looping=True),
        Pause(10),
        SetSpriteSequence(
            index=0,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_571_set_sprite_sequence_4",
        ),
        FixedFCoordOn(),
        SequenceLoopingOn(),
        SetWalkingSpeed(SLOW),
        WalkWestPixels(1),
        Pause(1),
        SetWalkingSpeed(VERY_SLOW),
        WalkNorthwestPixels(1),
        Pause(1),
        SetWalkingSpeed(VERY_SLOW),
        WalkSoutheastPixels(1),
        Pause(1),
        SetWalkingSpeed(VERY_SLOW),
        WalkEastPixels(1),
        Pause(1),
        SetWalkingSpeed(SLOW),
        WalkEastPixels(1),
        Pause(1),
        SetWalkingSpeed(VERY_SLOW),
        WalkNortheastPixels(1),
        Pause(1),
        SetWalkingSpeed(VERY_SLOW),
        WalkSouthwestPixels(1),
        Pause(1),
        SetWalkingSpeed(VERY_SLOW),
        WalkWestPixels(1),
        Pause(1),
        Jmp(["ACTION_571_set_sprite_sequence_4"]),
        Return(),
    ]
)
