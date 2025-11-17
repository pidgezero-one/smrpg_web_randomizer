# E2670_TOWER_KNIFE_GUY_CONSOLATION_PRIZE

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
	SetVarToRandom(PRIMARY_TEMP_7000, 21),
	CompareVarToConst(PRIMARY_TEMP_7000, 3),
	JmpIfComparisonResultIsLesser(["EVENT_2670_jmp_if_bit_set_31"]),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_2670_set_var_to_const_7"]),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_2670_set_var_to_const_9"]),
	SetVarToConst(ITEM_ID, WiltShroomItem),
	Jmp(["EVENT_2670_play_sound_11"]),
	SetVarToConst(ITEM_ID, RottenMushItem, identifier="EVENT_2670_set_var_to_const_7"),
	Jmp(["EVENT_2670_play_sound_11"]),
	SetVarToConst(ITEM_ID, MoldyMushItem, identifier="EVENT_2670_set_var_to_const_9"),
	Jmp(["EVENT_2670_play_sound_11"]),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6, identifier="EVENT_2670_play_sound_11"),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_2670_put_inventory_17"]),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_2670_put_inventory_19"]),
	AddToInventory(WiltShroomItem),
	Return(),
	AddToInventory(RottenMushItem, identifier="EVENT_2670_put_inventory_17"),
	Return(),
	AddToInventory(MoldyMushItem, identifier="EVENT_2670_put_inventory_19"),
	Return(),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6, identifier="EVENT_2670_play_sound_21"),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_2670_put_inventory_27"]),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_2670_put_inventory_29"]),
	AddToInventory(MushroomItem),
	Return(),
	AddToInventory(MidMushroomItem, identifier="EVENT_2670_put_inventory_27"),
	Return(),
	AddToInventory(MaxMushroomItem, identifier="EVENT_2670_put_inventory_29"),
	Return(),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_2670_set_var_to_const_35"], identifier="EVENT_2670_jmp_if_bit_set_31"),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_2670_set_var_to_const_37"]),
	SetVarToConst(ITEM_ID, MushroomItem),
	Jmp(["EVENT_2670_play_sound_21"]),
	SetVarToConst(ITEM_ID, MidMushroomItem, identifier="EVENT_2670_set_var_to_const_35"),
	Jmp(["EVENT_2670_play_sound_21"]),
	SetVarToConst(ITEM_ID, MaxMushroomItem, identifier="EVENT_2670_set_var_to_const_37"),
	Jmp(["EVENT_2670_play_sound_21"])
])
