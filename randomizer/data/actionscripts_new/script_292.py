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
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=FAST),
	SetPriority(2),
	ShiftSouthwestSteps(2),
	JmpIfRandom2of3(['ACTION_291_set_animation_speed_0', 'ACTION_291_set_animation_speed_0']),
	JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
	Jmp(["ACTION_291_set_animation_speed_0"])
])
