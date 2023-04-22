"""A0963_FACTORY_3RD_BOSS_MID_HAMMER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShadowOff(),
        SetWalkingSpeed(FASTEST),
        WalkSouthwestPixels(6),
        Pause(1, identifier="ACTION_963_pause_3"),
        JmpIfBitClear(TEMP_7043_1, ["ACTION_963_pause_3"]),
        SetSpriteSequence(index=3, looping=False),
        Pause(32),
        SetBit(TEMP_7043_4),
        Pause(4),
        ClearBit(TEMP_7043_1),
        Jmp(["ACTION_963_pause_3"]),
    ]
)
