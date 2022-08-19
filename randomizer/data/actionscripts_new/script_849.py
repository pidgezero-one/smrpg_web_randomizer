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
	Pause(2, identifier="ACTION_849_pause_0"),
	ShiftZDownPixels(1),
	Pause(4),
	ShiftZDownPixels(1),
	Pause(13),
	ShiftZUpPixels(1),
	Pause(4),
	ShiftZUpPixels(1),
	Pause(2),
	ShiftZUpPixels(1),
	Pause(4),
	ShiftZUpPixels(1),
	Pause(13),
	ShiftZDownPixels(1),
	Pause(4),
	ShiftZDownPixels(1),
	JmpIfBitSet(TEMP_708C_4, ["ACTION_849_ret_18"]),
	Jmp(["ACTION_849_pause_0"]),
	Return(identifier="ACTION_849_ret_18")
])
