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
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 457, ["ACTION_714_set_animation_speed_19"]),
	SetPriority(3),
	SequenceLoopingOn(),
	ShadowOn(),
	SetSequenceSpeed(speed=NORMAL),
	SetWalkingSpeed(speed=VERY_SLOW),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(1),
	EndLoop(),
	TurnClockwise45Degrees(identifier="ACTION_714_turn_clockwise_45_degrees_12"),
	ShiftFDirectionSteps(2),
	TurnRandomDirection(),
	ShiftFDirectionSteps(2),
	FaceMario(),
	Walk1StepFDirection(),
	Jmp(["ACTION_714_turn_clockwise_45_degrees_12"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_714_set_animation_speed_19"),
	SetSequenceSpeed(speed=NORMAL),
	FaceMario(identifier="ACTION_714_face_mario_21"),
	ShiftFDirectionSteps(2),
	TurnRandomDirection(),
	Walk1StepFDirection(),
	TurnClockwise45Degrees(),
	Walk1StepFDirection(),
	Jmp(["ACTION_714_face_mario_21"])
])
