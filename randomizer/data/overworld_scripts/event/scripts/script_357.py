# E0357_EXP_STAR_MUSIC_EXPERIMENT
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
from ....spells.spells import *
from ....variables.event_palette_names import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R224_FOREST_MAZE_AREA_01, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R226_FOREST_MAZE_AREA_02, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R228_FOREST_MAZE_AREA_04, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R229_FOREST_MAZE_AREA_06, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R231_FOREST_MAZE_SECRET_ENTRANCE, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R233_FOREST_MAZE_AREA_03_UNDERGROUND, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R234_FOREST_MAZE_SECRET, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R235_FOREST_MAZE_AREA_08_UNDERGROUND, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R256_FOREST_MAZE_SMALL_AREA_WTREE_TRUNK_UNUSED, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R040_BOOSTER_TOWER_8F_CHOMP_STAIRWAY, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R042_BOOSTER_TOWER_3F_AREA_02_NES_MARIO_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R004_POSTGAME_TOWER, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R201_BOOSTER_TOWER_6F_AREA_01_SMALL_ROOM_WSAVE_POINT, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R259_BOOSTER_TOWER_3F_AREA_01_GREEN_SWITCH_FOR_BP_SECRET, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R026_SUNKEN_SHIP_POSTKC_AREA_12_UNDERWATER_ROOM_WSTAIRWELL_AND_ZEOSTARS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R003_POSTGAME_SHIP, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R160_SUNKEN_SHIP_AREA_01, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R161_SUNKEN_SHIP_AREA_03_GREAPERS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R162_SUNKEN_SHIP_AREA_04_GREAPERS_DRY_BONES, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R163_SUNKEN_SHIP_PUZZLE_ROOM_2, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R164_SUNKEN_SHIP_AREA_02_FROM_ENTRANCE_WSAVE_POINT, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R166_SUNKEN_SHIP_PUZZLE_ROOM_1, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R168_SUNKEN_SHIP_PUZZLE_ROOM_3, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R170_SUNKEN_SHIP_AREA_14_DUMMY, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R171_SUNKEN_SHIP_PUZZLE_ROOM_4, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R172_SUNKEN_SHIP_PUZZLE_ROOM_5, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R176_SUNKEN_SHIP_AREA_08_WSAVE_POINT_AND_GREEN_SWITCH_FOR_BARREL, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R178_SUNKEN_SHIP_POSTKC_AREA_04_LONG_STAIRWELL_WRUNNING_ALLEY_RATS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R180_SUNKEN_SHIP_POSTKC_AREA_02_SMALL_2LEVEL_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R182_SUNKEN_SHIP_POSTKC_AREA_07_THREE_DRY_BONES, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R183_SUNKEN_SHIP_POSTKC_AREA_08_SECRET_ROOM_WITH_FROG_COIN, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R186_SUNKEN_SHIP_POSTKC_AREA_18_WARP_ROOM_FROM_JOHNNYS_ROOM, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS, ["EVENT_357_play_music_current_volume_72"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R188_SUNKEN_SHIP_POSTKC_AREA_11_WATER_ROOM_WITH_WHIRLPOOL, ["EVENT_357_play_music_current_volume_72"]),
    
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R123_PIPE_VAULT_AREA_01, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R124_PIPE_VAULT_AREA_03_LINE_OF_PIPES, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R126_PIPE_VAULT_AREA_06_LINE_OF_RED_PIPES, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R127_PIPE_VAULT_AREA_02, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R129_PIPE_VAULT_AREA_05, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R143_PIPE_VAULT_GOOMBATHUMPING_ROOM, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R146_PIPE_VAULT_AREA_02_DUMMY, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R245_GAME_INTRO_PIPE_VAULT_AREA_02_WTHWOMP, ["EVENT_357_play_music_current_volume_72"]),
    
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R107_NIMBUS_CASTLE_AREA_09_STATUE_ROOM_AFTER_VALENTINA, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R412_NIMBUS_CASTLE_AREA_11_LONG_HALLWAY_DOOR_TO_KINGS_CELLAR, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R497_NIMBUS_CASTLE_AREA_06_DUMMY, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R498_NIMBUS_CASTLE_AREA_10_DUMMY, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R500_NIMBUS_CASTLE_AREA_04_DUMMY, ["EVENT_357_play_music_current_volume_72"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA, ["EVENT_357_play_music_current_volume_72"]),
    

    PlaySound(sound=SO014_FLOWER, channel=6),
	StopMusicFDA0(),
	PlayMusicAtCurrentVolume(M0008_INVINCIBLESTAR),
	Return(),
    StopMusic(identifier="EVENT_357_play_music_current_volume_72"),
    PlaySound(sound=SO014_FLOWER, channel=6),
    Pause(16),
	PlayMusicAtCurrentVolume(M0008_INVINCIBLESTAR),
	Return()
])
