# pylint: disable=C0301

"""E0066_PIPE_DOWN_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_707C_0, ["EVENT_66_end_all_11"]),
        Set7000ToTappedButton(),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_66_end_all_11"]),
        Set7000ToPressedButton(),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_66_end_all_11"]),
        CompareVarToConst(X_COORD_2, 256),
        JmpIfComparisonResultIsLesser(["EVENT_66_set_action_script_async_9"]),
        CopyVarToVar(from_var=X_COORD_2, to_var=Y_COORD_2),
        VarShiftLeft(X_COORD_2, 8),
        SetAsyncActionScript(
            MARIO, A0011_GO_DOWN_PIPE, identifier="EVENT_66_set_action_script_async_9"
        ),
        Return(),
        EndAll(identifier="EVENT_66_end_all_11"),
    ]
)
