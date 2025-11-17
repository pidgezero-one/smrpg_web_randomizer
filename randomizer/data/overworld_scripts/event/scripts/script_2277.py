# E2277_EMPTY

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
	FadeOutMusicToVolume(duration=0, volume=0),
	Pause(60),
	EnterArea(room_id=R015_VISTA_HILL, face_direction=NORTHWEST, x=4, y=16, z=0),
	FadeOutMusicToVolume(duration=0, volume=0),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_BounceToXYWithHeight(x=0, y=2, height=0)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=4, y=26, z=0, direction=EAST),
		A_WalkNortheastPixels(1),
		A_FaceNorthwest(),
		A_SequencePlaybackOff(),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkEastSteps(1)
	]),
	ActionQueueAsync(target=LAYER_2, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkWestSteps(1)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=4, y=26, z=0, direction=EAST),
		A_WalkNortheastPixels(12),
		A_WalkNorthwestPixels(8),
		A_FaceNorthwest(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=4, y=26, z=0, direction=EAST),
		A_WalkNortheastSteps(1),
		A_WalkNortheastPixels(8),
		A_WalkSoutheastPixels(12),
		A_FaceNortheast(),
		A_VisibilityOn(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=4, y=26, z=0, direction=EAST),
		A_WalkSoutheastPixels(4),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(8),
		A_WalkSoutheastPixels(16),
		A_FaceNorthwest(),
		A_VisibilityOn(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=4, y=26, z=0, direction=EAST),
		A_WalkSoutheastSteps(1),
		A_WalkSouthPixels(4),
		A_FaceNorthwest(),
		A_VisibilityOn(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=4, y=26, z=0, direction=EAST),
		A_WalkSoutheastSteps(1),
		A_WalkNortheastPixels(10),
		A_WalkSouthPixels(4),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=4, y=26, z=0, direction=EAST),
		A_WalkNortheastSteps(1),
		A_WalkNortheastPixels(8),
		A_WalkSoutheastSteps(3),
		A_WalkSouthwestPixels(8),
		A_WalkSouthPixels(8),
		A_FaceSouthwest(),
		A_SequenceLoopingOn(),
		A_VisibilityOn()
	]),
	FadeInFromBlack(sync=False, duration=60),
	PlayMusicAtDefaultVolume(M0066_BOWSER_SCASTLE_2NDTIME),
	Pause(90),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_JumpToHeight(128),
		A_Pause(30),
		A_SequenceLoopingOff()
	]),
	Pause(25),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SequenceLoopingOff(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(5),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SequenceLoopingOff(),
		A_Pause(5),
		A_FaceNortheast(),
		A_Pause(10),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(20),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_Pause(5),
		A_FaceNorthwest(),
		A_SequenceLoopingOff(),
		A_Pause(15),
		A_SequenceLoopingOn(),
		A_FaceSouthwest(),
		A_Pause(50),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	Pause(60),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=127, y=15, z=0, direction=EAST),
		A_WalkNorthPixels(11),
		A_WalkWestPixels(24),
		A_VisibilityOn(),
		A_SequenceLoopingOn(),
		A_UnknownCommand(bytearray(b' \x01')),
		A_EmbeddedAnimationRoutine(bytearray(b'&\x80\x01\xfe\xff\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x80')),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthSteps(3),
		A_WalkSouthPixels(1),
		A_UnknownCommand(bytearray(b' \x00')),
		A_Pause(70),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(120),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(45)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceSouthwest(),
		A_SequenceLoopingOn()
	]),
	SetSyncActionScript(NPC_0, A1007_EMPTY),
	SetSyncActionScript(NPC_4, A1008_EMPTY),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SequenceLoopingOn(),
		A_Pause(45),
		A_FaceNortheast(),
		A_Pause(30),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(12),
		A_SequenceLoopingOn(),
		A_JumpToHeight(64)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn()
	]),
	Pause(90),
	FadeOutToBlack(sync=False, duration=50),
	Pause(90),
	JmpToEvent(E3868_WORLD_MAP_BOWSERS_KEEP)
])
