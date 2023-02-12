#A0039_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_TINY_FISH

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOn(),
	StartLoopNTimes(2),
	Pause(1, identifier="ACTION_39_pause_2"),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_39_pause_2"]),
	TransferToXYZF(x=29, y=29, z=0, direction=EAST),
	SetPriority(3),
	SetVRAMPriority(PRIORITY_3),
	SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	VisibilityOn(),
	SetWalkingSpeed(FAST),
	JumpToHeight(96),
	ShiftSoutheastSteps(3),
	VisibilityOff(),
	ClearBit(TEMP_7043_1),
	EndLoop(),
	Pause(1, identifier="ACTION_39_pause_15"),
	JmpIfBitClear(TEMP_7043_2, ["ACTION_39_pause_15"]),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	VisibilityOn(),
	Db(bytearray(b'\x97\x17'), identifier="ACTION_39_db_20"),
	JmpIfBitClear(TEMP_7043_3, ["ACTION_39_db_20"]),
	JumpToHeight(120),
	SetWalkingSpeed(SLOW),
	Walk1StepNorthwest(),
	ShiftNorthwestPixels(4),
	FloatingOff(),
	Return()
])
