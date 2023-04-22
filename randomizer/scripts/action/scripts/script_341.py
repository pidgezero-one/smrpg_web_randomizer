"""A0341_SHIP_1ST_STAIRWAY_RATS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(3),
        Set700CToPressedButton(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 24, ["ACTION_341_set_animation_speed_22"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 23, ["ACTION_341_set_animation_speed_16"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 22, ["ACTION_341_set_animation_speed_8"]
        ),
        SetWalkingSpeed(FAST, identifier="ACTION_341_set_animation_speed_5"),
        SetSequenceSpeed(VERY_FAST),
        WalkSoutheastSteps(5),
        SetAllSpeeds(NORMAL, identifier="ACTION_341_set_animation_speed_8"),
        Walk1StepSoutheast(),
        Walk1StepSouthwest(),
        SetWalkingSpeed(FAST),
        SetSequenceSpeed(VERY_FAST),
        WalkSouthwestSteps(3),
        SetAllSpeeds(NORMAL),
        Walk1StepSoutheast(),
        SetWalkingSpeed(SLOW, identifier="ACTION_341_set_animation_speed_16"),
        SetSequenceSpeed(FAST),
        WalkNortheastSteps(3),
        SetAllSpeeds(NORMAL),
        WalkNortheastSteps(2),
        WalkNorthwestSteps(2),
        SetWalkingSpeed(SLOW, identifier="ACTION_341_set_animation_speed_22"),
        SetSequenceSpeed(FAST),
        WalkNorthwestSteps(5),
        SetWalkingSpeed(NORMAL),
        Walk1StepSouthwest(),
        Jmp(["ACTION_341_set_animation_speed_5"]),
    ]
)
