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
	SetSpriteSequence(index=5, is_mold=True, is_sequence=True, mirror_sprite=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
	Pause(1, identifier="ACTION_428_pause_2"),
	JmpIfBitSet(TEMP_7043_2, ["ACTION_431_set_animation_speed_0"]),
	Jmp(["ACTION_428_pause_2"])
])
