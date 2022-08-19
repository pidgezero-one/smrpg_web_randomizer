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
	SetSequenceSpeed(speed=SLOW),
	SequenceLoopingOn(),
	JmpIfRandom1of2(["ACTION_402_set_var_to_random_5"], identifier="ACTION_402_jmp_if_random_above_128_2"),
	TurnRandomDirection(),
	Pause(8),
	SetVarToRandom(PRIMARY_TEMP_700C, 2, identifier="ACTION_402_set_var_to_random_5"),
	Inc(PRIMARY_TEMP_700C),
	ShiftZ20Steps(),
	Jmp(["ACTION_402_jmp_if_random_above_128_2"])
])
