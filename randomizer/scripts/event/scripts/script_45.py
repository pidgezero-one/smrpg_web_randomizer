# pylint: disable=C0301

"""E0045_GRANT_ANY_CONSUMABLE_EXCLUDE_WORST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToRandom(PRIMARY_TEMP_7000, 3),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_45__2"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_45___2"]),
        JmpToEvent(E0006_SET_70A7_TO_RANDOM_TIER_2_CONSUMABLE),
        JmpToEvent(
            E0007_SET_70A7_TO_RANDOM_TIER_3_CONSUMABLE, identifier="EVENT_45__2"
        ),
        JmpToEvent(
            E0008_SET_70A7_TO_RANDOM_TIER_4_CONSUMABLE, identifier="EVENT_45___2"
        ),
    ]
)
