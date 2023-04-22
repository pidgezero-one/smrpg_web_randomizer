# pylint: disable=C0301

"""E3239_SHIP_OPEN_DOOR_TO_ROOM_BEHIND_BOX_WALL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_3239_ret_3"]),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_1),
        Return(identifier="EVENT_3239_ret_3"),
    ]
)
