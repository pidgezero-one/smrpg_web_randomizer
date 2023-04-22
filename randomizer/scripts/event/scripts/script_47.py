# pylint: disable=C0301

"""E0047_GRANT_ANY_CONSUMABLE_OR_EQUIP_EXCLUDE_WORST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToRandom(PRIMARY_TEMP_7000, 3),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_47__2"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_47___2"]),
        JmpToEvent(E0027_GRANT_TIER_2_CONSUMABLE_OR_EQUIP),
        JmpToEvent(E0028_GRANT_TIER_3_CONSUMABLE_OR_EQUIP, identifier="EVENT_47__2"),
        JmpToEvent(E0029_GRANT_TIER_4_CONSUMABLE_OR_EQUIP, identifier="EVENT_47___2"),
    ]
)
