#A0570_MELODY_BAY_TADPOLE_SWIMS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetVarToConst(Y_COORD_1, 6),
	SetPriority(3),
	SetSequenceSpeed(FAST),
	VisibilityOn(),
	SetSpriteSequence(index=10, is_sequence=True, looping=True),
	Pause(10),
	SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_570_set_sprite_sequence_6"),
	StartLoopNTimes(5),
	SetBit(TEMP_7044_3),
	Pause(20),
	ClearBit(TEMP_7044_3),
	SetWalkingSpeed(FASTEST),
	ShiftSoutheastPixels(10),
	SetWalkingSpeed(FAST),
	ShiftSoutheastPixels(4),
	SetWalkingSpeed(NORMAL),
	ShiftSoutheastPixels(2),
	Dec(Y_COORD_1),
	EndLoop(),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	StartLoopNTimes(5),
	SetBit(TEMP_7044_3),
	Pause(20),
	ClearBit(TEMP_7044_3),
	SetWalkingSpeed(FASTEST),
	ShiftNorthwestPixels(10),
	SetWalkingSpeed(FAST),
	ShiftNorthwestPixels(4),
	SetWalkingSpeed(NORMAL),
	ShiftNorthwestPixels(2),
	Inc(Y_COORD_1),
	EndLoop(),
	Jmp(["ACTION_570_set_sprite_sequence_6"])
])
