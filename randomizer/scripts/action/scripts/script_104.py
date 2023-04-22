"""A0104_BASE_SOUTHWEST_MK_HENCHMAN_MOVEMENT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(NORMAL, identifier="ACTION_104_set_animation_speed_0"),
        Db(bytearray(b" \x04")),
        Db(bytearray(b"%\xc0\x06\x80\xff")),
        PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
        Walk1StepSouthwest(),
        WalkSouthwestPixels(11),
        BPL262728(),
        Pause(2),
        Return(),
    ]
)
