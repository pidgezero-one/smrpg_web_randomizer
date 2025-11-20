# E1738_EMPTY
# pyright: reportWildcardImportFromLibrary=false

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
	EnableControls([], identifier="EVENT_1738_enable_controls_0"),
	EnterArea(room_id=R150_GAME_INTRO_MOLEVILLE_OUTSIDE_DURING_BOWSERS_TROOP_SCENE, face_direction=SOUTH, x=19, y=31, z=0),
	SetSyncActionScript(MARIO, A0771_EMPTY),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNorthwest(),
		A_Pause(10),
		A_SetSpriteSequence(index=3, looping=False),
		A_Walk1StepSouthwest(),
		A_Pause(10),
		A_SetSpriteSequence(index=3, looping=False, mirror_sprite=True),
		A_Walk1StepSoutheast(),
		A_Pause(10),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(40),
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_FaceSoutheast(),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_JumpToHeight(64),
		A_Pause(24)
	]),
	FreezeAllNPCsUntilReturn(),
	ResumeActionScript(MARIO),
	ActionQueueSync(target=NPC_3, subscript=[
		A_JumpToHeight(64),
		A_Pause(24),
		A_ResetProperties()
	]),
	StartSyncEmbeddedActionScript(target=NPC_4, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=27, y=42),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	StartSyncEmbeddedActionScript(target=NPC_2, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ResetProperties(),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=26, y=44),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	StartSyncEmbeddedActionScript(target=NPC_5, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=27, y=43),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	StartSyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=26, y=45),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	StartSyncEmbeddedActionScript(target=NPC_6, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=28, y=44),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	StartAsyncEmbeddedActionScript(target=NPC_1, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FAST),
		A_WalkToXYCoords(x=27, y=46),
		A_FaceNorthwest(),
		A_SequenceLoopingOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FloatingOn(),
		A_WalkSouthwestSteps(2),
		A_Pause(1, identifier="EVENT_1738_action_queue_15_SUBSCRIPT_pause_2"),
		A_JmpIfObjectInAir(NPC_3, ["EVENT_1738_action_queue_15_SUBSCRIPT_pause_2"])
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkNorthPixels(4),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(4)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepSouth(),
		A_WalkSouthPixels(8)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkSouthSteps(2),
		A_SetSequenceSpeed(SLOW)
	]),
	CircleMaskShrinkToObject(target=NPC_3, width=30, speed=5, static=False),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=8, looping=False, mirror_sprite=True),
		A_Pause(80)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkSoutheastSteps(2)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthPixels(24)
	]),
	DisplayIntroTitleText(text=KING_BOWSER, y=6),
	Pause(120),
	FadeOutToBlack(sync=False, duration=30),
	JmpToEvent(E1730_EMPTY)
])
