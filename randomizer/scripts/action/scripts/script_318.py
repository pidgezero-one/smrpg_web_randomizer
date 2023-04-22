"""A0318_COIN_SNAKE_TAIL_BASE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(identifier="ACTION_318_visibility_off_0"),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        Pause(1, identifier="ACTION_318_pause_3"),
        Set700CToPressedButton(),
        CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_700C),
        Compare700CToVar(SECONDARY_TEMP_7024),
        JmpIfLoadedMemoryIsNot0(["ACTION_318_pause_3"]),
        VisibilityOn(),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        Pause(60),
        StartLoopNTimes(7),
        VisibilityOff(),
        Pause(2),
        VisibilityOn(),
        Pause(2),
        EndLoop(),
        VisibilityOff(),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        Return(),
    ]
)
