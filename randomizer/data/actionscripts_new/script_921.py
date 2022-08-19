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
	FloatingOn(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	SetSpriteSequence(index=1, is_sequence=True),
	JumpToHeight(height=0, silent=True),
	Pause(1, identifier="ACTION_921_pause_5"),
	Jmp(["ACTION_921_pause_5"])
])
