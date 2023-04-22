"""A0036_WIGGLER_GOING_TO_STUMP_TO_SLEEP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetVarToConst(SECONDARY_TEMP_7024, 20),
        SetWalkingSpeed(NORMAL),
        Set700CToPressedButton(),
        DecVarFrom700C(SECONDARY_TEMP_7024),
        Mem700CAndConst(0x0003),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_36_load_mem_11"]),
        Db(bytearray(b"\xc8\x07")),
        AddConstToVar(Z_COORD_2, 128),
        AddConstToVar(X_COORD_2, 64),
        TransferTo70167018701A(),
        Jmp(["ACTION_36_visibility_on_16"]),
        LoadMemory(PRIMARY_TEMP_700C, identifier="ACTION_36_load_mem_11"),
        Pause(8),
        EndLoop(),
        Pause(1),
        SetSequenceSpeed(FAST),
        VisibilityOn(identifier="ACTION_36_visibility_on_16"),
        SetPriority(3),
        WalkNorthwestSteps(4),
        Jmp(["ACTION_32_shift_z_up_steps_20"]),
        Return(),
    ]
)
