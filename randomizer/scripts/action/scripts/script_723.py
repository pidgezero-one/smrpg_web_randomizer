"""A0723_MINES_RECRUITABLE_CHARACTER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceSouthwest(),
        FixedFCoordOn(),
        SequencePlaybackOn(),
        SequenceLoopingOn(),
        WalkNortheastPixels(3),
        FaceSouthwest(identifier="ACTION_723_face_southwest_5"),
        FixedFCoordOn(),
        StartLoopNTimes(3),
        WalkWestPixels(1),
        Pause(1),
        WalkEastPixels(1),
        Pause(1),
        EndLoop(),
        SetWalkingSpeed(SLOW),
        WalkNortheastPixels(8),
        Pause(80),
        JmpIfRandom1of2(["ACTION_723_face_southwest_23"]),
        FixedFCoordOff(),
        FaceNorthwest(),
        JumpToHeight(40),
        Pause(16),
        JumpToHeight(40),
        Pause(64),
        FaceSouthwest(identifier="ACTION_723_face_southwest_23"),
        FixedFCoordOn(),
        WalkSouthwestPixels(8),
        SetWalkingSpeed(NORMAL),
        Jmp(["ACTION_723_face_southwest_5"]),
    ]
)
