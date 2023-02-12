#A1023_ERUPTED_MAGMITES

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Db(bytearray(b'\xfd\xf2')),
	VisibilityOff(),
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	EndAll(),
	SetPaletteRow(253),
	RemoveFromLevel(DUMMY_0X06, R001_____BLUE_BG_NOTHING_THERE),
	SummonObjectAt70A8ToCurrentLevel(),
	EndAll(),
	Pause(64),
	BPL262728(),
	VisibilityOff(),
	EndAll(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Db(bytearray(b'\xfd\xf2')),
	VisibilityOff(),
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
])
