# pylint: disable=C0301

"""E0059_GRANT_ANY_EQUIP_OR_CONSUMABLE_CUSTOM_CAP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=FLAG_COLLECTION_7088, to_var=PRIMARY_TEMP_7000),
        Mem7000AndConst(0x0018),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_59_tier4"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_59_tier3"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_59_tier2"]),
        JmpToEvent(E0026_GRANT_TIER_1_CONSUMABLE_OR_EQUIP),
        JmpToEvent(
            E0044_GRANT_ANY_CONSUMABLE_OR_EQUIP_TIER_2_CAP, identifier="EVENT_59_tier2"
        ),
        JmpToEvent(
            E0039_GRANT_ANY_CONSUMABLE_OR_EQUIP_TIER_3_CAP, identifier="EVENT_59_tier3"
        ),
        JmpToEvent(E0038_GRANT_ANY_CONSUMABLE_OR_EQUIP, identifier="EVENT_59_tier4"),
    ]
)
