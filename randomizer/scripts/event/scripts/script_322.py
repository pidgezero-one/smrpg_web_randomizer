# pylint: disable=C0301

"""E0322_MUSHROOM_KINGDOM_THRONE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Set0158Bit7Offset(0x015C),
        Set0158Bit7Offset(0x015E),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
