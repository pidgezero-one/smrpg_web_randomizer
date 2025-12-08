"""A0660_VARIOUS_YELLOW_PLATFORMS_WITHOUT_XY_MOVEMENT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToCurrentLevel(identifier="ACTION_660_set_700C_to_current_level_0"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 378, ["ACTION_660_shadow_off_9"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 381, ["ACTION_660_shadow_off_9"]),
        SetWalkingSpeed(SLOW),
        ShiftZUpSteps(2),
        Pause(30),
        ShiftZDownSteps(2),
        Pause(30),
        Jmp(["ACTION_660_set_700C_to_current_level_0"]),
        ShadowOff(identifier="ACTION_660_shadow_off_9"),
        SetAllSpeeds(SLOW),
        SequenceLoopingOn(),
        ShiftZUpSteps(3),
        JmpIfRandom1of2(["ACTION_660_shift_z_up_steps_15"]),
        JmpToSubroutine(["ACTION_660_set_700C_to_object_coord_25"]),
        ShiftZUpSteps(3, identifier="ACTION_660_shift_z_up_steps_15"),
        JmpIfRandom1of2(["ACTION_660_shift_z_down_steps_18"]),
        JmpToSubroutine(["ACTION_660_set_700C_to_object_coord_25"]),
        ShiftZDownSteps(3, identifier="ACTION_660_shift_z_down_steps_18"),
        JmpIfRandom1of2(["ACTION_660_shift_z_down_steps_21"]),
        JmpToSubroutine(["ACTION_660_set_700C_to_object_coord_25"]),
        ShiftZDownSteps(3, identifier="ACTION_660_shift_z_down_steps_21"),
        JmpIfRandom1of2(["ACTION_660_shadow_off_9"]),
        JmpToSubroutine(["ACTION_660_set_700C_to_object_coord_25"]),
        Jmp(["ACTION_660_shadow_off_9"]),
        Set700CToObjectCoord(
            target_npc=DUMMY_0X07,
            coord=COORD_F,
            pixel=True,
            identifier="ACTION_660_set_700C_to_object_coord_25"),
        Pause(30),
        TurnRandomDirection(),
        Pause(30),
        TurnRandomDirection(),
        Pause(30),
        FaceEast7C(),
        Return(),
    ]
)
