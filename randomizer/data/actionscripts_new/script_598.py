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
	SetVarToConst(X_COORD_2, 768),
	SetVarToConst(Y_COORD_2, 2560),
	SetVarToConst(Z_COORD_2, 0),
	TransferTo70167018701A(),
	SetAllSpeeds(speed=NORMAL),
	VisibilityOn(),
	ShiftNortheastSteps(3),
	Walk1StepEast(),
	ShiftSoutheastSteps(4),
	ShiftSouthSteps(2),
	Walk1StepSoutheast(),
	Walk1StepEast(),
	ShiftNortheastSteps(5),
	Walk1StepEast(),
	ShiftSoutheastSteps(3),
	SetBit(TEMP_7043_1),
	Walk1StepSoutheast(),
	ShiftSouthSteps(2),
	ShiftSouthwestSteps(3),
	ShiftSouthwestSteps(2),
	SetBit(TEMP_7043_0),
	Walk1StepSouthwest(),
	Return()
])
