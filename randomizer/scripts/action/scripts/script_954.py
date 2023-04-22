"""A0954_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(SLOW),
        SetSpriteSequence(
            index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        WalkToXYCoords(x=16, y=94),
        ShiftToXYCoords(x=8, y=35),
        SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
        WalkSoutheastSteps(5),
        Jmp(["ACTION_953_set_animation_speed_0"]),
    ]
)
