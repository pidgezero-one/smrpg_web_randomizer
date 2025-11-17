# E1803_EMPTY

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
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_PlaySound(sound=SO085_FLOWER, channel=4),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(30),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True)
	]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 33, ["EVENT_1803_set_var_to_const_6"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 34, ["EVENT_1803_set_var_to_const_8"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 35, ["EVENT_1803_set_var_to_const_10"]),
	Return(),
	SetVarToConst(ITEM_ID, MaxMushroomItem, identifier="EVENT_1803_set_var_to_const_6"),
	Jmp(["EVENT_1803_run_dialog_11"]),
	SetVarToConst(ITEM_ID, RoyalSyrupItem, identifier="EVENT_1803_set_var_to_const_8"),
	Jmp(["EVENT_1803_run_dialog_11"]),
	SetVarToConst(ITEM_ID, FireBombItem, identifier="EVENT_1803_set_var_to_const_10"),
	RunDialog(dialog_id=DI1177_FOUND_A_70A7_AUTO_TERMINATE, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, bit_6=True, identifier="EVENT_1803_run_dialog_11"),
	Pause(60),
	AddToInventory(ITEM_ID),
	Return()
])
