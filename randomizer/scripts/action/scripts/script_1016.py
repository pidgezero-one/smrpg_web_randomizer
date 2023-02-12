#A1016_FREESTANDING_FLOWER_PICKED_UP

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	SetPriority(3),
	PlaySound(sound=SO014_FLOWER, channel=4),
	StartLoopNTimes(4),
	VisibilityOn(),
	Pause(7),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Db(bytearray(b'\xfd\xf2')),
	Return()
])
