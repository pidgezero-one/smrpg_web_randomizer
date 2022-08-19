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
	SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
	SetSolidityBits(bit_4=True),
	SetWalkingSpeed(speed=VERY_SLOW),
	SetSequenceSpeed(speed=FAST),
	ShiftNorthwestPixels(8),
	FaceSouthwest(),
	Pause(20, identifier="ACTION_138_pause_6"),
	Walk1StepSoutheast(),
	FaceSouthwest(),
	Pause(20),
	Walk1StepNorthwest(),
	FaceSouthwest(),
	Jmp(["ACTION_138_pause_6"])
])
