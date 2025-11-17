# E0640_EMPTY

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
	ClearBit(TEMP_7043_3),
	Jmp(["EVENT_640_action_queue_6"]),
	JmpIfBitSet(SANCTUARY_LOCKED, ["EVENT_256_ret_0"]),
	SetBit(SANCTUARY_LOCKED),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkToXYCoords(x=20, y=17),
		A_FaceNorthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=20, y=17, z=0, direction=EAST),
		A_Pause(1),
		A_TransferXYZFPixels(x=252, y=2, z=0, direction=EAST),
		A_FixedFCoordOff(),
		A_WalkNorthwestPixels(6),
		A_VisibilityOn(),
		A_WalkNorthwestPixels(10),
		A_FaceSoutheast()
	], identifier="EVENT_640_action_queue_6"),
	Jmp(["EVENT_640_action_queue_14"]),
	Pause(10),
	RunDialog(dialog_id=DI2074_EMPTY, above_object=NPC_3, closable=False, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2075_EMPTY, above_object=NPC_3, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ResetProperties(),
		A_WalkToXYCoords(x=18, y=19),
		A_FaceNortheast()
	], identifier="EVENT_640_action_queue_14"),
	SetSyncActionScript(NPC_3, A0031_EMPTY),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceSouth()
	]),
	Return()
])
