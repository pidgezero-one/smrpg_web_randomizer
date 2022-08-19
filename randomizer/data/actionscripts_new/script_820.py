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
	PlaySound(sound=S010_TRAMPOLINE, channel=4),
	JmpIfBitSet(SPINNING_FLOWER_2, ["ACTION_820_set_animation_speed_3"]),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetWalkingSpeed(speed=FASTER, identifier="ACTION_820_set_animation_speed_3"),
	JumpToHeight(height=136, silent=True),
	ShiftFDirectionPixels(3, identifier="ACTION_820_shift_f_direction_pixels_5"),
	JmpIfMarioInAir(["ACTION_820_shift_f_direction_pixels_5"]),
	SetWalkingSpeed(speed=NORMAL),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Return()
])
