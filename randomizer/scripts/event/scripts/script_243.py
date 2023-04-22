# pylint: disable=C0301

"""E0243_CHEST_5_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 81, ["EVENT_243_room_81_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 144, ["EVENT_243_room_144_446_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 234, ["EVENT_243_room_234_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 446, ["EVENT_243_room_144_446_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_243_room_455_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_243_room_457_logic"]),
        Return(),
        SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_243_room_81_logic"),
        JmpToEvent(E3404_COIN_CHEST_MULTI_HIT_5),
        SetVarToConst(ITEM_ID, RockCandy, identifier="EVENT_243_room_144_446_logic"),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_243_room_234_logic",
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_243_room_455_logic"),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_243_room_457_logic"),
    ]
)
