#A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearBit(TEMP_7044_3),
	SetSequenceSpeed(FAST),
	SetSpriteSequence(index=10, is_sequence=True, looping=True),
	Pause(10),
	SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_571_set_sprite_sequence_4"),
	FixedFCoordOn(),
	SequenceLoopingOn(),
	SetWalkingSpeed(SLOW),
	ShiftWestPixels(1),
	Pause(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftNorthwestPixels(1),
	Pause(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftSoutheastPixels(1),
	Pause(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftEastPixels(1),
	Pause(1),
	SetWalkingSpeed(SLOW),
	ShiftEastPixels(1),
	Pause(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftNortheastPixels(1),
	Pause(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftSouthwestPixels(1),
	Pause(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftWestPixels(1),
	Pause(1),
	Jmp(["ACTION_571_set_sprite_sequence_4"]),
	Return()
])
