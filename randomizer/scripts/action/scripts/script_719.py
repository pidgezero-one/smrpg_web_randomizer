#A0719_MIDAS_RIVER_FROG_COIN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	SetBit(MIDAS_RIVER_TUNNEL_3_PRIZE),
	SetVRAMPriority(PRIORITY_3),
	SetPriority(3),
	SetSpriteSequence(index=2, looping=False),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(VERY_FAST),
	AddZCoord1Step(),
	Pause(24),
	VisibilityOff(),
	Db(bytearray(b'\xfd\xf2')),
	Return()
])
