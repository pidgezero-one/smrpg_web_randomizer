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
	SetSolidityBits(cant_pass_walls=True),
	FloatingOn(),
	FaceSouthwest(),
	TransferToXYZF(x=7, y=59, z=3, direction=EAST),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=NORMAL),
	ShiftSouthwestSteps(3),
	SetSequenceSpeed(speed=SLOW),
	FaceNorthwest(),
	Pause(60),
	SetSequenceSpeed(speed=NORMAL),
	Walk1StepSouthwest(),
	FaceSoutheast(),
	SetBit(TEMP_7044_3),
	Pause(1),
	ClearBit(TEMP_7044_3),
	Pause(29),
	Walk1StepSoutheast(),
	TransferToXYZF(x=6, y=88, z=0, direction=EAST),
	ClearSolidityBits(cant_pass_walls=True),
	FloatingOff(),
	SetBit(EMPLOYMENT_704C_2),
	Return()
])
