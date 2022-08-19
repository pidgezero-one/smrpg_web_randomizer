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
	SetWalkingSpeed(speed=SLOW),
	SetPriority(3),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(1),
	EndLoop(),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 27, ["ACTION_828_shift_northeast_steps_37"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 26, ["ACTION_828_shift_southwest_steps_33"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_828_shift_northwest_steps_29"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_828_shift_southwest_steps_26"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_828_shift_southeast_steps_19"]),
	ShiftNortheastSteps(6, identifier="ACTION_828_shift_northeast_steps_13"),
	ShiftNorthwestSteps(2),
	ShiftNortheastSteps(2),
	ShiftNorthwestSteps(4),
	ShiftNortheastSteps(2),
	ShiftNorthwestSteps(5),
	ShiftSoutheastSteps(5, identifier="ACTION_828_shift_southeast_steps_19"),
	ShiftSouthwestSteps(2),
	ShiftSoutheastSteps(4),
	ShiftSouthwestSteps(2),
	ShiftSoutheastSteps(2),
	ShiftSouthwestSteps(6),
	Jmp(["ACTION_828_shift_northeast_steps_13"]),
	ShiftSouthwestSteps(2, identifier="ACTION_828_shift_southwest_steps_26"),
	ShiftSoutheastSteps(5),
	Walk1StepSouthwest(),
	ShiftNorthwestSteps(3, identifier="ACTION_828_shift_northwest_steps_29"),
	ShiftNortheastSteps(3),
	ShiftNorthwestSteps(2),
	Jmp(["ACTION_828_shift_southwest_steps_26"]),
	ShiftSouthwestSteps(2, identifier="ACTION_828_shift_southwest_steps_33"),
	ShiftNorthwestSteps(2),
	ShiftSouthwestSteps(2),
	Walk1StepNorthwest(),
	ShiftNortheastSteps(3, identifier="ACTION_828_shift_northeast_steps_37"),
	ShiftSoutheastSteps(3),
	Walk1StepNortheast(),
	Jmp(["ACTION_828_shift_southwest_steps_33"])
])
