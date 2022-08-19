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
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	TransferToXYZF(x=15, y=55, z=2, direction=EAST),
	FaceSoutheast(),
	VisibilityOn(),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=FAST),
	ShiftSoutheastSteps(2),
	SetSolidityBits(cant_walk_through=True),
	Walk1StepNortheast(),
	FaceSouthwest(),
	SetSequenceSpeed(speed=SLOW),
	SetBit(TEMP_7043_7),
	Return()
])
