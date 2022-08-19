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
	Pause(1, identifier="ACTION_823_pause_0"),
	Set700CToObjectCoord(object=MARIO, coord=Z, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_700C, 2176),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_823_pause_0"]),
	Set700CToObjectCoord(object=MARIO, coord=X, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_700C, 9216),
	JmpIfComparisonResultIsLesser(["ACTION_823_object_memory_modify_bits_13"]),
	Set700CToObjectCoord(object=MARIO, coord=Y, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_700C, 13056),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_823_object_memory_modify_bits_13"]),
	SetPriority(0),
	ShadowOff(),
	Jmp(["ACTION_823_pause_0"]),
	ObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6], identifier="ACTION_823_object_memory_modify_bits_13"),
	ShadowOn(),
	Jmp(["ACTION_823_pause_0"])
])
