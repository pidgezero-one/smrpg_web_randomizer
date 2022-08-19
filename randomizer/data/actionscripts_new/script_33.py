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
	FaceNortheast(),
	JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	SetPriority(2),
	Walk1StepNortheast(),
	ShiftSoutheastSteps(2),
	SetPriority(3),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_33_shift_southwest_steps_11"]),
	ShiftSouthwestSteps(5),
	SetPriority(2),
	ShiftNorthwestSteps(4),
	Jmp(["ACTION_33_set_priority_18"]),
	ShiftSouthwestSteps(3, identifier="ACTION_33_shift_southwest_steps_11"),
	Walk1StepNorthwest(),
	Walk1StepSouthwest(),
	Walk1StepNorthwest(),
	Walk1StepSouthwest(),
	SetPriority(2),
	ShiftNorthwestSteps(2),
	SetPriority(3, identifier="ACTION_33_set_priority_18"),
	ShiftNortheastSteps(3),
	SetPriority(2),
	JmpIfBitSet(TEMP_7044_0, ["ACTION_33_walk_1_step_northeast_24"]),
	Walk1StepSoutheast(),
	Jmp(["ACTION_32_shift_z_up_steps_20"]),
	Walk1StepNortheast(identifier="ACTION_33_walk_1_step_northeast_24"),
	Walk1StepSoutheast(),
	Walk1StepNortheast(),
	Walk1StepSoutheast(),
	FaceSouthwest(),
	Jmp(["ACTION_32_walk_1_step_f_direction_33"])
])
