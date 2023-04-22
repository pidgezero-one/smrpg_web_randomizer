# pylint: disable=C0301

"""E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7076_0, ["EVENT_1603_ret_78_cancel"]),
        Return(),
        EndAll(identifier="EVENT_1603_ret_78_cancel"),
    ]
)
