#A0533_MUSHROOM_WAY_1_TROOPA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x06\x00\x01\x00\x00\x00\x04\x80')),
	SetSequenceSpeed(FAST, identifier="ACTION_533_set_animation_speed_2"),
	SetWalkingSpeed(NORMAL),
	ShiftNortheastSteps(1),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(SLOW),
	ShiftNortheastSteps(1),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(NORMAL),
	ShiftSoutheastSteps(1),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(SLOW),
	ShiftSoutheastSteps(1),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(NORMAL),
	ShiftSouthwestSteps(1),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(SLOW),
	ShiftSouthwestSteps(1),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(NORMAL),
	ShiftNorthwestSteps(1),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(SLOW),
	ShiftNorthwestSteps(1),
	Jmp(["ACTION_533_set_animation_speed_2"])
])
