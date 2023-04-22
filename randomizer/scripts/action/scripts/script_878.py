"""A0878_MONSTRO_GOOMBETTE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(NORMAL, identifier="ACTION_878_set_animation_speed_0"),
        SequenceLoopingOn(),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, pixel=True),
        CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=SECONDARY_TEMP_7024),
        FaceSouthwest7D(),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, pixel=True),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_878_face_east_7C_8"]),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_700C),
        FaceEast7C(identifier="ACTION_878_face_east_7C_8"),
        Pause(1),
        Jmp(["ACTION_878_set_animation_speed_0"]),
    ]
)
