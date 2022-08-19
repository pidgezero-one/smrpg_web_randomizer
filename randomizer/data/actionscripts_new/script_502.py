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
	BPL262728(),
	SetWalkingSpeed(speed=NORMAL),
	StartLoopNTimes(2),
	JumpToHeight(height=64, silent=True),
	ShiftNortheastPixels(2),
	Pause(1, identifier="ACTION_502_pause_5"),
	JmpIfMarioInAir(["ACTION_502_pause_5"]),
	Pause(4),
	EndLoop(),
	SetBit(TEMP_7043_2),
	Jmp(["ACTION_500_db_0"])
])
