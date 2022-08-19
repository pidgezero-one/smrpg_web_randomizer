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
	StartLoopNTimes(2),
	Pause(1, identifier="ACTION_40_pause_1"),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_40_pause_1"]),
	SetVarToConst(X_COORD_2, 15104),
	SetVarToConst(Y_COORD_2, 3712),
	SetVarToConst(Z_COORD_2, 0),
	TransferTo70167018701A(),
	VisibilityOn(),
	SequenceLoopingOn(),
	SetSpriteSequence(index=0, is_sequence=True),
	Pause(15),
	VisibilityOff(),
	EndLoop(),
	Return()
])
