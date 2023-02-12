#A0282_KEEP_BALL_SOLITAIRE_BALL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	SetSpriteSequence(index=2, is_sequence=True, looping=False),
	IncPaletteRowBy(1),
	SetPriority(3),
	SetWalkingSpeed(VERY_FAST),
	ShiftSouthwestPixels(10),
	ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetWalkingSpeed(NORMAL),
	Return()
])
