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
	SetPriority(3, identifier="ACTION_131_set_priority_0"),
	SetSequenceSpeed(speed=FAST),
	ShiftSoutheastSteps(5),
	Pause(1, identifier="ACTION_131_pause_3"),
	JmpIfBitSet(TEMP_7044_4, ["ACTION_131_shift_northwest_steps_6"]),
	Jmp(["ACTION_131_pause_3"]),
	ShiftNorthwestSteps(5, identifier="ACTION_131_shift_northwest_steps_6"),
	Pause(1, identifier="ACTION_131_pause_7"),
	JmpIfBitSet(TEMP_7044_3, ["ACTION_131_set_priority_0"]),
	Jmp(["ACTION_131_pause_7"])
])
