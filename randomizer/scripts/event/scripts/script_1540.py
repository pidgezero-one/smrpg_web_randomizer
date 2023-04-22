# pylint: disable=C0301

"""E1540_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7044_7, ["EVENT_1540_fade_in_from_black_sync_2"]),
        JmpToEvent(E0081_MARIO_LANDS_SUBROUTINE),
        FadeInFromBlack(sync=True, identifier="EVENT_1540_fade_in_from_black_sync_2"),
        Return(),
    ]
)
