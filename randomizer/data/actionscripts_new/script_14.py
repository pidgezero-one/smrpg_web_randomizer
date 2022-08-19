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
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(7),
	EndLoop(),
	Pause(2, identifier="ACTION_14_pause_5"),
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
	Jmp(["ACTION_14_pause_5"])
])
