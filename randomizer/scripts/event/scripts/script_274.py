# pylint: disable=C0301

"""E0274_CHECK_IF_HAVE_ENOUGH_COINS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(INSUFFICIENT_COINS),
        StoreCoinCountTo7000(),
        Compare7000ToVar(SECONDARY_TEMP_7024),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_274_ret_8"]),
        SetBit(INSUFFICIENT_COINS),
        JmpIfBitClear(UNKNOWN_7049_4, ["EVENT_274_ret_8"]),
        RunDialog(
            dialog_id=DI0520_LITTLE_SHORT_ON_COINS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        ClearBit(UNKNOWN_7049_4),
        Return(identifier="EVENT_274_ret_8"),
    ]
)
