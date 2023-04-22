# pylint: disable=C0301

"""E0051_GRANT_ANY_CONSUMABLE_EXCLUDE_WORST_CUSTOM_CAP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=FLAG_COLLECTION_7088, to_var=PRIMARY_TEMP_7000),
        Mem7000AndConst(0x0018),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_51_tier4"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_51_tier3"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_51_tier2"]),
        JmpToEvent(E0005_SET_70A7_TO_RANDOM_TIER_1_CONSUMABLE),
        JmpToEvent(
            E0006_SET_70A7_TO_RANDOM_TIER_2_CONSUMABLE, identifier="EVENT_51_tier2"
        ),
        JmpToEvent(
            E0048_GRANT_ANY_CONSUMABLE_EXCLUDE_WORST_TIER_3_CAP,
            identifier="EVENT_51_tier3",
        ),
        JmpToEvent(
            E0045_GRANT_ANY_CONSUMABLE_EXCLUDE_WORST, identifier="EVENT_51_tier4"
        ),
    ]
)
