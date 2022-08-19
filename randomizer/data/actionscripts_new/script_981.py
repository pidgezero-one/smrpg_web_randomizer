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
	ShadowOff(),
	SetPriority(3),
	SetWalkingSpeed(speed=SLOW),
	TransferXYZFPixels(x=251, y=254, z=0, direction=EAST),
	JmpIfRandom1of2(["ACTION_979_set_sprite_sequence_4"]),
	Jmp(["ACTION_980_pause_4"])
])
