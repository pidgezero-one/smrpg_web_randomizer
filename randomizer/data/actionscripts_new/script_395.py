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
	SetAllSpeeds(speed=NORMAL),
	OverwriteSolidity(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SequencePlaybackOn(),
	ObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6]),
	SetVRAMPriority(NORMAL),
	FloatingOn(),
	FixedFCoordOff(),
	ShadowOn(),
	ResetProperties(),
	SequenceLoopingOff(),
	Return()
])
