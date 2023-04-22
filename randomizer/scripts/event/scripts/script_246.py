# pylint: disable=C0301

"""E0246_CHEST_2_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 31, ["EVENT_246_room_31_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 60, ["EVENT_246_room_60_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 78, ["EVENT_246_room_78_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 81, ["EVENT_246_room_81_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 87, ["EVENT_246_room_87_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 93, ["EVENT_246_room_93_94_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 94, ["EVENT_246_room_93_94_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 100, ["EVENT_246_room_100_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 114, ["EVENT_246_room_114_498_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 121, ["EVENT_246_room_121_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 125, ["EVENT_246_room_125_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_246_room_128_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 132, ["EVENT_246_room_132_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 138, ["EVENT_246_room_138_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 144, ["EVENT_246_room_144_446_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 175, ["EVENT_246_room_175_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 184, ["EVENT_246_room_184_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 199, ["EVENT_246_room_199_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 203, ["EVENT_246_room_203_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 204, ["EVENT_246_room_204_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 234, ["EVENT_246_room_234_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 242, ["EVENT_246_room_242_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 252, ["EVENT_246_room_252_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 262, ["EVENT_246_room_262_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 270, ["EVENT_246_room_270_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 288, ["EVENT_246_room_288_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 301, ["EVENT_246_room_301_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 322, ["EVENT_246_room_322_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 331, ["EVENT_246_room_331_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 335, ["EVENT_246_room_335_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 349, ["EVENT_246_room_349_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 355, ["EVENT_246_room_355_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 366, ["EVENT_246_room_366_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 372, ["EVENT_246_room_372_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 373, ["EVENT_246_room_373_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 384, ["EVENT_246_room_384_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 405, ["EVENT_246_room_405_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 410, ["EVENT_246_room_410_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 419, ["EVENT_246_room_419_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 421, ["EVENT_246_room_421_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 425, ["EVENT_246_room_425_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 443, ["EVENT_246_room_443_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 446, ["EVENT_246_room_144_446_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 451, ["EVENT_246_room_451_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_246_room_455_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_246_room_457_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 458, ["EVENT_246_room_458_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 475, ["EVENT_246_room_475_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 492, ["EVENT_246_room_492_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 498, ["EVENT_246_room_114_498_logic"]),
        Return(),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_room_31_logic"
        ),
        JmpToEvent(E3124_MIMIC_1_CHEST, identifier="EVENT_246_room_60_logic"),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_room_78_logic"
        ),
        SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_246_room_81_logic"),
        JmpToEvent(E3401_COIN_CHEST_MULTI_HIT_2),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST, identifier="EVENT_246_room_87_logic"
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_93_94_logic",
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_room_100_logic"),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_114_498_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_121_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_125_logic",
        ),
        SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_246_room_128_logic"),
        JmpToEvent(E3401_COIN_CHEST_MULTI_HIT_2),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_132_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_138_logic",
        ),
        SetVarToConst(ITEM_ID, SuperSlap, identifier="EVENT_246_room_144_446_logic"),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST),
        SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_246_room_175_logic"),
        JmpToEvent(E3401_COIN_CHEST_MULTI_HIT_2),
        JmpToEvent(E3126_MIMIC_2_CHEST, identifier="EVENT_246_room_184_logic"),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_room_199_logic"),
        SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_246_room_203_logic"),
        JmpToEvent(E3401_COIN_CHEST_MULTI_HIT_2),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_204_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_234_logic",
        ),
        SetVarToConst(ITEM_ID, SonicCymbal, identifier="EVENT_246_room_242_logic"),
        JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_252_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_262_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_270_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_288_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_301_logic",
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_room_322_logic"),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_331_logic",
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_room_335_logic"),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_room_349_logic"),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_355_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_366_logic",
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_room_372_logic"),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_373_logic",
        ),
        SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_246_room_384_logic"),
        JmpToEvent(E3401_COIN_CHEST_MULTI_HIT_2),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_405_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_410_logic",
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_room_419_logic"),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_room_421_logic"),
        SetVarToConst(COIN_CHEST_MULTIPLIER, 0, identifier="EVENT_246_room_425_logic"),
        JmpToEvent(E3401_COIN_CHEST_MULTI_HIT_2),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_443_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_451_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_455_logic",
        ),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_457_logic",
        ),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_room_458_logic"),
        JmpToEvent(E3089_GRANT_ITEM_FROM_CHEST, identifier="EVENT_246_room_475_logic"),
        JmpToEvent(
            E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST,
            identifier="EVENT_246_room_492_logic",
        ),
    ]
)
