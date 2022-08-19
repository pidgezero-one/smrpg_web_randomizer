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
	TransferToXYZF(x=15, y=55, z=2, direction=EAST),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=FAST),
	VisibilityOn(),
	ClearSolidityBits(cant_pass_walls=True),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetBit(ROSE_TOWN_WATER_PUMPERS_POSITION),
	Walk1StepSoutheast(),
	FaceNorthwest(),
	Pause(60),
	SetSolidityBits(cant_walk_through=True),
	ShiftSoutheastSteps(4),
	SetSolidityBits(cant_pass_walls=True),
	FloatingOn(),
	ShiftSouthwestSteps(2),
	ClearSolidityBits(cant_pass_walls=True),
	FloatingOff(),
	ShiftSouthwestSteps(3),
	FaceNorthwest(),
	Pause(60),
	Walk1StepNortheast(),
	FaceNorthwest(),
	FixedFCoordOn(),
	StartLoopNTimes(2),
	SetWalkingSpeed(speed=FAST),
	ShiftZUpPixels(6),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftZDownPixels(6),
	Pause(30),
	EndLoop(),
	FixedFCoordOff(),
	SetWalkingSpeed(speed=SLOW),
	Walk1StepSouthwest(),
	FaceNorthwest(),
	Pause(60),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftNortheastSteps(3),
	SetSolidityBits(cant_pass_walls=True),
	FloatingOn(),
	ShiftNortheastSteps(2),
	ClearSolidityBits(cant_pass_walls=True),
	FloatingOff(),
	ShiftNorthwestSteps(4),
	Pause(30),
	ClearBit(ROSE_TOWN_WATER_PUMPERS_POSITION),
	ClearSolidityBits(cant_walk_through=True),
	Walk1StepNorthwest(),
	VisibilityOff(),
	TransferToXYZF(x=22, y=77, z=0, direction=EAST),
	Return()
])
