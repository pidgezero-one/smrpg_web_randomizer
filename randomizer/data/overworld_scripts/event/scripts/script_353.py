# E0353_BOSS_BATTLE

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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 28, ["EVENT_353_start_battle_41"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 103, ["EVENT_353_start_battle_43"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 154, ["EVENT_353_start_battle_45"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 177, ["EVENT_353_start_battle_47"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 192, ["EVENT_353_start_battle_49"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 258, ["EVENT_353_start_battle_51"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 205, ["EVENT_353_start_battle_53"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 206, ["EVENT_353_start_battle_55"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 223, ["EVENT_353_start_battle_57"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 232, ["EVENT_353_start_battle_59"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 254, ["EVENT_353_start_battle_61"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 255, ["EVENT_353_start_battle_63"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 266, ["EVENT_353_start_battle_65"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 268, ["EVENT_353_start_battle_67"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 271, ["EVENT_353_start_battle_69"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 302, ["EVENT_353_start_battle_71"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 315, ["EVENT_353_start_battle_73"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 326, ["EVENT_353_start_battle_75"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 351, ["EVENT_353_start_battle_77"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 352, ["EVENT_353_start_battle_79"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 393, ["EVENT_353_start_battle_81"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 409, ["EVENT_353_start_battle_83"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 430, ["EVENT_353_start_battle_85"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 461, ["EVENT_353_start_battle_87"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 469, ["EVENT_353_start_battle_89"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 470, ["EVENT_353_start_battle_91"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 471, ["EVENT_353_start_battle_93"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 472, ["EVENT_353_start_battle_95"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 496, ["EVENT_353_start_battle_97"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 512, ["EVENT_353_set_var_to_const_99"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 513, ["EVENT_353_set_var_to_const_102"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 514, ["EVENT_353_set_var_to_const_105"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 515, ["EVENT_353_start_battle_108"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 516, ["EVENT_353_start_battle_110"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 517, ["EVENT_353_start_battle_112"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 518, ["EVENT_353_start_battle_114"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 519, ["EVENT_353_set_var_to_const_116"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 520, ["EVENT_353_start_battle_119"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 521, ["EVENT_353_start_battle_121"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 522, ["EVENT_353_start_battle_123"]),
	Return(),
	StartBattleAtBattlefield(PACK166_JOHNNY_FIGHT_STATIC, BF04_SUNKEN_SHIP, identifier="EVENT_353_start_battle_41"),
	Return(),
	StartBattleAtBattlefield(PACK184_CLOAKER_DOMINO_FIGHT_STATIC, BF40_SMITHY_FACTORY_DOMINO_CLOAKERS_PAD, identifier="EVENT_353_start_battle_43"),
	Return(),
	StartBattleAtBattlefield(PACK176_BUNDT_FIGHT_STATIC, BF35_MARRYMORE_CHAPEL_SANCTUARY, identifier="EVENT_353_start_battle_45"),
	Return(),
	StartBattleAtBattlefield(PACK167_CALAMARI_FIGHT_STATIC, BF03_SUNKEN_SHIP_KING_CALAMARIS_CELLAR, identifier="EVENT_353_start_battle_47"),
	Return(),
	StartBattleAtBattlefield(PACK161_BOOSTER_FIGHT_STATIC, BF12_BOOSTER_TOWER, identifier="EVENT_353_start_battle_49"),
	Return(),
	StartBattleAtBattlefield(PACK177_KGGG_FIGHT_STATIC, BF17_BOOSTER_TOWER_BALCONY, identifier="EVENT_353_start_battle_51"),
	Return(),
	StartBattleAtBattlefield(PACK183_HAMMERBRO_FIGHT_STATIC, BF09_GRASSLANDS, identifier="EVENT_353_start_battle_53"),
	Return(),
	StartBattleAtBattlefield(PACK163_CROCO1_FIGHT_STATIC, BF09_GRASSLANDS, identifier="EVENT_353_start_battle_55"),
	Return(),
	StartBattleAtBattlefield(PACK174_COUNTDOWN_FIGHT_STATIC, BF18_SMITHY_FACTORY_COUNT_DOWNS_PAD, identifier="EVENT_353_start_battle_57"),
	Return(),
	StartBattleAtBattlefield(PACK181_BOWYER_FIGHT_STATIC, BF01_FOREST_MAZE_BOWYERS_PAD, identifier="EVENT_353_start_battle_59"),
	Return(),
	StartBattleAtBattlefield(PACK173_MEGASMILAX_FIGHT_STATIC, BF41_BEAN_VALLEY_GRASSLANDS, identifier="EVENT_353_start_battle_61"),
	Return(),
	StartBattleAtBattlefield(PACK189_JAGGER_FIGHT_STATIC, BF46_JINXS_DOJO, identifier="EVENT_353_start_battle_63"),
	Return(),
	StartBattleAtBattlefield(PACK209_MAGIKOOPA_BOSS_STATIC, BF07_BOWSERS_KEEP, identifier="EVENT_353_start_battle_65"),
	Return(),
	StartBattleAtBattlefield(PACK169_BELOME2_FIGHT_STATIC, BF42_BELOME_TEMPLE, identifier="EVENT_353_start_battle_67"),
	Return(),
	StartBattleAtBattlefield(PACK140_PUNCHINELLO_STATIC, BF05_MOLEVILLE_MINES, identifier="EVENT_353_start_battle_69"),
	Return(),
	StartBattleAtBattlefield(PACK168_BELOME1_FIGHT_STATIC, BF21_KERO_SEWERS, identifier="EVENT_353_start_battle_71"),
	Return(),
	StartBattleAtBattlefield(PACK180_YARIDOVICH_FIGHT_STATIC, BF37_SEASIDE_TOWN_BEACH, identifier="EVENT_353_start_battle_73"),
	Return(),
	StartBattleAtBattlefield(PACK179_MACK_FIGHT_STATIC, BF15_MUSHROOM_KINGDOM_CASTLE, identifier="EVENT_353_start_battle_75"),
	Return(),
	StartBattleAtBattlefield(PACK216_CULEX_BOSS_STATIC, BF47_CULEX, identifier="EVENT_353_start_battle_77"),
	Return(),
	StartBattleAtBattlefield(PACK172_CZAR_FIGHT_STATIC, BF08_BARREL_VOLCANO_CZAR_DRAGONS_PAD, identifier="EVENT_353_start_battle_79"),
	Return(),
	StartBattleAtBattlefield(PACK182_AXEM_FIGHT_STATIC, BF39_BLADE_AXEM_RANGERS, identifier="EVENT_353_start_battle_81"),
	Return(),
	StartBattleAtBattlefield(PACK175_BIRDETTA_FIGHT_STATIC, BF23_NIMBUS_CASTLE_BIRDOS_ROOM, identifier="EVENT_353_start_battle_83"),
	Return(),
	StartBattleAtBattlefield(PACK171_VALENTINA_FIGHT_STATIC, BF24_NIMBUS_LAND, identifier="EVENT_353_start_battle_85"),
	Return(),
	StartBattleAtBattlefield(PACK235_CHESTER_DUPE, BF07_BOWSERS_KEEP, identifier="EVENT_353_start_battle_87"),
	Return(),
	StartBattleAtBattlefield(PACK146_CLERK_STATIC, BF48_FACTORY_GROUNDS, identifier="EVENT_353_start_battle_89"),
	Return(),
	StartBattleAtBattlefield(PACK149_GUNYOLK_STATIC, BF48_FACTORY_GROUNDS, identifier="EVENT_353_start_battle_91"),
	Return(),
	StartBattleAtBattlefield(PACK147_MANAGER_STATIC, BF48_FACTORY_GROUNDS, identifier="EVENT_353_start_battle_93"),
	Return(),
	StartBattleAtBattlefield(PACK148_DIRECTOR_STATIC, BF48_FACTORY_GROUNDS, identifier="EVENT_353_start_battle_95"),
	Return(),
	StartBattleAtBattlefield(PACK185_SMITHY1_FIGHT_STATIC, BF44_FACTORY_GROUNDS_SMITHYS_PAD, identifier="EVENT_353_start_battle_97"),
	Return(),
	SetVarToConst(BATTLE_PACK_ID, 156, identifier="EVENT_353_set_var_to_const_99"),
	StartBattleWithPackAt700E(),
	Return(),
	SetVarToConst(BATTLE_PACK_ID, 157, identifier="EVENT_353_set_var_to_const_102"),
	StartBattleWithPackAt700E(),
	Return(),
	SetVarToConst(BATTLE_PACK_ID, 158, identifier="EVENT_353_set_var_to_const_105"),
	StartBattleWithPackAt700E(),
	Return(),
	StartBattleAtBattlefield(PACK178_JINX1_FIGHT_STATIC, BF46_JINXS_DOJO, identifier="EVENT_353_start_battle_108"),
	Return(),
	StartBattleAtBattlefield(PACK187_JINX2_FIGHT_STATIC, BF46_JINXS_DOJO, identifier="EVENT_353_start_battle_110"),
	Return(),
	StartBattleAtBattlefield(PACK188_JINX3_FIGHT_STATIC, BF46_JINXS_DOJO, identifier="EVENT_353_start_battle_112"),
	Return(),
	StartBattleAtBattlefield(PACK164_CROCO2_FIGHT_STATIC, BF05_MOLEVILLE_MINES, identifier="EVENT_353_start_battle_114"),
	Return(),
	SetVarToConst(BATTLE_PACK_ID, 207, identifier="EVENT_353_set_var_to_const_116"),
	StartBattleWithPackAt700E(),
	Return(),
	StartBattleAtBattlefield(PACK208_DODO_BOSS_STATIC, BF22_NIMBUS_CASTLE, identifier="EVENT_353_start_battle_119"),
	Return(),
	StartBattleAtBattlefield(PACK210_BOOMER_BOSS_STATIC, BF29_BOWSERS_KEEP_CHANDELIERS, identifier="EVENT_353_start_battle_121"),
	Return(),
	StartBattleAtBattlefield(PACK186_EXOR_FIGHT_STATIC, BF16_BOWSERS_KEEP_TURRET_EXOR, identifier="EVENT_353_start_battle_123"),
	Return()
])
