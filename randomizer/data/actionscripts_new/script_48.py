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
	ObjectMemorySetBit(arg_1=0x0B, bits=[3], identifier="ACTION_48_object_memory_set_bit_0"),
	SetAllSpeeds(speed=FAST),
	ShiftNortheastSteps(3),
	Pause(8),
	FaceNorthwest(),
	Pause(8),
	FaceSoutheast(),
	Pause(8),
	JmpIfRandom1of2(["ACTION_48_shift_southwest_steps_27"]),
	JumpToHeight(height=108, silent=True),
	ShiftNortheastSteps(3),
	Pause(8),
	ShiftNortheastSteps(4),
	ShiftSoutheastSteps(2),
	ShiftSouthwestSteps(2),
	Pause(8),
	Walk1StepNorthwest(),
	ShiftSouthwestSteps(4),
	Pause(8),
	JumpToHeight(height=108, silent=True),
	Pause(8),
	ShiftSouthwestSteps(4),
	JumpToHeight(height=108, silent=True),
	Pause(12),
	Walk1StepNorthwest(),
	Pause(8),
	Jmp(["ACTION_48_object_memory_set_bit_0"]),
	ShiftSouthwestSteps(5, identifier="ACTION_48_shift_southwest_steps_27"),
	Walk1StepSoutheast(),
	Pause(8),
	FaceSouthwest(),
	JumpToHeight(height=108, silent=True),
	Pause(12),
	Walk1StepSouthwest(),
	Pause(8),
	ShiftSouthwestSteps(5),
	FaceNorthwest(),
	JumpToHeight(height=108, silent=True),
	Pause(16),
	JmpIfRandom1of2(["ACTION_48_pause_52"]),
	ShiftNortheastSteps(3),
	FaceNorthwest(),
	JumpToHeight(height=72, silent=True),
	Pause(8),
	Walk1StepNorthwest(),
	ShiftNortheastSteps(4),
	Pause(8),
	JumpToHeight(height=72, silent=True),
	Pause(8),
	Walk1StepNortheast(),
	Pause(8),
	Jmp(["ACTION_48_object_memory_set_bit_0"]),
	Pause(8, identifier="ACTION_48_pause_52"),
	JumpToHeight(height=108, silent=True),
	Pause(16),
	Walk1StepSoutheast(),
	Walk1StepSouthwest(),
	Walk1StepNorthwest(),
	ShiftNortheastSteps(2),
	ShiftNorthwestSteps(2),
	FaceNortheast(),
	JumpToHeight(height=72, silent=True),
	Pause(8),
	Walk1StepNortheast(),
	Pause(4),
	Walk1StepSoutheast(),
	ShiftNortheastSteps(4),
	Pause(8),
	JumpToHeight(height=88, silent=True),
	ShiftNortheastSteps(2),
	Pause(8),
	Jmp(["ACTION_48_object_memory_set_bit_0"])
])
