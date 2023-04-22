"""A0342_SHIP_2ND_STAIRWAY_RATS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(3),
        Set700CToPressedButton(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 23, ["ACTION_342_set_animation_speed_15"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 22, ["ACTION_342_set_animation_speed_12"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 21, ["ACTION_342_set_animation_speed_8"]
        ),
        SetWalkingSpeed(FAST, identifier="ACTION_342_set_animation_speed_5"),
        SetSequenceSpeed(VERY_FAST),
        WalkSouthwestSteps(7),
        SetAllSpeeds(NORMAL, identifier="ACTION_342_set_animation_speed_8"),
        WalkSouthwestSteps(2),
        Walk1StepSoutheast(),
        WalkNortheastSteps(2),
        SetWalkingSpeed(SLOW, identifier="ACTION_342_set_animation_speed_12"),
        SetSequenceSpeed(FAST),
        WalkNortheastSteps(7),
        SetAllSpeeds(NORMAL, identifier="ACTION_342_set_animation_speed_15"),
        WalkNortheastSteps(3),
        Walk1StepNorthwest(),
        WalkSouthwestSteps(3),
        Jmp(["ACTION_342_set_animation_speed_5"]),
    ]
)
