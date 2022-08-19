#classes
from randomizer.types.actionscripts.commands import *
from randomizer.types.actionscripts.classes import ActionScript
#ids
from randomizer.types.eventscripts.constants.script_ids import *
from randomizer.types.actionscripts.constants.script_ids import *
from randomizer.types.packets.constants.packet_ids import *
from randomizer.types.constants.sound_names import *
from randomizer.types.constants.directions import *
#types
from randomizer.types.constants.area_objects import *
from randomizer.types.constants.coords import *
from randomizer.types.actionscripts.constants.sequence_speeds import *
from randomizer.types.actionscripts.constants.vram_priority import *
from randomizer.types.variables.variables import *

script = ActionScript([
	SequenceLoopingOn(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Db(bytearray(b'\xfd\x12')),
	FloatingOff(),
	ClearSolidityBits(cant_pass_walls=True),
	TransferToXYZF(x=13, y=71, z=16, direction=EAST),
	ShiftEastPixels(16),
	FaceNortheast(),
	VisibilityOn(),
	SetWalkingSpeed(speed=SLOW),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	ShiftNortheastSteps(5),
	FloatingOn(),
	SetSolidityBits(cant_pass_walls=True),
	StartLoopNTimes(2),
	Walk1StepSoutheast(),
	FloatingOff(),
	ClearSolidityBits(cant_pass_walls=True),
	ShiftSoutheastPixels(6),
	FloatingOn(),
	SetSolidityBits(cant_pass_walls=True),
	JumpToHeight(0),
	ShiftSoutheastPixels(10),
	EndLoop(),
	Pause(16),
	Walk1StepSouthwest(),
	ShiftSouthwestPixels(8),
	JumpToHeight(0),
	Walk1StepSouthwest(),
	FloatingOff(),
	ClearSolidityBits(cant_pass_walls=True),
	ShiftSouthwestSteps(2),
	ShiftSouthwestPixels(8),
	Db(bytearray(b'\xfd\xf2')),
	VisibilityOff(),
	Return()
])
