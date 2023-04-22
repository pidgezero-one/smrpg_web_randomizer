"""A0404_FOREST_TRUNK_AREA_UNDERGROUND_AMANITA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(NORMAL),
        SequenceLoopingOn(),
        JmpIfRandom2of3(
            [
                "ACTION_404_jmp_if_random_above_128_10",
                "ACTION_404_jmp_if_random_above_128_10",
            ],
            identifier="ACTION_404_jmp_if_random_above_66_2",
        ),
        FaceMario(identifier="ACTION_404_face_mario_3"),
        SetWalkingSpeed(NORMAL),
        Pause(8),
        SetVarToRandom(PRIMARY_TEMP_700C, 2),
        Inc(PRIMARY_TEMP_700C),
        ShiftZ20Steps(),
        Jmp(["ACTION_404_jmp_if_random_above_66_2"]),
        JmpIfRandom1of2(
            ["ACTION_404_set_animation_speed_13"],
            identifier="ACTION_404_jmp_if_random_above_128_10",
        ),
        TurnRandomDirection(),
        Pause(8),
        SetWalkingSpeed(SLOW, identifier="ACTION_404_set_animation_speed_13"),
        SetVarToRandom(PRIMARY_TEMP_700C, 2),
        Inc(PRIMARY_TEMP_700C),
        ShiftZ20Steps(),
        Jmp(["ACTION_404_jmp_if_random_above_66_2"]),
    ]
)
