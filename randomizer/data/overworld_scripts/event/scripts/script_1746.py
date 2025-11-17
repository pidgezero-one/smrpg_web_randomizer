# E1746_EMPTY

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
	EnableControls([], identifier="EVENT_1746_enable_controls_0"),
	EnterArea(room_id=R149_GAME_INTRO_MIDAS_RIVER_BARREL_JUMPING, face_direction=SOUTHWEST, x=13, y=16, z=3),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7026, 22),
	SetVarToConst(TEMP_7028, 21),
	RunBackgroundEvent(event_id=E1585_MIDAS_RIVER_BARREL_SUBROUTINE, return_on_level_exit=True),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthSteps(4)
	]),
	FreezeCamera(),
	Set7016701BToObjectXYZ(target=NPC_1, bit_7=True),
	SetAsyncActionScript(NPC_9, A0170_MIDAS_BARRELS_WATER_SPLASH),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	FadeInFromBlack(sync=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
		A_FloatingOff(),
		A_TransferToXYZF(x=13, y=16, z=17, direction=EAST),
		A_Pause(9),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSpriteSequence(index=8, sprite_offset=3, is_sequence=True, looping=True),
		A_JumpToHeight(height=0, silent=True),
		A_FloatingOn()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(2)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(4),
		A_SetWalkingSpeed(FAST)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_JumpToHeight(height=64, silent=True),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True, looping=True),
		A_Pause(20),
		A_ResetProperties(),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn(),
		A_FloatingOn(),
		A_ShadowOn()
	]),
	SetSyncActionScript(NPC_1, A0593_MIDAS_BARREL_AREA_MOVE_SOUTHWEST_REPEATEDLY),
	SetSyncActionScript(MARIO, A0593_MIDAS_BARREL_AREA_MOVE_SOUTHWEST_REPEATEDLY),
	SetSyncActionScript(SCREEN_FOCUS, A0592_MIDAS_BARREL_CAMERA),
	MoveScriptToBackgroundThread2(),
	SetVarToConst(TIMER_701C, 300),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E1747_EMPTY, timer_var=TIMER_701C, bit_4=True, bit_5=True),
	SetVarToConst(TIMER_701E, 140),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E1749_EMPTY, timer_var=TIMER_701E, bit_4=True, bit_5=True),
	Pause(1, identifier="EVENT_1746_pause_25"),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1746_clear_bit_29"]),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_1746_copy_var_to_var_45"]),
	Jmp(["EVENT_1746_pause_25"]),
	ClearBit(TEMP_7044_7, identifier="EVENT_1746_clear_bit_29"),
	PauseActionScript(MARIO),
	PauseActionScript(SCREEN_FOCUS),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(8),
		A_WalkSouthPixels(4),
		A_SetWalkingSpeed(FAST)
	]),
	PauseActionScript(MEM_70A9),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=64, silent=True),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True, looping=True)
	]),
	ResumeActionScript(MARIO),
	StoreSetBits(TEMP_7044_6),
	Pause(19),
	ResumeActionScript(SCREEN_FOCUS),
	Pause(1),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_ResetProperties()
	]),
	AddConstToVar(TEMP_702C, 65526),
	Jmp(["EVENT_1746_pause_25"]),
	CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1746_copy_var_to_var_45"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	SetSyncActionScript(MEM_70A9, A0592_MIDAS_BARREL_CAMERA),
	SetSyncActionScript(MARIO, A0592_MIDAS_BARREL_CAMERA),
	FadeOutToBlack(sync=False, duration=30),
	JmpToEvent(E1729_EMPTY)
])
