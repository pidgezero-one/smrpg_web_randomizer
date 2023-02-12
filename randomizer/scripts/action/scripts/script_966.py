# A0966_FACTORY_3RD_BOSS_CONVEYOR_NPC

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShadowOn(),
        SetWalkingSpeed(SLOW),
        SetSpriteSequence(
            index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        WalkToXYCoords(x=9, y=99),
        ShiftSoutheastPixels(9),
        SetBit(TEMP_7043_1),
        WalkToXYCoords(x=12, y=105),
        ShiftSoutheastPixels(9),
        SetBit(TEMP_7043_2),
        Walk1StepSoutheast(),
        SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
        WalkToXYCoords(x=16, y=113),
        ShiftToXYCoords(x=14, y=52),
        ShiftSoutheastSteps(3),
        SetSpriteSequence(
            index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        ShiftToXYCoords(x=6, y=92),
        Jmp(["ACTION_965_shadow_off_0"]),
    ]
)
