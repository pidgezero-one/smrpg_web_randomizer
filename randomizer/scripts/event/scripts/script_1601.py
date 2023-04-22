# pylint: disable=C0301

"""E1601_LANDS_END_1ST_ROOM_EXIT_TO_WORLD_MAP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_708C_4, ["EVENT_1601_set_5"]),
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, OW43_LANDS_END),
        ExitToWorldMap(area=OW43_LANDS_END, bit_6=True, bit_7=True),
        Return(),
        SetVarToConst(
            CURRENT_OVERWORLD_MARKER_ID, OW37_LANDS_END, identifier="EVENT_1601_set_5"
        ),
        ExitToWorldMap(area=OW37_LANDS_END, bit_6=True, bit_7=True),
        Return(),
    ]
)
