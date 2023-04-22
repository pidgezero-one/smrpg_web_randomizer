# pylint: disable=C0301

"""E0048_GRANT_ANY_CONSUMABLE_EXCLUDE_WORST_TIER_3_CAP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToRandom(PRIMARY_TEMP_7000, 2),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_48__2"]),
        JmpToEvent(E0006_SET_70A7_TO_RANDOM_TIER_2_CONSUMABLE),
        JmpToEvent(
            E0007_SET_70A7_TO_RANDOM_TIER_3_CONSUMABLE, identifier="EVENT_48__2"
        ),
    ]
)
