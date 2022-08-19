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
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=128, tiles=3, destinations=["ACTION_403_face_mario_9"], identifier="ACTION_403_db_0"),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=5, destinations=["ACTION_403_face_mario_9"], identifier="ACTION_403_db_1"),
	JmpIfRandom1of2(["ACTION_403_set_var_to_random_5"]),
	TurnRandomDirection(),
	Pause(8),
	SetVarToRandom(PRIMARY_TEMP_700C, 2, identifier="ACTION_403_set_var_to_random_5"),
	Inc(PRIMARY_TEMP_700C),
	ShiftZ20Steps(),
	Jmp(["ACTION_403_db_0"]),
	FaceMario(identifier="ACTION_403_face_mario_9"),
	Pause(8),
	SetVarToRandom(PRIMARY_TEMP_700C, 2),
	Inc(PRIMARY_TEMP_700C),
	ShiftZ20Steps(),
	Jmp(["ACTION_403_db_1"])
])
