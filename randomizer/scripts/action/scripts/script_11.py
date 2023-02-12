#A0011_GO_DOWN_PIPE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(),
	FaceSouth(),
	FixedFCoordOn(),
	FloatingOff(),
	ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
	SetWalkingSpeed(FAST),
	RunAwayShift(),
	SetWalkingSpeed(NORMAL),
	SetSolidityBits(cant_pass_walls=True),
	PlaySound(sound=SO028_PIPE_ENTRANCE, channel=6),
	SetSpriteSequence(index=30, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
	ClearSolidityBits(cant_pass_walls=True),
	DecZCoord1Step(),
	ResetProperties(),
	Return()
])
