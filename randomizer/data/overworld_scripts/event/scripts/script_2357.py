# E2357_EMPTY

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
	EnableControls([]),
	ApplyTileModToLevel(use_alternate=True, room_id=R248_GAME_INTRO_MUSHROOM_WAY_AREA_01, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R248_GAME_INTRO_MUSHROOM_WAY_AREA_01, mod_id=1),
	Pause(1),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=12, y=28)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=16, y=44, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	SetSyncActionScript(MARIO, A0838_EMPTY),
	Pause(3),
	FadeInFromBlack(sync=False),
	Pause(1, identifier="EVENT_2357_pause_9"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2357_set_action_script_12"]),
	Jmp(["EVENT_2357_pause_9"]),
	SetSyncActionScript(NPC_7, A0839_EMPTY, identifier="EVENT_2357_set_action_script_12"),
	Pause(16),
	SetSyncActionScript(NPC_5, A0832_EMPTY),
	Pause(96),
	SetSyncActionScript(NPC_7, A0839_EMPTY),
	Pause(16),
	SetSyncActionScript(NPC_6, A0832_EMPTY),
	Pause(1, identifier="EVENT_2357_pause_19"),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_2357_remove_from_current_level_22"]),
	Jmp(["EVENT_2357_pause_19"]),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_2357_remove_from_current_level_22"),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	CircleMaskShrinkToObject(target=MARIO, width=24, speed=5, static=False),
	Pause(80),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	DisplayIntroTitleText(text=SUPER_MARIO, y=17),
	Pause(150),
	FadeOutToBlack(sync=False, duration=30),
	JmpToEvent(E0129_EMPTY),
	Return()
])
