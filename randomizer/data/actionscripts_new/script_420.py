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
	JmpToSubroutine(["ACTION_420_set_sprite_sequence_2"]),
	Jmp(["ACTION_416_transfer_to_xyzf_47"]),
	SetSpriteSequence(index=1, is_mold=True, identifier="ACTION_420_set_sprite_sequence_2"),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	ShiftZDownPixels(4),
	VisibilityOff(),
	ResetProperties(),
	Return()
])
