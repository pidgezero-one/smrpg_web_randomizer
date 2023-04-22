"""A0658_PIPE_VAULT_THWOMP_ROOM_SHAKE_CAMERA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(FASTEST),
        WalkSouthPixels(8),
        SetBit(TEMP_7043_2),
        WalkNorthPixels(16),
        WalkSouthPixels(16),
        WalkNorthPixels(12),
        WalkSouthPixels(8),
        ClearBit(TEMP_7043_2),
        WalkNorthPixels(8),
        WalkSouthPixels(6),
        WalkNorthPixels(4),
        WalkSouthPixels(4),
        WalkNorthPixels(2),
        Return(),
    ]
)
