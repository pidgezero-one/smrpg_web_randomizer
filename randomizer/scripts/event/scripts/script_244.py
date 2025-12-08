# pylint: disable=C0301

"""E0244_CHEST_4_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 81, ["EVENT_244_room_81_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 144, ["EVENT_244_room_144_446_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 234, ["EVENT_244_room_234_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 322, ["EVENT_244_room_322_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 421, ["EVENT_244_room_421_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 425, ["EVENT_244_room_425_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 443, ["EVENT_244_room_443_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 446, ["EVENT_244_room_144_446_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_244_room_455_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_244_room_457_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 458, ["EVENT_244_room_458_logic"]),
        Return(),
        SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_244_room_81_logic"),
        JmpToEvent(E3403_COIN_CHEST_MULTI_HIT_4),
        SetVarToConst(ITEM_ID, StarGun, identifier="EVENT_244_room_144_446_logic"),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_244_room_234_logic"),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_244_room_322_logic"),
        SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_244_room_421_logic"),
        JmpToEvent(E3403_COIN_CHEST_MULTI_HIT_4),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_244_room_425_logic"),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_244_room_443_logic"),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_244_room_455_logic"),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_244_room_457_logic"),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_244_room_458_logic"),
    ]
)
