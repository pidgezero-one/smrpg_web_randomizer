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
	ObjectMemorySetBit(arg_1=0x0B, bits=[3], identifier="ACTION_49_object_memory_set_bit_0"),
	ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True, bit_7=True),
	Pause(13),
	Inc(TEMP_702C),
	Walk1StepSouthwest(),
	Walk1StepSoutheast(),
	ShiftSouthwestSteps(3),
	ShiftNorthwestSteps(3),
	JmpIfRandom1of2(["ACTION_49_shift_southeast_steps_13"]),
	ShiftNortheastSteps(3),
	ShiftSoutheastSteps(2),
	Walk1StepNortheast(),
	Jmp(["ACTION_49_object_memory_set_bit_0"]),
	ShiftSoutheastSteps(2, identifier="ACTION_49_shift_southeast_steps_13"),
	ShiftNortheastSteps(4),
	Jmp(["ACTION_49_object_memory_set_bit_0"])
])
