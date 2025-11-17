# E1720_EMPTY

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
	JmpIfBitSet(TEMP_7043_5, ["EVENT_1720_ret_41"]),
	SetBit(TEMP_7043_5),
	SetVarToConst(SECONDARY_TEMP_7024, 20),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	DecVarFrom7000(SECONDARY_TEMP_7024),
	Mem7000AndConst(0x0004),
	AddVarTo7000(SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_702E),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	Set7000ToObjectCoord(target_npc=MEM_70AA, coord=COORD_F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	StartLoopNTimes(3),
	PauseActionScript(MEM_70AA),
	Inc(TEMP_70AA),
	EndLoop(),
	CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=PRIMARY_TEMP_700C),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_JumpToHeight(height=144, silent=True),
		A_WalkSoutheastPixels(20)
	]),
	Inc(TEMP_70AF),
	JmpIfVarNotEqualsConst(TEMP_70AF, 8, ["EVENT_1720_summon_to_current_level_at_marios_coords_22"]),
	SetBit(TEMP_7044_6),
	FadeOutToBlack(sync=True, duration=30),
	SummonObjectToCurrentLevelAtMariosCoords(MEM_70AB, identifier="EVENT_1720_summon_to_current_level_at_marios_coords_22"),
	StartSyncEmbeddedActionScript(target=MEM_70AB, prefix=0xF1, subscript=[
		A_ShadowOn(),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetPriority(3),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_AddConstToVar(PRIMARY_TEMP_700C, 2),
		A_Mem700CAndConst(0x0004),
		A_Mem700CXorConst(0x0004),
		A_FaceEast7C(),
		A_FloatingOff(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x08\xb0\xff')),
		A_Walk1StepFDirection(),
		A_VisibilityOff(),
		A_BPL262728()
	]),
	Pause(1),
	CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	StartLoopNTimes(3),
	ActionQueueSync(target=MEM_70AA, subscript=[
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(16),
		A_ShiftZDownPixels(16)
	]),
	Inc(TEMP_70AA),
	Pause(3),
	EndLoop(),
	Dec(TEMP_70AA),
	StopEmbeddedActionScript(MEM_70AA),
	CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	StartLoopNTimes(3),
	ResumeActionScript(MEM_70AA),
	Inc(TEMP_70AA),
	EndLoop(),
	ClearBit(TEMP_7043_5),
	Return(identifier="EVENT_1720_ret_41")
])
