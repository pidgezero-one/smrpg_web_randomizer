#A0038_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_LAKITU

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(),
	ShadowOn(),
	SetPriority(3),
	SetSpriteSequence(index=6, is_sequence=True, looping=True),
	ShiftEastPixels(8),
	FaceSouthwest(),
	StartLoopNTimes(2),
	Pause(15),
	SetWalkingSpeed(FAST),
	SetBit(TEMP_7043_1),
	ShiftZUpPixels(10),
	ShiftZDownPixels(10),
	Pause(20),
	EndLoop(),
	Pause(30),
	SetBit(TEMP_7043_4),
	SetSpriteSequence(index=3, looping=False),
	Pause(60),
	SetAllSpeeds(NORMAL),
	FixedFCoordOn(),
	ShiftWestSteps(4),
	SetAllSpeeds(FAST),
	ShiftNorthwestSteps(6),
	ShiftNorthSteps(2),
	SetBit(TEMP_7043_4),
	SetSpriteSequence(index=3, looping=False),
	Return()
])
