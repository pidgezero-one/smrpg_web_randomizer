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
	SetSolidityBits(bit_4=True),
	SetWalkingSpeed(speed=SLOW),
	FixedFCoordOn(),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 27, ["ACTION_821_set_animation_speed_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_821_shift_southwest_steps_19"]),
	SetPriority(3),
	AddConstToVar(PRIMARY_TEMP_700C, 65515),
	Inc(PRIMARY_TEMP_700C),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(9),
	EndLoop(),
	Set700CToPressedButton(),
	Mem700CAndConst(0x0001),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_821_shift_z_up_steps_16"]),
	Pause(96),
	ShiftZUpSteps(3, identifier="ACTION_821_shift_z_up_steps_16"),
	ShiftZDownSteps(3),
	Jmp(["ACTION_821_shift_z_up_steps_16"]),
	ShiftSouthwestSteps(2, identifier="ACTION_821_shift_southwest_steps_19"),
	ShiftZUpSteps(5),
	Walk1StepSouthwest(),
	Pause(32),
	Walk1StepNortheast(),
	ShiftZDownSteps(5),
	ShiftNortheastSteps(2),
	Pause(32),
	Jmp(["ACTION_821_shift_southwest_steps_19"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_821_set_animation_speed_28"),
	ShiftZUpSteps(3),
	SetWalkingSpeed(speed=NORMAL),
	ShiftZUpSteps(4),
	SetWalkingSpeed(speed=FAST),
	ShiftZUpSteps(3),
	StartLoopNTimes(7),
	ShiftZDownPixels(4),
	ShiftZUpPixels(4),
	EndLoop(),
	SetWalkingSpeed(speed=FASTEST),
	ShiftZDownSteps(10),
	Jmp(["ACTION_821_set_animation_speed_28"])
])
