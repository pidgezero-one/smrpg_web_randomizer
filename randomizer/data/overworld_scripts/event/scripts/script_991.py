# E0991_FROGFUCIUS_HINT_DIALOGUES
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
	RunDialog(dialog_id=DI2731_FROGFUCIUS_MARIOS_PAD_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="marios_pad_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2732_FROGFUCIUS_BANDITS_WAY_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="bandits_way_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2733_FROGFUCIUS_MUSHROOM_KINGDOM_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="mushroom_kingdom_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2734_FROGFUCIUS_LANDS_END_GROTTO_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="lands_end_grotto_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2735_FROGFUCIUS_MELODY_BAY_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="tadpole_pond_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2736_FROGFUCIUS_ROSE_TOWN_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="rose_town_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2737_FROGFUCIUS_YOSTER_ISLE_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="yoster_isle_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2738_FROGFUCIUS_MOLEVILLE_TOWN_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="moleville_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2739_FROGFUCIUS_MINE_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="mines_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2740_FROGFUCIUS_TOWER_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="booster_tower_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2741_FROGFUCIUS_SEASIDE_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="seaside_town_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2742_FROGFUCIUS_MONSTRO_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="monstro_town_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2743_FROGFUCIUS_BEAN_VALLEY_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="bean_valley_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2744_FROGFUCIUS_NIMBUS_TOWN_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="nimbus_land_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2745_FROGFUCIUS_NIMBUS_CASTLE_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="nimbus_castle_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2746_FROGFUCIUS_MUSHROOM_WAY_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="mushroom_way_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2747_FROGFUCIUS_SHIP_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="sunken_ship_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2748_FROGFUCIUS_SEWER_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="kero_sewers_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2749_FROGFUCIUS_FOREST_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="forest_maze_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2750_FROGFUCIUS_MARRYMORE_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="marrymore_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2751_FROGFUCIUS_LANDS_END_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="lands_end_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2752_FROGFUCIUS_TEMPLE_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="belome_temple_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2753_FROGFUCIUS_BOOSTER_HILL_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="booster_hill_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2754_FROGFUCIUS_VOLCANO_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="barrel_volcano_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2755_FROGFUCIUS_BOWSERS_KEEP_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="bowsers_keep_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2756_FROGFUCIUS_FACTORY_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="factory_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2757_FROGFUCIUS_CASINO_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="casino_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2760_FROGFUCIUS_MIDAS_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="midas_river_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2761_FROGFUCIUS_ROSE_WAY_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="rose_way_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2762_FROGFUCIUS_PIPE_VAULT_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="pipe_vault_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2763_FROGFUCIUS_BOOSTER_PASS_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="booster_pass_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2764_FROGFUCIUS_STAR_HILL_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="star_hill_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2765_FROGFUCIUS_MARRYMORE_HOTEL_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="marrymore_hotel_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2766_FROGFUCIUS_FROG_DISCIPLE_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="frog_disciple_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2767_FROGFUCIUS_SEA_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="sea_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2768_FROGFUCIUS_BEANSTALK_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="beanstalk_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2769_FROGFUCIUS_SUPER_JUMP_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="super_jump_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI2770_FROGFUCIUS_KEEP_OBSTACLE_PRIZE_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="keep_obstacle_hint_text"),
	ReturnAll(),
	RunDialog(dialog_id=DI0023_INVISIBLE_ITEM_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="invisible_item_hint_text"),
	ReturnAll(),
])
