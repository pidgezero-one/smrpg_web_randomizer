"""A0948_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES_BEFORE_PAINT_BASE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShadowOff(identifier="ACTION_948_shadow_off_0"),
        SetWalkingSpeed(SLOW),
        WalkToXYCoords(x=11, y=38),
        WalkSoutheastPixels(11),
        SetBit(TEMP_7043_0),
        WalkToXYCoords(x=11, y=39),
        VisibilityOff(),
        WalkToXYCoords(x=16, y=49),
        ShiftToXYCoords(x=3, y=88),
        WalkSoutheastSteps(3),
        ShiftToXYCoords(x=6, y=28),
        VisibilityOn(),
        Jmp(["ACTION_948_shadow_off_0"]),
    ]
)
