# pylint: disable=C0301

"""E0029_GRANT_TIER_4_CONSUMABLE_OR_EQUIP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfRandom2of3(["EVENT_29_3", "EVENT_29_3"]),
        JmpToEvent(E0012_SET_70A7_TO_RANDOM_TIER_4_EQUIP),
        JmpToEvent(E0008_SET_70A7_TO_RANDOM_TIER_4_CONSUMABLE, identifier="EVENT_29_3"),
    ]
)
