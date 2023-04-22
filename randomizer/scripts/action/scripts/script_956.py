"""A0956_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
        Pause(56),
        Jmp(["ACTION_953_set_animation_speed_0"]),
    ]
)
