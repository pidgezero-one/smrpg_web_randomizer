#A0389_TOWER_BULLET_BILL_APPEARS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShiftToXYCoords(x=15, y=35),
	ShiftSouthPixels(3),
	ShiftNorthwestPixels(11),
	ShiftSouthwestPixels(6),
	Db(bytearray(b'\xfd\x12')),
	VisibilityOn(),
	PlaySound(sound=SO073_THWOMP_STOMP, channel=4),
	SequenceLoopingOn(),
	ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	ShiftSouthwestSteps(10),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	VisibilityOff(),
	Return()
])
