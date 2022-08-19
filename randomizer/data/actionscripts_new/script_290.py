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
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_290_set_animation_speed_0"),
	SetSequenceSpeed(speed=FAST),
	SetPriority(3),
	ShiftSouthwestSteps(2),
	JmpIfRandom2of3(['ACTION_290_set_priority_6', 'ACTION_290_set_priority_6']),
	JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
	SetPriority(2, identifier="ACTION_290_set_priority_6"),
	ShiftSoutheastSteps(2),
	JmpIfRandom2of3(['ACTION_290_set_priority_10', 'ACTION_290_set_priority_10']),
	JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
	SetPriority(2, identifier="ACTION_290_set_priority_10"),
	ShiftNortheastSteps(2),
	JmpIfRandom2of3(['ACTION_290_set_priority_14', 'ACTION_290_set_priority_14']),
	JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
	SetPriority(3, identifier="ACTION_290_set_priority_14"),
	ShiftNorthwestSteps(2),
	JmpIfRandom2of3(['ACTION_290_set_animation_speed_0', 'ACTION_290_set_animation_speed_0']),
	JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
	Jmp(["ACTION_290_set_animation_speed_0"])
])
