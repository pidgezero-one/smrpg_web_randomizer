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
	Pause(10, identifier="ACTION_302_pause_0"),
	SetSolidityBits(cant_walk_through=True),
	SetSolidityBits(bit_4=True),
	SetSpriteSequence(index=2, looping_off=True, is_sequence=True),
	PlaySound(sound=S089_LIT_FUSE, channel=4),
	Pause(16),
	StopSound(),
	SetBit(TEMP_7043_0),
	Pause(1),
	ClearBit(TEMP_7043_0),
	Pause(3),
	VisibilityOff(),
	ClearBit(TEMP_7043_1),
	Pause(12),
	ClearSolidityBits(cant_walk_through=True),
	ClearSolidityBits(bit_4=True),
	TransferToXYZF(x=4, y=55, z=0, direction=EAST),
	Return()
])
