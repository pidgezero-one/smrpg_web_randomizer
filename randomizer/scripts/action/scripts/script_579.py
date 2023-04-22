"""A0579_CURTAIN_GAME_HENCHMAN_SPIN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST, identifier="ACTION_579_set_animation_speed_0"),
        SequenceLoopingOn(),
        FaceSouthwest(),
        Pause(24),
        FaceNorthwest(),
        Pause(24),
        FaceNortheast(),
        Pause(30),
        FaceNorthwest(),
        Pause(44),
        FaceSouthwest(),
        Pause(19),
        FaceNorthwest(),
        Pause(45),
        FaceNortheast(),
        Pause(36),
        FaceNorthwest(),
        Pause(20),
        Jmp(["ACTION_579_set_animation_speed_0"]),
    ]
)
