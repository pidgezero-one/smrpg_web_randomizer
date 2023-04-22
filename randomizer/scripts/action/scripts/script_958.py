"""A0958_CRANE_FOR_FINAL_FACTORY_BOSS_DEFAULT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(FASTEST),
        SetPriority(3),
        SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
        WalkEastPixels(12, identifier="ACTION_958_shift_east_pixels_3"),
        SetWalkingSpeed(SLOW),
        SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
        ShiftZDownSteps(4),
        ShiftZDownPixels(3),
        Pause(32),
        SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
        Pause(11),
        SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
        Pause(8),
        SetBit(TEMP_7044_0),
        ShiftZUpSteps(3),
        WalkToXYCoords(x=3, y=88),
        SetWalkingSpeed(VERY_SLOW),
        WalkSoutheastPixels(8),
        SetWalkingSpeed(SLOW),
        ShiftZDownSteps(3),
        Pause(10),
        SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
        Pause(10),
        SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
        Pause(16),
        ShiftZUpSteps(4),
        ShiftZUpPixels(3),
        WalkToXYCoords(x=1, y=72),
        Jmp(["ACTION_958_shift_east_pixels_3"]),
    ]
)
