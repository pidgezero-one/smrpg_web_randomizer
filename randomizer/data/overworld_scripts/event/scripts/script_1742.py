# E1742_EMPTY

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
	StopBackgroundEvent(TIMER_701C),
	ClearBit(TEMP_7043_5),
	EnableControlsUntilReturn([]),
	JmpIfMarioOnAnObjectOrNot(['EVENT_1742_set_var_to_const_18', 'EVENT_1742_action_queue_7']),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_7000, 256),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1742_set_var_to_const_18"]),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	], identifier="EVENT_1742_action_queue_7"),
	ResumeActionScript(MEM_70A8),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSpriteSequence(index=7, sprite_offset=3, is_sequence=True, looping=True),
		A_JumpToHeight(height=112, silent=True),
		A_SetWalkingSpeed(NORMAL),
		A_FloatingOn(),
		A_Pause(20),
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	EnableControlsUntilReturn([B]),
	CompareVarToConst(SECONDARY_TEMP_7024, 0),
	JmpIfLoadedMemoryIsBelow0(["EVENT_1742_resume_background_event_16"]),
	SetVarToConst(TIMER_701C, 2),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E3505_BOOSTER_HILL_UNKNOWN, timer_var=TIMER_701C, bit_4=True, bit_5=True),
	Return(),
	ResumeBackgroundEvent(TIMER_701C, identifier="EVENT_1742_resume_background_event_16"),
	Return(),
	SetVarToConst(TEMP_7028, 36, identifier="EVENT_1742_set_var_to_const_18"),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ResumeActionScript(MEM_70A8),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_700C),
		A_AddVarTo700C(TEMP_7028),
		A_CompareVarToConst(PRIMARY_TEMP_700C, 64),
		A_JmpIfLoadedMemoryIsAboveOrEqual0(["EVENT_1742_action_queue_21_SUBSCRIPT_copy_var_to_var_6"]),
		A_Jmp(["EVENT_1742_action_queue_21_SUBSCRIPT_set_var_to_const_8"]),
		A_CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_700C, identifier="EVENT_1742_action_queue_21_SUBSCRIPT_copy_var_to_var_6"),
		A_Jmp(["EVENT_1742_action_queue_21_SUBSCRIPT_set_animation_speed_15"]),
		A_SetVarToConst(PRIMARY_TEMP_700C, 64, identifier="EVENT_1742_action_queue_21_SUBSCRIPT_set_var_to_const_8"),
		A_DecVarFrom700C(SECONDARY_TEMP_7024),
		A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_1742_action_queue_21_SUBSCRIPT_set_animation_speed_15"]),
		A_FloatingOff(),
		A_JumpToHeight(height=108, silent=True),
		A_FloatingOn(),
		A_Jmp(["EVENT_1742_action_queue_21_SUBSCRIPT_set_solidity_bits_23"]),
		A_SetWalkingSpeed(NORMAL, identifier="EVENT_1742_action_queue_21_SUBSCRIPT_set_animation_speed_15"),
		A_FloatingOff(),
		A_JumpToHeight(height=108, silent=True),
		A_FloatingOn(),
		A_LoadMemory(PRIMARY_TEMP_700C),
		A_WalkNorthwestPixels(1),
		A_Inc(SECONDARY_TEMP_7024),
		A_EndLoop(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True, identifier="EVENT_1742_action_queue_21_SUBSCRIPT_set_solidity_bits_23")
	]),
	EnableControlsUntilReturn([B]),
	CompareVarToConst(SECONDARY_TEMP_7024, 0),
	JmpIfLoadedMemoryIsAboveOrEqual0(["EVENT_1742_resume_background_event_16"]),
	SetVarToConst(TIMER_701C, 180),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E3505_BOOSTER_HILL_UNKNOWN, timer_var=TIMER_701C, bit_4=True, bit_5=True),
	Return()
])
