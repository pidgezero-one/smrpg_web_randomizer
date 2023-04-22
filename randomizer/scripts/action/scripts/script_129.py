"""A0129_WALLET_TOAD_OCCUPIED"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST, identifier="ACTION_129_set_animation_speed_0"),
        WalkSouthwestPixels(22),
        Walk1StepSouthwest(),
        Walk1StepSoutheast(),
        Walk1StepSoutheast(),
        WalkSoutheastPixels(11),
        WalkNortheastSteps(2),
        WalkNortheastPixels(22),
        WalkNorthwestPixels(11),
        WalkNorthwestSteps(2),
        Walk1StepSouthwest(),
        FaceSoutheast(),
        Pause(1, identifier="ACTION_129_pause_12"),
        JmpIfBitSet(TEMP_7044_5, ["ACTION_129_set_animation_speed_0"]),
        Jmp(["ACTION_129_pause_12"]),
    ]
)
