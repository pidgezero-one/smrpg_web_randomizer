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
	SetPriority(3, identifier="ACTION_130_set_priority_0"),
	JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	ClearBit(TEMP_7044_3),
	SetBit(TEMP_7044_4),
	JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	ClearBit(TEMP_7044_4),
	SetBit(TEMP_7044_3),
	Jmp(["ACTION_130_set_priority_0"])
])
