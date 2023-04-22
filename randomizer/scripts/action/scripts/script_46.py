"""A0046_MIDAS_WATERFALL_SPLASH"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65517),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(3),
        EndLoop(),
        SequenceLoopingOn(),
        Pause(414),
        VisibilityOff(),
        Return(),
    ]
)
