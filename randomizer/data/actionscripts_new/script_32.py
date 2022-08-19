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
	FaceSoutheast(),
	JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	SetPriority(3),
	Walk1StepSoutheast(),
	ShiftNortheastSteps(2),
	SetPriority(2),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_32_shift_northwest_steps_10"]),
	ShiftNorthwestSteps(4),
	ShiftSouthwestSteps(5),
	Jmp(["ACTION_32_shift_southeast_steps_16"]),
	ShiftNorthwestSteps(2, identifier="ACTION_32_shift_northwest_steps_10"),
	Walk1StepSouthwest(),
	Walk1StepNorthwest(),
	Walk1StepSouthwest(),
	Walk1StepNorthwest(),
	ShiftSouthwestSteps(3),
	ShiftSoutheastSteps(2, identifier="ACTION_32_shift_southeast_steps_16"),
	SetPriority(3),
	JmpIfBitSet(TEMP_7044_0, ["ACTION_32_walk_1_step_northeast_27"]),
	ShiftNortheastSteps(2),
	ShiftZUpSteps(2, identifier="ACTION_32_shift_z_up_steps_20"),
	SetPriority(3),
	Walk1StepFDirection(),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	DecZCoord1Step(),
	VisibilityOff(),
	Return(),
	Walk1StepNortheast(identifier="ACTION_32_walk_1_step_northeast_27"),
	Walk1StepSoutheast(),
	Walk1StepNortheast(),
	Walk1StepSoutheast(),
	Walk1StepNortheast(),
	FaceNorthwest(),
	Walk1StepFDirection(identifier="ACTION_32_walk_1_step_f_direction_33"),
	Jmp(["ACTION_32_shift_z_up_steps_20"])
])
