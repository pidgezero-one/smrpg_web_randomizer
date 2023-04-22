# pylint: disable=C0301

"""E0049_GRANT_ANY_EQUIP_EXCLUDE_WORST_TIER_3_CAP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToRandom(PRIMARY_TEMP_7000, 2),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_49__2"]),
        JmpToEvent(E0010_SET_70A7_TO_RANDOM_TIER_2_EQUIP),
        JmpToEvent(E0011_SET_70A7_TO_RANDOM_TIER_3_EQUIP, identifier="EVENT_49__2"),
    ]
)
