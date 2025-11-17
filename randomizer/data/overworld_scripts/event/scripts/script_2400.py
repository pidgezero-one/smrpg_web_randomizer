# E2400_EMPTY

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
	UnfreezeAllNPCs(),
	ClearBit(DIRECTIONAL_7045_0),
	ClearBit(DIRECTIONAL_7045_1),
	ClearBit(DIRECTIONAL_7045_2),
	ActionQueueAsync(target=MARIO, subscript=[
		A_OverwriteSolidity(),
		A_VisibilityOff(),
		A_TransferToXYZF(x=14, y=26, z=0, direction=EAST)
	]),
	SetSyncActionScript(NPC_0, A0455_EMPTY),
	Pause(32),
	Pause(1, identifier="EVENT_2400_pause_7"),
	Set7000ToTappedButton(),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_2400_pause_7"]),
	PauseActionScript(NPC_0),
	JmpIfBitSet(DIRECTIONAL_7045_1, ["EVENT_2400_action_queue_15"]),
	JmpIfBitSet(DIRECTIONAL_7045_2, ["EVENT_2400_action_queue_18"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth(),
		A_VisibilityOn(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\x80\x00\x80\x00')),
		A_UnknownCommand(bytearray(b'%\x00\n\xd0\xff')),
		A_Pause(104),
		A_BPL262728()
	]),
	Jmp(["EVENT_2400_set_action_script_19"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\x00\xff\x80\x00')),
		A_UnknownCommand(bytearray(b'%\x00\t\xd0\xff')),
		A_Pause(104),
		A_BPL262728()
	], identifier="EVENT_2400_action_queue_15"),
	SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
	Jmp(["EVENT_2400_set_action_script_19"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_VisibilityOn(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\x00\x01\x80\xff')),
		A_UnknownCommand(bytearray(b'%\x00\t\xd0\xff')),
		A_Pause(104),
		A_BPL262728()
	], identifier="EVENT_2400_action_queue_18"),
	SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY, identifier="EVENT_2400_set_action_script_19"),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetSyncActionScript(NPC_0, A0454_EMPTY),
	Return()
])
