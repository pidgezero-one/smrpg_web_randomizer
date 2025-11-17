# E2661_EMPTY

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
	JmpIfBitSet(DIRECTIONAL_7046_2, ["EVENT_2661_ret_13"]),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	SetSyncActionScript(NPC_4, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
	SummonObjectToSpecificLevel(NPC_4, R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS),
	RemoveObjectFromSpecificLevel(NPC_7, R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS),
	SetBit(DIRECTIONAL_7046_2),
	Inc(HIDDEN_CHEST_COUNTER),
	RunDialog(dialog_id=DI3321_YOU_MISSED, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	SetSyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=1, sprite_offset=3, is_sequence=True, looping=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4)
	]),
	Pause(40),
	SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(identifier="EVENT_2661_ret_13")
])
