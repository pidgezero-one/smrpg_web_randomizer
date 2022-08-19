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
	SetSequenceSpeed(speed=FAST),
	VisibilityOff(),
	Pause(30, identifier="ACTION_112_pause_2"),
	ClearBit(TEMP_7043_1),
	VisibilityOn(),
	ShiftSoutheastSteps(9),
	VisibilityOff(),
	Pause(150),
	SetBit(TEMP_7043_2),
	Pause(100),
	VisibilityOn(),
	ShiftNorthwestSteps(9),
	VisibilityOff(),
	ClearBit(TEMP_7043_2),
	Pause(1, identifier="ACTION_112_pause_14"),
	JmpIfBitSet(TEMP_7043_1, ["ACTION_112_pause_2"]),
	Jmp(["ACTION_112_pause_14"])
])
