"""A0757_STAR_HILL_2ND_ROOM_EAST_GECKO"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(identifier="ACTION_757_sequence_looping_on_0"),
        ShadowOff(),
        SetWalkingSpeed(VERY_SLOW),
        WalkNortheastSteps(3),
        WalkNortheastPixels(8),
        Pause(16),
        FaceNorthwest(),
        Pause(16),
        WalkNorthwestSteps(4),
        Pause(16),
        FaceNortheast(),
        Pause(16),
        WalkNortheastSteps(8),
        Pause(16),
        FaceSoutheast(),
        Pause(16),
        WalkSoutheastSteps(8),
        Pause(16),
        FaceSouthwest(),
        Pause(16),
        WalkSouthwestSteps(8),
        Pause(16),
        FaceSoutheast(),
        Pause(16),
        WalkSoutheastSteps(4),
        Pause(16),
        FaceSouthwest(),
        Pause(16),
        WalkSouthwestSteps(4),
        Pause(16),
        FaceNorthwest(),
        Pause(16),
        WalkToXYCoords(x=21, y=39),
        Jmp(["ACTION_757_sequence_looping_on_0"]),
    ]
)
