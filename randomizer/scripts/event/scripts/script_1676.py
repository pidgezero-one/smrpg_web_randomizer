# pylint: disable=C0301

"""E1676_LANDS_END_GROTTO_ROOM_1_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeInFromBlack(sync=False),
        SetVarToConst(
            CURRENT_OVERWORLD_MARKER_ID, OW37_LANDS_END, identifier="EVENT_1676_set_8"
        ),
        JmpIfBitClear(TEMP_708C_4, ["EVENT_1676_ret_11"]),
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, OW43_LANDS_END),
        Return(identifier="EVENT_1676_ret_11"),
    ]
)
