"""A0014_FLOATING_CHEST"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65517),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(7),
        EndLoop(),
        Pause(2, identifier="ACTION_14_pause_5"),
        ShiftZDownPixels(1),
        Pause(4),
        ShiftZDownPixels(1),
        Pause(13),
        ShiftZUpPixels(1),
        Pause(4),
        ShiftZUpPixels(1),
        Pause(2),
        ShiftZUpPixels(1),
        Pause(4),
        ShiftZUpPixels(1),
        Pause(13),
        ShiftZDownPixels(1),
        Pause(4),
        ShiftZDownPixels(1),
        Jmp(["ACTION_14_pause_5"]),
    ]
)
