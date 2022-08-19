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
	ClearSolidityBits(bit_4=True, identifier="ACTION_111_clear_solidity_bits_0"),
	ClearSolidityBits(cant_walk_through=True),
	VisibilityOff(),
	Pause(60),
	FaceSoutheast(),
	VisibilityOn(),
	SetSolidityBits(bit_4=True),
	SetSolidityBits(cant_walk_through=True),
	StartLoopNTimes(4),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Walk1StepSoutheast(),
	ShiftSoutheastPixels(11),
	BPL262728(),
	Pause(2),
	EndLoop(),
	Walk1StepSoutheast(),
	VisibilityOff(),
	ClearSolidityBits(bit_4=True),
	ClearSolidityBits(cant_walk_through=True),
	TransferToXYZF(x=8, y=32, z=4, direction=EAST),
	Pause(240),
	FaceNorthwest(),
	VisibilityOn(),
	SetSolidityBits(bit_4=True),
	SetSolidityBits(cant_walk_through=True),
	StartLoopNTimes(4),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Walk1StepNorthwest(),
	ShiftNorthwestPixels(11),
	BPL262728(),
	Pause(2),
	EndLoop(),
	Walk1StepNorthwest(),
	VisibilityOff(),
	ClearSolidityBits(bit_4=True),
	ClearSolidityBits(cant_walk_through=True),
	TransferToXYZF(x=3, y=23, z=4, direction=EAST),
	Pause(180),
	SetBit(TEMP_7043_1),
	Jmp(["ACTION_111_clear_solidity_bits_0"])
])
