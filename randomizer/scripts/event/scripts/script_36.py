# pylint: disable=C0301

"""E0036_GRANT_ANY_CONSUMABLE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToRandom(PRIMARY_TEMP_7000, 4),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_36__2"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_36___2"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_36____2"]),
        JmpToEvent(E0008_SET_70A7_TO_RANDOM_TIER_4_CONSUMABLE),
        JmpToEvent(
            E0007_SET_70A7_TO_RANDOM_TIER_3_CONSUMABLE, identifier="EVENT_36__2"
        ),
        JmpToEvent(
            E0006_SET_70A7_TO_RANDOM_TIER_2_CONSUMABLE, identifier="EVENT_36___2"
        ),
        JmpToEvent(
            E0005_SET_70A7_TO_RANDOM_TIER_1_CONSUMABLE, identifier="EVENT_36____2"
        ),
    ]
)
