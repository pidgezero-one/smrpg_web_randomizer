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
	TransferToXYZF(x=16, y=77, z=0, direction=EAST),
	ShiftEastPixels(16),
	FaceNortheast(),
	VisibilityOn(),
	SetWalkingSpeed(speed=SLOW),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	ShiftNortheastSteps(4),
	FloatingOn(),
	SetSolidityBits(cant_pass_walls=True),
	JumpToHeight(108),
	Walk1StepNortheast(),
	FloatingOff(),
	ClearSolidityBits(cant_pass_walls=True),
	ShiftNortheastPixels(4),
	StartLoopNTimes(2),
	FloatingOff(),
	ClearSolidityBits(cant_pass_walls=True),
	Walk1StepNorthwest(),
	FloatingOn(),
	SetSolidityBits(cant_pass_walls=True),
	JumpToHeight(108),
	Walk1StepNorthwest(),
	EndLoop(),
	FloatingOff(),
	ClearSolidityBits(cant_pass_walls=True),
	ShiftNorthwestPixels(4),
	ShiftSouthwestSteps(5),
	VisibilityOff(),
	Db(bytearray(b'\xfd\xf2')),
	Return()
])
