# pylint: disable=C0301

"""E0027_GRANT_TIER_2_CONSUMABLE_OR_EQUIP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfRandom2of3(["EVENT_27_3", "EVENT_27_3"]),
        JmpToEvent(E0010_SET_70A7_TO_RANDOM_TIER_2_EQUIP),
        JmpToEvent(E0006_SET_70A7_TO_RANDOM_TIER_2_CONSUMABLE, identifier="EVENT_27_3"),
    ]
)
