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
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 262, ["ACTION_768_set_priority_21"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 270, ["ACTION_768_set_priority_21"]),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(5),
	EndLoop(),
	SequenceLoopingOn(),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=FAST, identifier="ACTION_768_set_animation_speed_10"),
	TurnClockwise45Degrees(),
	Walk1StepFDirection(),
	SetSequenceSpeed(speed=SLOW),
	Pause(60),
	SetSequenceSpeed(speed=FAST),
	TurnRandomDirection(),
	Walk1StepFDirection(),
	SetSequenceSpeed(speed=VERY_SLOW),
	Pause(30),
	Jmp(["ACTION_768_set_animation_speed_10"]),
	SetPriority(3, identifier="ACTION_768_set_priority_21"),
	SequenceLoopingOn(),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(2),
	EndLoop(),
	FaceMario(identifier="ACTION_768_face_mario_28"),
	SetSequenceSpeed(speed=FAST),
	Pause(32),
	FaceMario(),
	SetSequenceSpeed(speed=VERY_SLOW),
	Pause(32),
	Jmp(["ACTION_768_face_mario_28"])
])
