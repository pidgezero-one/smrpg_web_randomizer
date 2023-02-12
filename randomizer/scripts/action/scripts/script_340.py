#A0340_SHIP_PUZZLE_HINT_VANISH

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=4),
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	JumpToHeight(height=160, silent=True),
	Pause(13),
	FloatingOff(),
	StartLoopNTimes(7),
	VisibilityOff(),
	Pause(2),
	VisibilityOn(),
	Pause(2),
	EndLoop(),
	VisibilityOff(),
	Return()
])
