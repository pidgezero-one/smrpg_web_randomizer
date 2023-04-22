"""A0293_MINES_FINAL_BOSS_ROOM_HENCHMAN_BASE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ObjectMemoryModifyBits(
            arg_1=0x09,
            set_bits=[5],
            clear_bits=[4, 6],
            identifier="ACTION_293_object_memory_modify_bits_0",
        ),
        FaceMario(),
        SetWalkingSpeed(FAST),
        SetSequenceSpeed(VERY_FAST),
        WalkFDirectionSteps(2),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, pixel=True),
        AddConstToVar(PRIMARY_TEMP_700C, 4),
        Mem700CAndConst(0x0007),
        FaceEast7C(),
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(FAST),
        WalkFDirectionSteps(2),
        Return(),
    ]
)
