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
	ClearSolidityBits(cant_pass_walls=True),
	ClearBit(TEMP_7043_0),
	SetVarToConst(X_COORD_2, 4608),
	SetVarToConst(Y_COORD_2, 13568),
	SetVarToConst(Z_COORD_2, 0),
	TransferTo70167018701A(),
	SetAllSpeeds(speed=NORMAL),
	VisibilityOn(),
	ShiftNortheastSteps(6),
	Walk1StepNorth(),
	ShiftNorthwestSteps(4),
	ShiftNorthSteps(2),
	ShiftNorthwestSteps(4),
	ShiftSouthwestSteps(3),
	ShiftSouthSteps(2),
	ShiftSoutheastSteps(3),
	Walk1StepSouth(),
	ShiftSouthwestSteps(3),
	Walk1StepWest(),
	ShiftNorthwestSteps(2),
	Walk1StepNorth(),
	ShiftNorthwestSteps(3),
	ShiftSouthwestSteps(2),
	SetBit(TEMP_7043_0),
	Walk1StepSouthwest(),
	Return()
])
