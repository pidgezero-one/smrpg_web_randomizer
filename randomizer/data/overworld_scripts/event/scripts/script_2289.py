# E2289_EMPTY

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
	EnterArea(room_id=R247_GAME_INTRO_TADPOLE_POND_MARIO_SUMMONS_TADPOLES, face_direction=NORTHEAST, x=9, y=58, z=0),
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_BounceToXYWithHeight(x=11, y=34, height=0),
		A_WalkSouthwestSteps(1)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=12, y=51, z=0, direction=EAST)
	]),
	FadeInFromBlack(sync=False),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(35),
		A_SetPriority(3),
		A_JumpToHeight(height=108, silent=True),
		A_Pause(10),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=12, y=47),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=15, y=49),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=14, y=43),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftToXYCoords(x=17, y=45),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_ShiftToXYCoords(x=16, y=39),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ShiftToXYCoords(x=19, y=41),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ShiftToXYCoords(x=18, y=35),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ShiftToXYCoords(x=21, y=37),
		A_ReturnQueue()
	]),
	SetSyncActionScript(NPC_0, A0091_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_1, A0092_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_2, A0091_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_3, A0092_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_4, A0091_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_5, A0092_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_6, A0091_BRIDGE_TADPOLE),
	Pause(5),
	SetSyncActionScript(NPC_7, A0092_BRIDGE_TADPOLE),
	Pause(20),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_Pause(20),
		A_ShadowOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Pause(1),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(80),
		A_WalkNortheastSteps(2),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_Pause(1),
		A_FaceNortheast(),
		A_Pause(5),
		A_ShadowOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Pause(1),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(80),
		A_WalkNortheastSteps(2),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_Pause(1),
		A_FaceNortheast(),
		A_Pause(5),
		A_ShadowOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Pause(1),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(80),
		A_WalkNortheastSteps(2),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_Pause(1),
		A_FaceNortheast(),
		A_Pause(5),
		A_ShadowOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Pause(1),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(80),
		A_WalkNortheastSteps(2),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_Pause(1),
		A_FaceNortheast(),
		A_Pause(5)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShadowOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Pause(1),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(80),
		A_WalkNortheastSteps(2),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ShadowOn(),
		A_Pause(1),
		A_FaceNortheast(),
		A_Pause(1)
	]),
	FadeOutToBlack(sync=False, duration=30),
	JmpToEvent(E0134_EMPTY)
])
