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
	JmpIfRandom2of3(['ACTION_115_jmp_to_subroutine_4', 'ACTION_115_jmp_to_subroutine_7'], identifier="ACTION_115_jmp_if_random_above_66_0"),
	JmpToSubroutine(["ACTION_106_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	Jmp(["ACTION_115_jmp_if_random_above_66_0"]),
	JmpToSubroutine(["ACTION_107_set_animation_speed_0"], identifier="ACTION_115_jmp_to_subroutine_4"),
	JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	Jmp(["ACTION_115_jmp_if_random_above_66_0"]),
	JmpToSubroutine(["ACTION_104_set_animation_speed_0"], identifier="ACTION_115_jmp_to_subroutine_7"),
	JmpToSubroutine(["ACTION_106_set_animation_speed_0"]),
	Jmp(["ACTION_115_jmp_if_random_above_66_0"])
])
