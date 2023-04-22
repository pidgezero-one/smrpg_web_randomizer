"""A0745_STAR_HILL_1ST_ROOM_SOUTH_GECKO"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(identifier="ACTION_745_sequence_looping_on_0"),
        ShadowOff(),
        SetWalkingSpeed(VERY_SLOW),
        WalkNortheastSteps(3),
        Pause(24),
        FaceSoutheast(),
        Pause(24),
        WalkSoutheastSteps(4),
        WalkSoutheastPixels(8),
        Pause(24),
        FaceSouthwest(),
        Pause(24),
        WalkSouthwestSteps(8),
        Pause(24),
        FaceNorthwest(),
        Pause(24),
        WalkNorthwestSteps(8),
        Pause(24),
        FaceNortheast(),
        Pause(24),
        WalkNortheastSteps(3),
        WalkNortheastPixels(4),
        Pause(24),
        FaceSoutheast(),
        Pause(24),
        WalkSoutheastSteps(3),
        WalkSoutheastPixels(8),
        Pause(24),
        FaceSoutheast(),
        Pause(24),
        WalkToXYCoords(x=10, y=107),
        Jmp(["ACTION_745_sequence_looping_on_0"]),
    ]
)
