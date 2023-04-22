"""A0968_FACTORY_3RD_BOSS_CONVEYOR_NPC"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShadowOff(),
        SetWalkingSpeed(SLOW),
        SetSpriteSequence(
            index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Walk1StepSoutheast(),
        SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
        WalkToXYCoords(x=16, y=113),
        ShiftToXYCoords(x=14, y=52),
        WalkSoutheastSteps(3),
        SetSpriteSequence(
            index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        ShiftToXYCoords(x=6, y=92),
        Jmp(["ACTION_965_shadow_off_0"]),
    ]
)
