# E0992_EMPTY

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
	EnterArea(room_id=R243_GAME_INTRO_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM, face_direction=NORTHEAST, x=13, y=35, z=0),
	FreezeCamera(),
	SetSyncActionScript(NPC_1, A0790_EMPTY),
	SetSyncActionScript(NPC_2, A0790_EMPTY),
	SetSyncActionScript(NPC_3, A0791_EMPTY),
	SetSyncActionScript(NPC_4, A0791_EMPTY),
	SetSyncActionScript(NPC_5, A0791_EMPTY),
	SetSyncActionScript(NPC_6, A0790_EMPTY),
	SetSyncActionScript(SCREEN_FOCUS, A0792_EMPTY),
	Pause(10),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkNortheastSteps(2),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(4),
		A_Pause(80),
		A_StartLoopNTimes(2),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(6),
		A_ResetProperties(),
		A_Pause(6),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestPixels(12),
		A_Pause(90),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(10),
		A_ResetProperties()
	]),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceSouthwest(),
		A_Pause(20),
		A_JumpToHeight(height=108, silent=True),
		A_Pause(1, identifier="EVENT_992_action_queue_14_SUBSCRIPT_pause_4"),
		A_JmpIfMarioInAir(["EVENT_992_action_queue_14_SUBSCRIPT_pause_4"]),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(6),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Pause(90),
	FadeOutToBlack(sync=True, duration=30),
	PauseScriptUntilEffectDone(),
	RememberLastObject(),
	JmpToEvent(E0130_EMPTY)
])
