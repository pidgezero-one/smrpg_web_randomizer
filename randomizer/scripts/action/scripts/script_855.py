#A0855_PLAYER_DIZZY_FROM_GARDENER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	OverwriteSolidity(),
	SetWalkingSpeed(SLOW),
	WalkToXYCoords(x=24, y=18),
	PlaySound(sound=SO031_SPINNING_FLOWER, channel=4),
	StartLoopNTimes(1),
	FaceSouthwest(),
	Pause(3),
	FaceWest(),
	Pause(3),
	FaceNorthwest(),
	Pause(3),
	FaceNorth(),
	Pause(3),
	FaceNortheast(),
	Pause(3),
	FaceEast(),
	Pause(3),
	FaceSoutheast(),
	Pause(3),
	FaceSouth(),
	Pause(3),
	EndLoop(),
	SetSpriteSequence(index=1, sprite_offset=3, is_sequence=True, looping=True),
	FaceSouth(),
	PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	Return()
])
