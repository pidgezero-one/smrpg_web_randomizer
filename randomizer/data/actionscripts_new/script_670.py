#classes
from randomizer.types.actionscripts.commands import *
from randomizer.types.actionscripts.classes import ActionScript
#ids
from randomizer.types.eventscripts.constants.script_ids import *
from randomizer.types.actionscripts.constants.script_ids import *
from randomizer.types.packets.constants.packet_ids import *
from randomizer.types.constants.sound_names import *
from randomizer.types.constants.directions import *
#types
from randomizer.types.constants.area_objects import *
from randomizer.types.constants.coords import *
from randomizer.types.actionscripts.constants.sequence_speeds import *
from randomizer.types.actionscripts.constants.vram_priority import *
from randomizer.types.variables.variables import *

script = ActionScript([
	Set700CToObjectCoord(object=MARIO, coord=F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ROSE_WAY_7038),
	JmpIfVarEqualsConst(ROSE_WAY_7038, 1, ["ACTION_670_start_loop_n_times_15"]),
	JmpIfVarEqualsConst(ROSE_WAY_7038, 3, ["ACTION_670_start_loop_n_times_22"]),
	JmpIfVarEqualsConst(ROSE_WAY_7038, 5, ["ACTION_670_start_loop_n_times_29"]),
	JmpIfVarEqualsConst(ROSE_WAY_7038, 7, ["ACTION_670_start_loop_n_times_36"]),
	CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_700C),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70AB),
	Db(bytearray(b'\xfd$\x00\x13')),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=PRIMARY_TEMP_7000),
	Mem700CAndConst(0x00C0),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_670_start_loop_n_times_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 64, ["ACTION_670_start_loop_n_times_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 128, ["ACTION_670_start_loop_n_times_29"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 192, ["ACTION_670_start_loop_n_times_36"]),
	StartLoopNTimes(2, identifier="ACTION_670_start_loop_n_times_15"),
	SetSpriteSequence(index=6, is_mold=True, mirror_sprite=True),
	Pause(5),
	SetSpriteSequence(index=0, is_mold=True, mirror_sprite=True),
	Pause(5),
	EndLoop(),
	Jmp(["ACTION_670_reset_properties_42"]),
	StartLoopNTimes(2, identifier="ACTION_670_start_loop_n_times_22"),
	SetSpriteSequence(index=6, is_mold=True),
	Pause(5),
	SetSpriteSequence(index=0, is_mold=True),
	Pause(5),
	EndLoop(),
	Jmp(["ACTION_670_reset_properties_42"]),
	StartLoopNTimes(2, identifier="ACTION_670_start_loop_n_times_29"),
	SetSpriteSequence(index=3, is_mold=True),
	Pause(5),
	SetSpriteSequence(index=7, is_mold=True),
	Pause(5),
	EndLoop(),
	Jmp(["ACTION_670_reset_properties_42"]),
	StartLoopNTimes(2, identifier="ACTION_670_start_loop_n_times_36"),
	SetSpriteSequence(index=3, is_mold=True, mirror_sprite=True),
	Pause(5),
	SetSpriteSequence(index=7, is_mold=True, mirror_sprite=True),
	Pause(5),
	EndLoop(),
	ResetProperties(identifier="ACTION_670_reset_properties_42"),
	CopyVarToVar(from_var=ROSE_WAY_7038, to_var=PRIMARY_TEMP_700C),
	FaceEast7C(),
	ClearBit(TEMP_7044_7),
	Return()
])
