"""A0536_MUSHROOM_WAY_SPINNING_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(VERY_FAST, identifier="ACTION_536_set_animation_speed_0"),
        SequenceLoopingOn(),
        FaceNorthwest(),
        Pause(12),
        FaceNortheast(),
        Pause(12),
        FaceSoutheast(),
        Pause(12),
        FaceSouthwest(),
        Pause(12),
        Jmp(["ACTION_536_set_animation_speed_0"]),
    ]
)
