"""A0174_MIDAS_UPPER_TUNNEL_BOOS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        SetPriority(3),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65517),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(10),
        EndLoop(),
        AddZCoord1Step(identifier="ACTION_174_add_z_coord_1_step_7"),
        Pause(10),
        DecZCoord1Step(),
        Pause(27),
        Jmp(["ACTION_174_add_z_coord_1_step_7"]),
    ]
)
