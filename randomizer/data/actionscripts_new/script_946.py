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
	SetSpriteSequence(index=5, is_sequence=True, mirror_sprite=True, identifier="ACTION_946_set_sprite_sequence_0"),
	Pause(128, identifier="ACTION_946_pause_1"),
	JmpIfRandom1of2(["ACTION_946_start_loop_n_times_9"]),
	StartLoopNTimes(2),
	ShiftNortheastPixels(1),
	ShiftSouthwestPixels(1),
	EndLoop(),
	Pause(128),
	Jmp(["ACTION_946_set_sprite_sequence_0"]),
	StartLoopNTimes(2, identifier="ACTION_946_start_loop_n_times_9"),
	ShiftSoutheastPixels(1),
	ShiftNorthwestPixels(1),
	EndLoop(),
	Pause(128),
	Jmp(["ACTION_946_pause_1"])
])
