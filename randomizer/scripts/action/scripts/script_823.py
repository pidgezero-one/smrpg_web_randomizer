"""A0823_PLAYER_RESET_IN_SKY_BRIDGE_ROOM"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(1, identifier="ACTION_823_pause_0"),
        Set700CToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
        CompareVarToConst(PRIMARY_TEMP_700C, 2176),
        JmpIfComparisonResultIsGreaterOrEqual(["ACTION_823_pause_0"]),
        Set700CToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True),
        CompareVarToConst(PRIMARY_TEMP_700C, 9216),
        JmpIfComparisonResultIsLesser(["ACTION_823_object_memory_modify_bits_13"]),
        Set700CToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True),
        CompareVarToConst(PRIMARY_TEMP_700C, 13056),
        JmpIfComparisonResultIsGreaterOrEqual(
            ["ACTION_823_object_memory_modify_bits_13"]
        ),
        SetPriority(0),
        ShadowOff(),
        Jmp(["ACTION_823_pause_0"]),
        ObjectMemoryModifyBits(
            arg_1=0x09,
            set_bits=[5],
            clear_bits=[4, 6],
            identifier="ACTION_823_object_memory_modify_bits_13"),
        ShadowOn(),
        Jmp(["ACTION_823_pause_0"]),
    ]
)
