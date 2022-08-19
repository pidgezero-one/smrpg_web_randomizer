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
	ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True, bit_7=True),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_50_pause_26"]),
	Pause(4, identifier="ACTION_50_pause_4"),
	Walk1StepNorthwest(),
	Pause(1),
	Walk1StepSouthwest(),
	Pause(1),
	ShiftSoutheastSteps(2),
	Pause(1),
	Walk1StepNortheast(),
	Pause(1),
	Inc(TEMP_702C),
	Walk1StepNorthwest(),
	Pause(1),
	ShiftSouthwestSteps(2),
	Pause(1),
	Walk1StepNorthwest(),
	Pause(1),
	ShiftNortheastSteps(3),
	Pause(1),
	Walk1StepSoutheast(),
	Pause(1),
	Walk1StepSouthwest(),
	Jmp(["ACTION_50_pause_4"]),
	Pause(3, identifier="ACTION_50_pause_26"),
	Walk1StepNorthwest(),
	Pause(1),
	ShiftNortheastSteps(2),
	Pause(2),
	Walk1StepSoutheast(),
	ShiftSouthwestSteps(3),
	Walk1StepSoutheast(),
	Walk1StepNortheast(),
	Walk1StepNorthwest(),
	JmpIfRandom1of2(["ACTION_50_pause_26"]),
	ShiftNortheastSteps(2),
	Walk1StepSoutheast(),
	Pause(3),
	ShiftNorthwestSteps(2),
	ShiftSouthwestSteps(3),
	Walk1StepSoutheast(),
	Walk1StepNortheast(),
	Jmp(["ACTION_50_pause_26"])
])
