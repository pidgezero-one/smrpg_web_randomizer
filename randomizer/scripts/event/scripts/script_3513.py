# pylint: disable=C0301

"""E3513_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_ITEM_GRANTER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_3513_pause"),
        JmpIfBitSet(MIDAS_RIVER_TUNNEL_4_PRIZE, ["EVENT_3513_jmp_2"]),
        Jmp(["EVENT_3513_pause"]),
        JmpToEvent(E0241_FREESTANDING_1_GRANT, identifier="EVENT_3513_jmp_2"),
    ]
)
