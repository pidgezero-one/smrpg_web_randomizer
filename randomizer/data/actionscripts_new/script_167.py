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
	SetVRAMPriority(PRIORITY_3),
	SetPriority(3),
	FloatingOff(),
	Db(bytearray(b'\xc8\x00')),
	AddConstToVar(X_COORD_2, 62848),
	AddConstToVar(Y_COORD_2, 1280),
	SetVarToConst(Z_COORD_2, 144),
	TransferTo70167018701A(),
	SetWalkingSpeed(speed=FAST),
	ShiftNortheastSteps(4),
	VisibilityOn(),
	SequenceLoopingOn(),
	SetSpriteSequence(index=0, is_sequence=True),
	Pause(15),
	VisibilityOff(),
	Return()
])
