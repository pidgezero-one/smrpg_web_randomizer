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
	ObjectMemorySetBit(arg_1=0x0B, bits=[3], identifier="ACTION_61_object_memory_set_bit_0"),
	SetPriority(2),
	Set700CToPressedButton(),
	Mem700CAndConst(0x0003),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_61_pause_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_61_pause_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_61_pause_10"]),
	Pause(3),
	Pause(3, identifier="ACTION_61_pause_8"),
	Pause(3, identifier="ACTION_61_pause_9"),
	Pause(3, identifier="ACTION_61_pause_10"),
	ShiftFDirectionSteps(2),
	Pause(5),
	TurnClockwise45DegreesNTimes(4),
	JmpIfRandom1of2(["ACTION_61_object_memory_set_bit_0"]),
	Pause(8),
	TurnClockwise45DegreesNTimes(4),
	Jmp(["ACTION_61_object_memory_set_bit_0"])
])
