"""A0744_STAR_HILL_1ST_ROOM_NORTH_GECKO"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(identifier="ACTION_744_sequence_looping_on_0"),
        ShadowOff(),
        SetWalkingSpeed(VERY_SLOW),
        WalkSouthwestSteps(4),
        WalkSouthwestPixels(7),
        Pause(32),
        FaceNorthwest(),
        Pause(24),
        WalkNorthwestSteps(3),
        WalkNorthwestPixels(7),
        Pause(16),
        FaceNortheast(),
        FixedFCoordOn(),
        SetWalkingSpeed(FASTEST),
        WalkSouthwestPixels(3),
        SetSequenceSpeed(SLOW),
        Pause(384),
        WalkNortheastPixels(3),
        FixedFCoordOff(),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(VERY_SLOW),
        Walk1StepSouthwest(),
        WalkSoutheastSteps(8),
        WalkSoutheastPixels(5),
        SetSequenceSpeed(SLOW),
        Pause(32),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(SLOW),
        WalkNortheastSteps(4),
        WalkNortheastPixels(7),
        Pause(32),
        SequenceLoopingOff(),
        Pause(64),
        SetWalkingSpeed(VERY_SLOW),
        WalkToXYCoords(x=12, y=71),
        Jmp(["ACTION_744_sequence_looping_on_0"]),
    ]
)
