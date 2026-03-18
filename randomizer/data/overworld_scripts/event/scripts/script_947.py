# E0947_FROGFUCIUS_HINT_MAIN_CHECKS
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_rows import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *

script = EventScript([
	RunDialog(dialog_id=DI2730_FROGFUCIUS_OFFER_HINT, above_object=BOWSER, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfBitClear(TOAD_IN_MUSHROOM_WAY_3, ["mushroom_way_hint_text"]),
	JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_947_jmp_if_bit_clear_5"]),
	JmpIfBitClear(MAP_BANDITS_WAY, ["EVENT_947_jmp_if_bit_clear_5"]),
	JmpIfBitSet(BANDITS_WAY_LIBERATED, ["mushroom_kingdom_hint_text"]),
	JmpIfBitClear(MAP_BANDITS_WAY, ["EVENT_947_run_event_as_subroutine_7"], identifier="EVENT_947_jmp_if_bit_clear_5"),
	JmpIfBitClear(BANDITS_WAY_LIBERATED, ["bandits_way_hint_text"]),
	RunEventAsSubroutine(E0989_FROGFUCIUS_HINT_OPTIONAL_9, identifier="EVENT_947_run_event_as_subroutine_7"),
	JmpIfBitClear(SEWER_BOSS_DEFEATED, ["kero_sewers_hint_text"]),
	JmpIfBitClear(MAP_FOREST_MAZE, ["EVENT_947_jmp_if_bit_clear_11"]),
	JmpIfBitClear(FOREST_LIBERATED, ["forest_maze_hint_text"]),
	JmpIfBitClear(MOLEVILLE_MINES_ENTRANCE_GATING, ["EVENT_947_jmp_if_bit_clear_17"], identifier="EVENT_947_jmp_if_bit_clear_11"),
	JmpIfBitClear(MINES_BOSS_1_DEFEATED, ["mines_hint_text"]),
	JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_947_jmp_if_bit_clear_17"]),
	JmpIfBitSet(MINES_BACK_OPENED, ["mines_hint_text"]),
	StoreItemAmountTo7000(BambinoBombItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["mines_hint_text"]),
	JmpIfBitClear(TOWER_OPENED, ["EVENT_947_jmp_if_bit_set_21"], identifier="EVENT_947_jmp_if_bit_clear_17"),
	JmpIfBitClear(CURTAIN_MINIGAME_COMPLETED, ["booster_tower_hint_text"]),
	JmpIfObjectInSpecificLevel(NPC_7, R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, ["booster_tower_hint_text"]),
	Jmp(["EVENT_947_jmp_if_bit_set_22"]),
	JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"], identifier="EVENT_947_jmp_if_bit_set_21"),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_947_jmp_if_bit_clear_26"], identifier="EVENT_947_jmp_if_bit_set_22"),
	JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["EVENT_947_run_event_as_subroutine_25"]),
	RunEventAsSubroutine(E0979_FROGFUCIUS_HINT_OPTIONAL_MARRYMORE),
	RunEventAsSubroutine(E0985_FROGFUCIUS_HINT_OPTIONAL_5, identifier="EVENT_947_run_event_as_subroutine_25"),
	JmpIfBitClear(STAR_HILL_CHECKED, ["star_hill_hint_text"], identifier="EVENT_947_jmp_if_bit_clear_26"),
	JmpIfBitClear(MAP_SEA, ["EVENT_947_jmp_if_bit_set_31"]),
	JmpIfBitClear(SHIP_MIDBOSS_COMPLETED, ["sunken_ship_hint_text"]),
	RunEventAsSubroutine(E0988_FROGFUCIUS_HINT_OPTIONAL_8, identifier="EVENT_947_run_event_as_subroutine_29"),
	JmpIfBitClear(SHIP_LIBERATED, ["sunken_ship_hint_text"]),
	JmpIfBitSet(SEASIDE_LIBERATED, ["EVENT_947_jmp_if_bit_clear_33"], identifier="EVENT_947_jmp_if_bit_set_31"),
	JmpIfBitSet(SEASIDE_BOSS_AVAILABLE, ["seaside_town_hint_text"]),
	JmpIfBitClear(LANDS_END_CLOUD_STAR_PIECE, ["lands_end_hint_text"], identifier="EVENT_947_jmp_if_bit_clear_33"),
	JmpIfBitClear(BELOME_TEMPLE_OPEN, ["EVENT_947_jmp_if_bit_clear_36"]),
	JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["belome_temple_hint_text"]),
	JmpIfBitClear(MAP_MONSTRO_TOWN, ["EVENT_947_jmp_if_bit_clear_47"], identifier="EVENT_947_jmp_if_bit_clear_36"),
	JmpIfBitClear(DOJO_BOSS_1_DEFEATED, ["monstro_town_hint_text"]),
	JmpIfBitClear(DOJO_BOSS_2_DEFEATED, ["monstro_town_hint_text"]),
	JmpIfBitClear(DOJO_BOSS_3_DEFEATED, ["monstro_town_hint_text"]),
	JmpIfBitClear(DOJO_BOSS_4_DEFEATED, ["monstro_town_hint_text"]),
	JmpIfBitSet(WIN_CONDITION_MONSTRO_DOOR, ["EVENT_947_jmp_if_bit_clear_47"]),
	JmpIfBitSet(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_947_jmp_if_bit_clear_47"]),
	JmpIfObjectNotInSpecificLevel(NPC_2, R324_MONSTRO_TOWN_OUTSIDE, ["monstro_town_hint_text"]),
	StoreItemAmountTo7000(ShinyStoneItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["monstro_town_hint_text"]),
	RunEventAsSubroutine(E0986_FROGFUCIUS_HINT_OPTIONAL_6),
	JmpIfBitClear(BEAN_VALLEY_BOSS_DEFEATED, ["bean_valley_hint_text"], identifier="EVENT_947_jmp_if_bit_clear_47"),
	RunEventAsSubroutine(E0987_FROGFUCIUS_HINT_OPTIONAL_7),
	JmpIfObjectInSpecificLevel(NPC_1, R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT, ["nimbus_castle_hint_text"]),
	JmpIfBitClear(STATUE_KEEPER_STAR_PIECE, ["nimbus_land_hint_text"]),
	StoreItemAmountTo7000(CastleKey1Item),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["nimbus_castle_hint_text"]),
	JmpIfObjectInSpecificLevel(NPC_10, R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, ["EVENT_947_jmp_if_bit_clear_59"]),
	JmpIfBitClear(NIMBUS_MID_BOSS_COMPLETED, ["nimbus_castle_hint_text"]),
	StoreItemAmountTo7000(CastleKey2Item),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["nimbus_castle_hint_text"]),
	JmpIfObjectInSpecificLevel(NPC_6, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["EVENT_947_jmp_if_bit_clear_59"]),
	JmpIfBitClear(NIMBUS_LAND_LIBERATED, ["nimbus_castle_hint_text"]),
	JmpIfBitClear(MAP_BARREL_VOLCANO, ["EVENT_947_jmp_if_bit_clear_61"], identifier="EVENT_947_jmp_if_bit_clear_59"),
	JmpIfBitClear(VOLCANO_LIBERATED, ["barrel_volcano_hint_text"]),
	JmpIfBitClear(MAP_VISTA_HILL, ["EVENT_947_run_event_as_subroutine_66"], identifier="EVENT_947_jmp_if_bit_clear_61"),
	JmpIfBitClear(BATTLE_DOOR_BOSS_BIT, ["keep_obstacle_hint_text"]),
	JmpIfBitClear(KEEP_BOSS_3_DEFEATED, ["bowsers_keep_hint_text"]),
	JmpIfBitClear(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE, ["EVENT_947_run_event_as_subroutine_66"]),
	JmpIfBitClear(INNER_FACTORY_ROOM_4_COMPLETED, ["factory_hint_text"]),
	RunEventAsSubroutine(E0984_FROGFUCIUS_HINT_OPTIONAL_4, identifier="EVENT_947_run_event_as_subroutine_66"),
	JmpIfObjectNotInSpecificLevel(NPC_1, R189_MARIOS_PIPEHOUSE, ["EVENT_947_jmp_if_bit_clear_69"]),
	JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_947_jmp_if_bit_clear_74"], identifier="EVENT_947_jmp_if_bit_clear_69"),
	StoreItemAmountTo7000(RareFrogCoinItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_947_jmp_73"]),
	Jmp(["EVENT_947_jmp_if_bit_clear_74"]),
	Jmp(["mushroom_kingdom_hint_text"], identifier="EVENT_947_jmp_73"),
	JmpIfBitClear(LANDS_END_GROTTO_BARREL_FLIPPED, ["lands_end_grotto_hint_text"], identifier="EVENT_947_jmp_if_bit_clear_74"),
	JmpIfBitClear(SEWERS_FLIPPED_CHEST_OPENED, ["kero_sewers_hint_text"]),
	JmpIfBitClear(MELODY_BAY_ITEM_1_GRANTED, ["tadpole_pond_hint_text"]),
	JmpIfBitClear(MINECART_CLEARED, ["EVENT_947_jmp_if_object_in_level_81"]),
	JmpIfBitClear(MELODY_BAY_ITEM_2_GRANTED, ["tadpole_pond_hint_text"]),
	JmpIfBitClear(MELODY_BAY_SONG_3_UNLOCKED, ["EVENT_947_jmp_if_object_in_level_81"]),
	JmpIfBitClear(MELODY_BAY_ITEM_3_GRANTED, ["tadpole_pond_hint_text"]),
	JmpIfObjectInSpecificLevel(NPC_13, R084_ROSE_TOWN_OUTSIDE, ["rose_town_hint_text"], identifier="EVENT_947_jmp_if_object_in_level_81"),
	JmpIfBitSet(PIPE_VAULT_GATED, ["EVENT_947_run_event_as_subroutine_84"]),
	JmpIfObjectInSpecificLevel(NPC_16, R034_YOSTER_ISLE, ["yoster_isle_hint_text"]),
	RunEventAsSubroutine(E0990_FROGFUCIUS_HINT_OPTIONAL_10, identifier="EVENT_947_run_event_as_subroutine_84"),
	JmpIfBitClear(TOWER_BOSS_2_DEFEATED, ["EVENT_947_jmp_if_bit_clear_88"]),
	JmpIfBitSet(KNIFE_GUY_PRIZE_GRANTED, ["EVENT_947_jmp_if_bit_clear_88"]),
	Jmp(["booster_tower_hint_text"]),
	JmpIfBitClear(TOWER_OPENED, ["EVENT_947_jmp_if_bit_set_92"], identifier="EVENT_947_jmp_if_bit_clear_88"),
	JmpIfObjectInSpecificLevel(NPC_16, R034_YOSTER_ISLE, ["booster_tower_hint_text"]),
	JmpIfBitSet(PORTRAIT_GAME_COMPLETED, ["EVENT_947_jmp_if_bit_clear_93"]),
	Jmp(["booster_tower_hint_text"]),
	JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["booster_tower_hint_text"], identifier="EVENT_947_jmp_if_bit_set_92"),
	JmpIfBitClear(MAP_MONSTRO_TOWN, ["EVENT_947_jmp_if_object_in_level_96"], identifier="EVENT_947_jmp_if_bit_clear_93"),
	JmpIfObjectInSpecificLevel(NPC_0, R324_MONSTRO_TOWN_OUTSIDE, ["monstro_town_hint_text"]),
	JmpIfBitClear(INVISIBLE_ITEMS_SUMMONED, ["monstro_town_hint_text"]),
	JmpIfObjectInSpecificLevel(NPC_3, R254_BEAN_VALLEY_SMILAX_AREA, ["bean_valley_hint_text"], identifier="EVENT_947_jmp_if_object_in_level_96"),
	JmpIfBitClear(RED_CELLAR_GUARD_ITEM_GRANTED, ["nimbus_castle_hint_text"]),
	StoreItemAmountTo7000(CastleKey1Item, identifier="EVENT_947_store_item_amount_7000_98"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["nimbus_castle_hint_text"]),
	JmpIfObjectInSpecificLevel(NPC_10, R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, ["postgame_progress_checker_2"]),
	JmpIfBitClear(NIMBUS_MID_BOSS_COMPLETED, ["nimbus_castle_hint_text"]),
	StoreItemAmountTo7000(CastleKey2Item),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["nimbus_castle_hint_text"]),
	JmpIfObjectInSpecificLevel(NPC_6, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["postgame_progress_checker_2"]),
	JmpIfBitClear(NIMBUS_LAND_LIBERATED, ["nimbus_castle_hint_text"]),
	JmpIfObjectInSpecificLevel(NPC_9, R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, ["nimbus_land_hint_text"]),
    JmpIfObjectInSpecificLevel(NPC_3, R189_MARIOS_PIPEHOUSE, ["EVENT_947_jmp_if_bit_clear_911"], identifier="postgame_progress_checker_2"),
    JmpIfBitClear(VOUCHER_CHECK_DONE, ["marios_pad_hint_text"]),
    StoreItemAmountTo7000(StayVoucherItem),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["marrymore_hint_text"]),
    JmpIfBitClear(STAY_VOUCHER_USED, ["EVENT_947_jmp_if_bit_clear_911"]),
	JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["hint_tower_postgame"]),
    JmpIfBitClear(MINES_POSTGAME_COMPLETED, ["mines_hint_text"]),
    JmpIfBitClear(TOWER_BOSS_1_STAR_PIECE, ["hint_temple_postgame"], identifier="hint_tower_postgame"),
    JmpIfBitClear(POSTGAME_TOWER_COMPLETED, ["booster_tower_hint_text"]),
	JmpIfObjectInSpecificLevel(NPC_4, R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM, ["hint_dojo_postgame"], identifier="hint_temple_postgame"),
    JmpIfBitClear(TEMPLE_POSTGAME_BOSS_DEFEATED, ["belome_temple_hint_text"]),
    JmpIfBitClear(DOJO_BOSS_4_DEFEATED, ["hint_culex_postgame"], identifier="hint_dojo_postgame"),
    JmpIfBitClear(DOJO_POSTGAME_COMPLETED, ["monstro_town_hint_text"]),
    JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["hint_chapel_postgame"], identifier="hint_culex_postgame"),
    StoreItemAmountTo7000(ExtraShinyStoneItem),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["hint_chapel_postgame"]),
    JmpIfBitClear(CULEX_POSTGAME_COMPLETED, ["monstro_town_hint_text"]),
    JmpIfBitClear(MARRYMORE_LIBERATED, ["hint_ship_postgame"], identifier="hint_chapel_postgame"),
    JmpIfBitClear(POSTGAME_CHAPEL_COMPLETE, ["marrymore_hint_text"]),
    JmpIfBitClear(SHIP_LIBERATED, ["EVENT_947_jmp_if_bit_clear_911"], identifier="hint_ship_postgame"),
    JmpIfBitClear(POSTGAME_SHIP_COMPLETED, ["sunken_ship_hint_text"]),
    JmpIfBitClear(MAP_MONSTRO_TOWN, ["EVENT_947_jmp_to_event_107"], identifier="EVENT_947_jmp_if_bit_clear_911"),
	JmpIfBitClear(INVISIBLE_FLAG_1_FOUND, ["invisible_item_hint_text"]),
    JmpIfBitClear(INVISIBLE_FLAG_2_FOUND, ["invisible_item_hint_text"]),
    JmpIfBitClear(INVISIBLE_FLAG_3_FOUND, ["invisible_item_hint_text"]),
	JmpToEvent(E0948_FROGFUCIUS_HINT_EXPANSION, identifier="EVENT_947_jmp_to_event_107")
])
