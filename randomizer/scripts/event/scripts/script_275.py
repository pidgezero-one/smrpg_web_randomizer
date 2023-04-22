# pylint: disable=C0301

"""E0275_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControlsUntilReturn([]),
        StartLoopNTimes(127),
        Pause(1),
        Set7000ToTappedButton(),
        JmpIf7000AnyBitsSet(bits=[], destinations=["EVENT_275_set_9"]),
        EndLoop(),
        SetVarToConst(PRIMARY_TEMP_7000, 2),
        EnableControlsUntilReturn([]),
        Return(),
        SetVarToConst(PRIMARY_TEMP_7000, 0, identifier="EVENT_275_set_9"),
        EnableControlsUntilReturn([]),
        Return(),
    ]
)
