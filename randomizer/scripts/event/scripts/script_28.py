# pylint: disable=C0301

"""E0028_GRANT_TIER_3_CONSUMABLE_OR_EQUIP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfRandom2of3(["EVENT_28_3", "EVENT_28_3"]),
        JmpToEvent(E0011_SET_70A7_TO_RANDOM_TIER_3_EQUIP),
        JmpToEvent(E0007_SET_70A7_TO_RANDOM_TIER_3_CONSUMABLE, identifier="EVENT_28_3"),
    ]
)
