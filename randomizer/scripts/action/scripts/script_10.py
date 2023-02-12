#A0010_FALL_ON_TRAMPOLINE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(),
	ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
	SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True),
	FaceSouth(),
	FixedFCoordOn(),
	PlaySound(sound=SO028_PIPE_ENTRANCE, channel=6),
	AddZCoord1Step(),
	SetSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
	ResetProperties(),
	FixedFCoordOff(),
	ShadowOn(),
	FloatingOn(),
	ClearBit(TEMP_707C_0),
	Return()
])
