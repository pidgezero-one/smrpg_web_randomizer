# pylint: disable=C0301

"""E0353_BOSS_BATTLE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 28, ["EVENT_353_room_28_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 103, ["EVENT_353_room_103_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 154, ["EVENT_353_room_154_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 177, ["EVENT_353_room_177_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 192, ["EVENT_353_room_192_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 258, ["EVENT_353_room_258_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 205, ["EVENT_353_room_205_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 206, ["EVENT_353_room_206_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 223, ["EVENT_353_room_223_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 232, ["EVENT_353_room_232_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 254, ["EVENT_353_room_254_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 255, ["EVENT_353_room_255_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 266, ["EVENT_353_room_266_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 268, ["EVENT_353_room_268_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 271, ["EVENT_353_room_271_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 302, ["EVENT_353_room_302_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 315, ["EVENT_353_room_315_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 326, ["EVENT_353_room_326_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 351, ["EVENT_353_room_351_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 352, ["EVENT_353_room_352_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 393, ["EVENT_353_room_393_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 409, ["EVENT_353_room_409_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 430, ["EVENT_353_room_430_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 461, ["EVENT_353_room_461_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 469, ["EVENT_353_room_469_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 470, ["EVENT_353_room_470_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 471, ["EVENT_353_room_471_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 472, ["EVENT_353_room_472_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 496, ["EVENT_353_room_496_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 512, ["EVENT_353_room_512_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 513, ["EVENT_353_room_513_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 514, ["EVENT_353_room_514_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 515, ["EVENT_353_room_515_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 516, ["EVENT_353_room_516_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 517, ["EVENT_353_room_517_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 518, ["EVENT_353_room_518_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 519, ["EVENT_353_room_519_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 520, ["EVENT_353_room_520_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 521, ["EVENT_353_room_521_logic"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 522, ["EVENT_353_room_522_logic"]),
        Return(),
        StartBattleAtBattlefield(
            166, BF04_SUNKEN_SHIP, identifier="EVENT_353_room_28_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            184,
            BF40_SMITHY_FACTORY_DOMINO__CLOAKERS_PAD,
            identifier="EVENT_353_room_103_logic"),
        Return(),
        StartBattleAtBattlefield(
            176, BF35_MARRYMORE_CHAPEL_SANCTUARY, identifier="EVENT_353_room_154_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            167,
            BF03_SUNKEN_SHIP_KING_CALAMARIS_CELLAR,
            identifier="EVENT_353_room_177_logic"),
        Return(),
        StartBattleAtBattlefield(
            161, BF12_BOOSTER_TOWER, identifier="EVENT_353_room_192_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            177, BF17_BOOSTER_TOWER_BALCONY, identifier="EVENT_353_room_258_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            183, BF09_GRASSLANDS, identifier="EVENT_353_room_205_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            163, BF09_GRASSLANDS, identifier="EVENT_353_room_206_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            174,
            BF18_SMITHY_FACTORY_COUNT_DOWNS_PAD,
            identifier="EVENT_353_room_223_logic"),
        Return(),
        StartBattleAtBattlefield(
            181, BF01_FOREST_MAZE_BOWYERS_PAD, identifier="EVENT_353_room_232_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            173, BF41_BEAN_VALLEY_GRASSLANDS, identifier="EVENT_353_room_254_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            189, BF46_JINXS_DOJO, identifier="EVENT_353_room_255_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            209, BF07_BOWSERS_KEEP, identifier="EVENT_353_room_266_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            169, BF42_BELOME_TEMPLE, identifier="EVENT_353_room_268_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            140, BF05_MOLEVILLE_MINES, identifier="EVENT_353_room_271_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            168, BF21_KERO_SEWERS, identifier="EVENT_353_room_302_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            180, BF37_SEASIDE_TOWN_BEACH, identifier="EVENT_353_room_315_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            179, BF15_MUSHROOM_KINGDOM_CASTLE, identifier="EVENT_353_room_326_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            216, BF47_CULEX, identifier="EVENT_353_room_351_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            172,
            BF08_BARREL_VOLCANO_CZAR_DRAGONS_PAD,
            identifier="EVENT_353_room_352_logic"),
        Return(),
        StartBattleAtBattlefield(
            182, BF39_BLADE_AXEM_RANGERS, identifier="EVENT_353_room_393_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            175, BF23_NIMBUS_CASTLE_BIRDOS_ROOM, identifier="EVENT_353_room_409_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            171, BF24_NIMBUS_LAND, identifier="EVENT_353_room_430_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            235, BF07_BOWSERS_KEEP, identifier="EVENT_353_room_461_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            146, BF48_FACTORY_GROUNDS, identifier="EVENT_353_room_469_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            149, BF48_FACTORY_GROUNDS, identifier="EVENT_353_room_470_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            147, BF48_FACTORY_GROUNDS, identifier="EVENT_353_room_471_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            148, BF48_FACTORY_GROUNDS, identifier="EVENT_353_room_472_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            185, BF44_FACTORY_GROUNDS_SMITHYS_PAD, identifier="EVENT_353_room_496_logic"
        ),
        Return(),
        SetVarToConst(BATTLE_PACK_ID, 156, identifier="EVENT_353_room_512_logic"),
        StartBattleWithPackAt700E(),
        Return(),
        SetVarToConst(BATTLE_PACK_ID, 157, identifier="EVENT_353_room_513_logic"),
        StartBattleWithPackAt700E(),
        Return(),
        SetVarToConst(BATTLE_PACK_ID, 158, identifier="EVENT_353_room_514_logic"),
        StartBattleWithPackAt700E(),
        Return(),
        StartBattleAtBattlefield(
            178, BF46_JINXS_DOJO, identifier="EVENT_353_room_515_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            187, BF46_JINXS_DOJO, identifier="EVENT_353_room_516_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            188, BF46_JINXS_DOJO, identifier="EVENT_353_room_517_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            164, BF05_MOLEVILLE_MINES, identifier="EVENT_353_room_518_logic"
        ),
        Return(),
        SetVarToConst(BATTLE_PACK_ID, 207, identifier="EVENT_353_room_519_logic"),
        StartBattleWithPackAt700E(),
        Return(),
        StartBattleAtBattlefield(
            208, BF22_NIMBUS_CASTLE, identifier="EVENT_353_room_520_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            210, BF29_BOWSERS_KEEP_CHANDELIERS, identifier="EVENT_353_room_521_logic"
        ),
        Return(),
        StartBattleAtBattlefield(
            186, BF16_BOWSERS_KEEP_TURRET_EXOR, identifier="EVENT_353_room_522_logic"
        ),
        Return(),
    ]
)
