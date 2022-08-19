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
	SequenceLoopingOn(),
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 78, ["ACTION_474_set_priority_27"]),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(9),
	EndLoop(),
	SetAllSpeeds(speed=SLOW, identifier="ACTION_474_set_animation_speed_8"),
	ShiftFDirectionSteps(2),
	Pause(21),
	TurnClockwise45DegreesNTimes(2),
	Walk1StepFDirection(),
	TurnClockwise45DegreesNTimes(2),
	ShiftFDirectionSteps(2),
	Pause(37),
	StartLoopNTimes(1),
	TurnClockwise45DegreesNTimes(6),
	Walk1StepFDirection(),
	TurnClockwise45DegreesNTimes(6),
	ShiftFDirectionSteps(2),
	Pause(21),
	EndLoop(),
	TurnClockwise45DegreesNTimes(2),
	Walk1StepFDirection(),
	TurnClockwise45DegreesNTimes(2),
	Jmp(["ACTION_474_set_animation_speed_8"]),
	SetPriority(3, identifier="ACTION_474_set_priority_27"),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	VisibilityOn(),
	SetSequenceSpeed(speed=NORMAL),
	SetWalkingSpeed(speed=VERY_SLOW),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(16),
	EndLoop(),
	Jmp(["ACTION_714_turn_clockwise_45_degrees_12"])
])
