"""A0106_BASE_NORTHEAST_MK_HENCHMAN_MOVEMENT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(NORMAL, identifier="ACTION_106_set_animation_speed_0"),
        Db(bytearray(b" \x04")),
        Db(bytearray(b"%\xc0\x06\x80\xff")),
        PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
        Walk1StepNortheast(),
        WalkNortheastPixels(11),
        BPL262728(),
        Pause(2),
        Return(),
    ]
)
