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
	SetMovementsBits(bit_0=True, cant_walk_under=True),
	SetWalkingSpeed(speed=SLOW),
	SequenceLoopingOn(),
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x10\x00\x01\x00\x00\x80\x00\x80')),
	TurnRandomDirection(identifier="ACTION_308_turn_random_direction_5"),
	ShiftFDirectionSteps(2),
	FaceMario(),
	Walk1StepFDirection(),
	TurnRandomDirection(),
	ShiftFDirectionSteps(2),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=4, destinations=["ACTION_308_face_mario_13"]),
	Jmp(["ACTION_308_turn_random_direction_5"]),
	FaceMario(identifier="ACTION_308_face_mario_13"),
	SetWalkingSpeed(speed=NORMAL),
	SetSequenceSpeed(speed=FAST),
	Walk1StepFDirection(),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=NORMAL),
	Jmp(["ACTION_308_turn_random_direction_5"])
])
