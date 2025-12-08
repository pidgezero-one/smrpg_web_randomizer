# pylint: disable=C0301

"""E1892_ABYSS_BOSS_1_DEFEATED_TEMP_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            UNKNOWN_DIRECTIONAL_BIT_1, ["EVENT_1892_fade_in_from_black_async_6"]
        ),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=14, y=9, z=18, direction=EAST),
                ASJumpToHeight(height=0, silent=True),
            ]),
        FadeInFromBlack(sync=True),
        Return(),
        FadeInFromBlack(sync=False, identifier="EVENT_1892_fade_in_from_black_async_6"),
        ClearBit(UNKNOWN_DIRECTIONAL_BIT_1),
        Return(),
    ]
)
