#A0800_MUSHROOM_DERBY_UNKNOWN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(10, identifier="ACTION_800_pause_0"),
	SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True),
	SetWalkingSpeed(VERY_FAST),
	ShiftNortheastPixels(1),
	StartLoopNTimes(29),
	ShiftSouthwestPixels(2),
	ShiftNortheastPixels(2),
	EndLoop(),
	ShiftSouthwestPixels(1),
	SetWalkingSpeed(FAST),
	Pause(16),
	ResetProperties(),
	FaceNorthwest(),
	Return()
])
