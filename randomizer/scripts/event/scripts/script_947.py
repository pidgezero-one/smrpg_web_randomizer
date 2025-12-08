# pylint: disable=C0301

"""E0947_FROGFUCIUS_HINT_MAIN_CHECKS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2730_FROGFUCIUS_OFFER_HINT,
            above_object=BOWSER,
            closable=False,
            sync=False,
            multiline=True,
            use_background=True),
        JmpIfBitClear(TOAD_IN_MUSHROOM_WAY_3, ["EVENT_991_mushroom_way"]),
        JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_947_croco1"]),
        JmpIfBitClear(MAP_BANDITS_WAY, ["EVENT_947_croco1"]),
        JmpIfBitSet(BANDITS_WAY_LIBERATED, ["EVENT_991_kingdom"]),
        JmpIfBitClear(
            MAP_BANDITS_WAY, ["EVENT_947_pando"], identifier="EVENT_947_croco1"
        ),
        JmpIfBitClear(BANDITS_WAY_LIBERATED, ["EVENT_991_bandits"]),
        RunEventAsSubroutine(
            E0989_FROGFUCIUS_HINT_OPTIONAL_9, identifier="EVENT_947_pando"
        ),
        JmpIfBitClear(SEWER_BOSS_DEFEATED, ["EVENT_991_sewer"]),
        JmpIfBitClear(MAP_FOREST_MAZE, ["EVENT_947_mines_access"]),
        JmpIfBitClear(FOREST_LIBERATED, ["EVENT_991_forest"]),
        JmpIfBitClear(
            MOLEVILLE_MINES_ENTRANCE_GATING,
            ["EVENT_947_rk+"],
            identifier="EVENT_947_mines_access"),
        JmpIfBitClear(MINES_BOSS_1_DEFEATED, ["EVENT_991_mines"]),
        JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_947_rk+"]),
        JmpIfBitSet(MINES_BACK_OPENED, ["EVENT_991_mines"]),
        StoreItemAmountTo7000(BambinoBomb),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_mines"]),
        JmpIfBitClear(
            TOWER_OPENED, ["EVENT_947_booster_recruit+"], identifier="EVENT_947_rk+"
        ),
        JmpIfBitClear(CURTAIN_MINIGAME_COMPLETED, ["EVENT_991_tower"]),
        JmpIfObjectInSpecificLevel(
            NPC_7,
            R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            ["EVENT_991_tower"]),
        Jmp(["EVENT_947_bundt"]),
        JmpIfBitSet(
            TOWER_CHARACTER_RECRUITED,
            ["EVENT_991_tower"],
            identifier="EVENT_947_booster_recruit+"),
        JmpIfBitSet(
            MARRYMORE_LIBERATED, ["EVENT_947_star_hill"], identifier="EVENT_947_bundt"
        ),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["EVENT_947_bundt_2"]),
        RunEventAsSubroutine(E0979_FROGFUCIUS_HINT_OPTIONAL_MARRYMORE),
        RunEventAsSubroutine(
            E0985_FROGFUCIUS_HINT_OPTIONAL_5, identifier="EVENT_947_bundt_2"
        ),
        JmpIfBitClear(
            STAR_HILL_CHECKED, ["EVENT_991_star_hill"], identifier="EVENT_947_star_hill"
        ),
        JmpIfBitClear(MAP_SEA, ["EVENT_947_yarid"]),
        JmpIfBitClear(SHIP_MIDBOSS_COMPLETED, ["EVENT_991_ship"]),
        RunEventAsSubroutine(E0988_FROGFUCIUS_HINT_OPTIONAL_8),
        JmpIfBitClear(SHIP_LIBERATED, ["EVENT_991_ship"]),
        JmpIfBitSet(
            SEASIDE_LIBERATED, ["EVENT_947_mokura"], identifier="EVENT_947_yarid"
        ),
        JmpIfBitSet(SEASIDE_BOSS_AVAILABLE, ["EVENT_991_seaside"]),
        JmpIfBitClear(
            LANDS_END_CLOUD_STAR_PIECE,
            ["EVENT_991_lands_end"],
            identifier="EVENT_947_mokura"),
        JmpIfBitClear(BELOME_TEMPLE_OPEN, ["EVENT_947_mtown_open"]),
        JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["EVENT_991_temple"]),
        JmpIfBitClear(
            MAP_MONSTRO_TOWN,
            ["EVENT_947_megasmilax"],
            identifier="EVENT_947_mtown_open"),
        JmpIfBitClear(DOJO_BOSS_1_DEFEATED, ["EVENT_991_monstro"]),
        JmpIfBitClear(DOJO_BOSS_2_DEFEATED, ["EVENT_991_monstro"]),
        JmpIfBitClear(DOJO_BOSS_3_DEFEATED, ["EVENT_991_monstro"]),
        JmpIfBitClear(DOJO_BOSS_4_DEFEATED, ["EVENT_991_monstro"]),
        JmpIfBitSet(WIN_CONDITION_MONSTRO_DOOR, ["EVENT_947_megasmilax"]),
        JmpIfBitSet(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_947_megasmilax"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_2, R324_MONSTRO_TOWN_OUTSIDE, ["EVENT_991_monstro"]
        ),
        StoreItemAmountTo7000(ShinyStone),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_monstro"]),
        RunEventAsSubroutine(E0986_FROGFUCIUS_HINT_OPTIONAL_6),
        JmpIfBitClear(
            BEAN_VALLEY_BOSS_DEFEATED,
            ["EVENT_991_bean"],
            identifier="EVENT_947_megasmilax"),
        RunEventAsSubroutine(E0987_FROGFUCIUS_HINT_OPTIONAL_7),
        JmpIfObjectInSpecificLevel(
            NPC_1,
            R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
            ["EVENT_991_nimbus_castle"]),
        JmpIfBitClear(UNKNOWN_TOWER_BOSS_2_FIGHT_7092_5, ["EVENT_991_nimbus_proper"]),
        StoreItemAmountTo7000(CastleKey1),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_nimbus_castle"]),
        JmpIfObjectInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["EVENT_947_is_volcano_open"]),
        JmpIfBitClear(NIMBUS_MID_BOSS_COMPLETED, ["EVENT_991_nimbus_castle"]),
        StoreItemAmountTo7000(CastleKey2),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_nimbus_castle"]),
        JmpIfObjectInSpecificLevel(
            NPC_6, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["EVENT_947_is_volcano_open"]
        ),
        JmpIfBitClear(NIMBUS_LAND_LIBERATED, ["EVENT_991_nimbus_castle"]),
        JmpIfBitClear(
            MAP_BARREL_VOLCANO,
            ["EVENT_947_is_keep_open"],
            identifier="EVENT_947_is_volcano_open"),
        JmpIfBitClear(VOLCANO_LIBERATED, ["EVENT_991_volcano"]),
        JmpIfBitClear(
            MAP_VISTA_HILL, ["EVENT_947_smithy"], identifier="EVENT_947_is_keep_open"
        ),
        JmpIfBitClear(BATTLE_DOOR_BOSS_BIT, ["EVENT_991_deep_keep"]),
        JmpIfBitClear(KEEP_BOSS_3_DEFEATED, ["EVENT_991_keep"]),
        JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE, ["EVENT_947_smithy"]),
        JmpIfBitClear(INNER_FACTORY_ROOM_4_COMPLETED, ["EVENT_991_factory"]),
        RunEventAsSubroutine(
            E0984_FROGFUCIUS_HINT_OPTIONAL_4, identifier="EVENT_947_smithy"
        ),
        JmpIfObjectInSpecificLevel(
            NPC_1, R189_MARIOS_PIPEHOUSE, ["EVENT_991_marios_pad"]
        ),
        JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_947_barrel"]),
        StoreItemAmountTo7000(RareFrogCoin),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_947_rfc_3"]),
        Jmp(["EVENT_947_barrel"]),
        Jmp(["EVENT_991_kingdom"], identifier="EVENT_947_rfc_3"),
        JmpIfBitClear(
            LANDS_END_GROTTO_BARREL_FLIPPED,
            ["EVENT_991_lands_end_secret"],
            identifier="EVENT_947_barrel"),
        JmpIfBitClear(SEWERS_FLIPPED_CHEST_OPENED, ["EVENT_991_sewer"]),
        JmpIfBitClear(MELODY_BAY_ITEM_1_GRANTED, ["EVENT_991_mb"]),
        JmpIfBitClear(MINECART_CLEARED, ["EVENT_947_rose_town_flower"]),
        JmpIfBitClear(MELODY_BAY_ITEM_2_GRANTED, ["EVENT_991_mb"]),
        JmpIfBitClear(MELODY_BAY_SONG_3_UNLOCKED, ["EVENT_947_rose_town_flower"]),
        JmpIfBitClear(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_991_mb"]),
        JmpIfObjectInSpecificLevel(
            NPC_13,
            R084_ROSE_TOWN_OUTSIDE,
            ["EVENT_991_rose_town"],
            identifier="EVENT_947_rose_town_flower"),
        JmpIfBitClear(PIPE_VAULT_GATED, ["EVENT_947_fw"]),
        JmpIfObjectInSpecificLevel(NPC_16, R034_YOSTER_ISLE, ["EVENT_991_yoster"]),
        RunEventAsSubroutine(
            E0990_FROGFUCIUS_HINT_OPTIONAL_10, identifier="EVENT_947_fw"
        ),
        JmpIfBitClear(TOWER_BOSS_2_DEFEATED, ["EVENT_947_rk"]),
        JmpIfBitSet(KNIFE_GUY_PRIZE_GRANTED, ["EVENT_947_rk"]),
        Jmp(["EVENT_991_tower"]),
        JmpIfBitClear(
            TOWER_OPENED, ["EVENT_947_booster_recruit"], identifier="EVENT_947_rk"
        ),
        JmpIfObjectInSpecificLevel(NPC_16, R034_YOSTER_ISLE, ["EVENT_991_tower"]),
        JmpIfBitSet(PORTRAIT_GAME_COMPLETED, ["EVENT_947_templekey"]),
        Jmp(["EVENT_991_tower"]),
        JmpIfBitSet(
            TOWER_CHARACTER_RECRUITED,
            ["EVENT_991_tower"],
            identifier="EVENT_947_booster_recruit"),
        JmpIfBitClear(
            MAP_MONSTRO_TOWN, ["EVENT_947_-seed"], identifier="EVENT_947_templekey"
        ),
        JmpIfObjectInSpecificLevel(
            NPC_0, R324_MONSTRO_TOWN_OUTSIDE, ["EVENT_991_monstro"]
        ),
        JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["EVENT_991_monstro"]),
        JmpIfObjectInSpecificLevel(
            NPC_3,
            R254_BEAN_VALLEY_SMILAX_AREA,
            ["EVENT_991_bean"],
            identifier="EVENT_947_-seed"),
        JmpIfBitClear(RED_CELLAR_GUARD_ITEM_GRANTED, ["EVENT_991_nimbus_castle"]),
        StoreItemAmountTo7000(CastleKey1),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_nimbus_castle"]),
        JmpIfObjectInSpecificLevel(
            NPC_10,
            R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            ["EVENT_947_end"]),
        JmpIfBitClear(NIMBUS_MID_BOSS_COMPLETED, ["EVENT_991_nimbus_castle"]),
        StoreItemAmountTo7000(CastleKey2),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_991_nimbus_castle"]),
        JmpIfObjectInSpecificLevel(
            NPC_6, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["EVENT_947_end"]
        ),
        JmpIfBitClear(NIMBUS_LAND_LIBERATED, ["EVENT_991_nimbus_castle"]),
        JmpIfObjectInSpecificLevel(
            NPC_9, R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, ["EVENT_991_nimbus_proper"]
        ),
        JmpToEvent(E0948_FROGFUCIUS_HINT_EXPANSION, identifier="EVENT_947_end"),
    ]
)
