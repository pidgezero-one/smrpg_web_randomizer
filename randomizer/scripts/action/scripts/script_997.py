"""A0997_KEEP_ORIGINAL_THRONE_ROOM_RUNNING_GOOMBAS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequencePlaybackOn(identifier="ACTION_997_sequence_playback_on_0"),
        SetSequenceSpeed(VERY_FAST),
        SetWalkingSpeed(FAST),
        WalkNortheastSteps(13),
        JumpToHeight(height=21, silent=True),
        SequencePlaybackOff(),
        WalkNortheastSteps(3),
        SetWalkingSpeed(NORMAL),
        WalkNortheastSteps(1),
        SetWalkingSpeed(SLOW),
        WalkNortheastSteps(1),
        Pause(15),
        FaceSouthwest(),
        Pause(15),
        SequencePlaybackOn(),
        SetSequenceSpeed(VERY_FAST),
        SetWalkingSpeed(FAST),
        WalkSouthwestSteps(13),
        JumpToHeight(height=21, silent=True),
        SequencePlaybackOff(),
        WalkSouthwestSteps(3),
        SetWalkingSpeed(NORMAL),
        WalkSouthwestSteps(1),
        SetWalkingSpeed(SLOW),
        WalkSouthwestSteps(1),
        Pause(15),
        FaceNortheast(),
        Pause(15),
        Jmp(["ACTION_997_sequence_playback_on_0"]),
    ]
)
