"""A0491_MUSHROOM_WAY_3_RECRUITABLE_CHARACTER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FixedFCoordOff(identifier="ACTION_491_fixed_f_coord_off_0"),
        SequenceLoopingOn(),
        FaceSoutheast(),
        Pause(9),
        FaceSouthwest(),
        Pause(9),
        Jmp(["ACTION_491_fixed_f_coord_off_0"]),
    ]
)
