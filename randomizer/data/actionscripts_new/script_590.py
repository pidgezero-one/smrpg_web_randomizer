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
	FixedFCoordOn(),
	ShiftSouthPixels(1, identifier="ACTION_590_shift_south_pixels_1"),
	ShiftNorthPixels(1),
	ShiftSouthPixels(1),
	ShiftNorthPixels(1),
	Pause(40),
	JmpIfRandom2of3(['ACTION_590_pause_9', 'ACTION_590_pause_11']),
	Pause(50),
	Jmp(["ACTION_590_shift_south_pixels_1"]),
	Pause(120, identifier="ACTION_590_pause_9"),
	Jmp(["ACTION_590_shift_south_pixels_1"]),
	Pause(100, identifier="ACTION_590_pause_11"),
	ShiftSouthPixels(1),
	ShiftNorthPixels(1),
	Pause(90),
	JmpIfRandom1of2(["ACTION_590_pause_9"]),
	Jmp(["ACTION_590_shift_south_pixels_1"])
])
