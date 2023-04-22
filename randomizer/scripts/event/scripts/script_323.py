# pylint: disable=C0301

"""E0323_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_323_enter_area_6"]),
        JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_323_enter_area_8"]),
        JmpToEvent(E0288_UNKNOWN_ROSE_TOWN, identifier="EVENT_323_enter_area_6"),
        JmpToEvent(E0305_UNKNOWN, identifier="EVENT_323_enter_area_8"),
    ]
)
