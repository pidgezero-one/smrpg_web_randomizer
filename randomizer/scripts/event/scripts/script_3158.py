# pylint: disable=C0301

"""E3158_ITEM_BEHIND_SHIP_UPPER_STAIRS_TILE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SHIP_STAIRWAY_FREESTANDING_ITEM_OBTAINED, ["EVENT_3158_ret_8"]),
        SetBit(SHIP_STAIRWAY_FREESTANDING_ITEM_OBTAINED),
        Set70107015ToObjectXYZ(MARIO),
        JmpToEvent(E3385_SHIP_UPPER_STAIRWAY_ITEM_PACKET_GRANT),
        Return(identifier="EVENT_3158_ret_8"),
    ]
)
