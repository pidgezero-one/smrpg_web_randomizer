"""A0534_MUSHROOM_WAY_GUARD_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceSouthwest(identifier="ACTION_534_face_southwest_0"),
        Pause(40),
        SequenceLoopingOn(),
        SetSequenceSpeed(VERY_FAST),
        Pause(90),
        SequenceLoopingOff(),
        Pause(40),
        FaceSoutheast(),
        Pause(20),
        Jmp(["ACTION_534_face_southwest_0"]),
        Return(),
    ]
)
