# pylint: disable=C0301

"""E0041_GRANT_ANY_CONSUMABLE_TIER_3_CAP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToRandom(PRIMARY_TEMP_7000, 3),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_41__2"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_41___2"]),
        JmpToEvent(E0005_SET_70A7_TO_RANDOM_TIER_1_CONSUMABLE),
        JmpToEvent(
            E0006_SET_70A7_TO_RANDOM_TIER_2_CONSUMABLE, identifier="EVENT_41__2"
        ),
        JmpToEvent(
            E0007_SET_70A7_TO_RANDOM_TIER_3_CONSUMABLE, identifier="EVENT_41___2"
        ),
    ]
)
