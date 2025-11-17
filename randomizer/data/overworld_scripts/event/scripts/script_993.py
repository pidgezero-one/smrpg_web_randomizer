# E0993_EMPTY

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
	EnterArea(room_id=R245_GAME_INTRO_PIPE_VAULT_AREA_02_WTHWOMP, face_direction=NORTHEAST, x=22, y=33, z=1),
	RunBackgroundEvent(event_id=E0429_PIPE_VAULT_THWOMP_ROOM_LOADER_BACKGROUND, return_on_level_exit=True),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastSteps(3),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastSteps(6)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_JumpToHeight(height=96, silent=True),
		A_WalkNortheastSteps(2),
		A_Pause(1, identifier="EVENT_993_action_queue_3_SUBSCRIPT_pause_3"),
		A_JmpIfMarioInAir(["EVENT_993_action_queue_3_SUBSCRIPT_pause_3"]),
		A_JumpToHeight(height=96, silent=True),
		A_WalkNortheastSteps(2),
		A_Pause(1, identifier="EVENT_993_action_queue_3_SUBSCRIPT_pause_7"),
		A_JmpIfMarioInAir(["EVENT_993_action_queue_3_SUBSCRIPT_pause_7"]),
		A_JumpToHeight(height=96, silent=True),
		A_WalkNortheastSteps(2),
		A_Pause(1, identifier="EVENT_993_action_queue_3_SUBSCRIPT_pause_11"),
		A_JmpIfMarioInAir(["EVENT_993_action_queue_3_SUBSCRIPT_pause_11"]),
		A_JumpToHeight(height=96, silent=True),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(4),
		A_Pause(1, identifier="EVENT_993_action_queue_3_SUBSCRIPT_pause_16"),
		A_JmpIfMarioInAir(["EVENT_993_action_queue_3_SUBSCRIPT_pause_16"]),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast(),
		A_JumpToHeight(height=96, silent=True),
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_WalkNortheastPixels(4),
		A_Pause(1, identifier="EVENT_993_action_queue_3_SUBSCRIPT_pause_24"),
		A_JmpIfMarioInAir(["EVENT_993_action_queue_3_SUBSCRIPT_pause_24"]),
		A_JumpToHeight(height=108, silent=True),
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(1),
		A_FloatingOff(),
		A_SetSpriteSequence(index=9, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_ShadowOn(),
		A_Pause(60),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZDownSteps(4),
		A_SetBit(TEMP_7043_1),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_Pause(2),
		A_ClearBit(TEMP_7043_1),
		A_Pause(28),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZUpSteps(10)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(60),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(4),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Pause(80),
		A_VisibilityOn(),
		A_SetPriority(3),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_AddZCoord1Step(),
		A_ShiftZUpPixels(12),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(48)
	]),
	Pause(16),
	FadeInFromBlack(sync=True),
	Pause(98),
	FadeOutToBlack(sync=True, duration=30),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E0138_EMPTY)
])
