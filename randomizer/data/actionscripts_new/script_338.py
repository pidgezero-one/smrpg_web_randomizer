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
	FloatingOff(),
	VisibilityOff(),
	Pause(6),
	PlaySound(sound=S087_CORRECT_SIGNAL, channel=6),
	SetSpriteSequence(index=1, looping_off=True, is_sequence=True),
	IncPaletteRowBy(2),
	VisibilityOn(),
	FloatingOn(),
	JumpToHeight(height=0, silent=True),
	SetSolidityBits(cant_pass_walls=True, cant_jump_through=True, bit_4=True, cant_walk_through=True),
	SetVRAMPriority(NORMAL),
	Pause(1),
	Return()
])
