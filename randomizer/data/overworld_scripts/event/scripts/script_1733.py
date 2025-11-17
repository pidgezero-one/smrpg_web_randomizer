# E1733_EMPTY

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
	SetVarToConst(TEMP_7030, 0, identifier="EVENT_1733_set_var_to_const_0"),
	EnableControls([]),
	SummonObjectToSpecificLevel(NPC_2, R148_GAME_INTRO_BANDITS_WAY_AREA_04),
	SummonObjectToSpecificLevel(NPC_3, R148_GAME_INTRO_BANDITS_WAY_AREA_04),
	SummonObjectToSpecificLevel(NPC_4, R148_GAME_INTRO_BANDITS_WAY_AREA_04),
	SummonObjectToSpecificLevel(NPC_5, R148_GAME_INTRO_BANDITS_WAY_AREA_04),
	EnableObjectTriggerInSpecificLevel(NPC_0, R148_GAME_INTRO_BANDITS_WAY_AREA_04),
	EnterArea(room_id=R148_GAME_INTRO_BANDITS_WAY_AREA_04, face_direction=EAST, x=7, y=24, z=4),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_JumpToHeight(height=0, silent=True)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOn(),
		A_WalkEastPixels(16)
	]),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkNortheastPixels(8),
		A_WalkEastPixels(2)
	]),
	MoveScriptToBackgroundThread2(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_FloatingOff(),
		A_WalkEastPixels(5),
		A_JumpToHeight(height=108, silent=True),
		A_WalkEastSteps(2)
	]),
	SetSyncActionScript(NPC_2, A0769_EMPTY),
	SetSyncActionScript(NPC_3, A0769_EMPTY),
	SetSyncActionScript(NPC_4, A0769_EMPTY),
	SetSyncActionScript(NPC_5, A0769_EMPTY),
	RunBackgroundEvent(event_id=E1734_EMPTY, return_on_level_exit=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkEastSteps(4),
		A_WalkNorthwestSteps(3),
		A_WalkSouthwestSteps(6),
		A_WalkNorthwestSteps(3),
		A_WalkNortheastSteps(3),
		A_WalkSoutheastSteps(6),
		A_WalkNortheastSteps(3)
	]),
	FadeOutToBlack(sync=True, duration=30),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkWestSteps(6)
	]),
	PauseScriptUntilEffectDone(),
	MoveScriptToMainThread(),
	ClearBit(TEMP_7076_0),
	MarioStopsGlowing(),
	JmpToEvent(E1728_EMPTY)
])
