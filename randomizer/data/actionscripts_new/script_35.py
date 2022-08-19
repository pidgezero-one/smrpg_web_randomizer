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
	JmpIfBitSet(TEMP_7044_5, ["ACTION_35_jmp_if_bit_set_3"]),
	JmpIfBitSet(TEMP_7044_6, ["ACTION_35_face_southwest_31"]),
	Jmp(["ACTION_35_face_southwest_21"]),
	JmpIfBitSet(TEMP_7044_6, ["ACTION_35_face_southwest_11"], identifier="ACTION_35_jmp_if_bit_set_3"),
	FaceNortheast(),
	JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	SetPriority(2),
	ShiftNortheastSteps(2),
	SetPriority(3),
	ShiftNortheastSteps(2),
	Jmp(["ACTION_32_shift_z_up_steps_20"]),
	FaceSouthwest(identifier="ACTION_35_face_southwest_11"),
	JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	SetPriority(3),
	Walk1StepSouthwest(),
	Walk1StepSoutheast(),
	ShiftNortheastSteps(10),
	SetPriority(2),
	Walk1StepNorthwest(),
	Walk1StepSouthwest(),
	Jmp(["ACTION_32_shift_z_up_steps_20"]),
	FaceSouthwest(identifier="ACTION_35_face_southwest_21"),
	JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	SetPriority(3),
	Walk1StepSouthwest(),
	Walk1StepNorthwest(),
	SetPriority(2),
	ShiftNortheastSteps(10),
	Walk1StepSoutheast(),
	Walk1StepSouthwest(),
	Jmp(["ACTION_32_shift_z_up_steps_20"]),
	FaceSouthwest(identifier="ACTION_35_face_southwest_31"),
	JmpToSubroutine(["ACTION_34_clear_solidity_bits_48"]),
	SetPriority(3),
	Walk1StepSouthwest(),
	Walk1StepSoutheast(),
	ShiftNortheastSteps(10),
	Walk1StepSoutheast(),
	ShiftSouthwestSteps(5),
	SetPriority(2),
	StartLoopNTimes(2),
	Walk1StepNorthwest(),
	Walk1StepSouthwest(),
	EndLoop(),
	ShiftSouthwestSteps(2),
	SetPriority(3),
	Walk1StepSoutheast(),
	Walk1StepNortheast(),
	Jmp(["ACTION_32_shift_z_up_steps_20"])
])
