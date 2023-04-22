"""A0258_NIMBUS_SHY_GUY_RIGHT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(NORMAL, identifier="ACTION_258_set_animation_speed_0"),
        SetSequenceSpeed(FAST),
        TurnRandomDirection(),
        JumpToHeight(height=80, silent=True),
        Pause(1, identifier="ACTION_258_pause_4"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_258_pause_4"]),
        Walk1StepNortheast(),
        TurnRandomDirection(),
        JumpToHeight(height=80, silent=True),
        Pause(1, identifier="ACTION_258_pause_9"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_258_pause_9"]),
        Walk1StepSouthwest(),
        Jmp(["ACTION_258_set_animation_speed_0"]),
    ]
)
