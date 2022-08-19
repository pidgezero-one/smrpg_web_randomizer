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
	ShiftNorthwestSteps(2),
	FixedFCoordOn(),
	JmpIfRandom2of3(['ACTION_717_pause_6', 'ACTION_717_pause_9'], identifier="ACTION_717_jmp_if_random_above_66_3"),
	Pause(30),
	Jmp(["ACTION_717_jmp_if_random_above_66_3"]),
	Pause(30, identifier="ACTION_717_pause_6"),
	ShiftNortheastSteps(2),
	Jmp(["ACTION_717_jmp_if_random_above_128_12"]),
	Pause(30, identifier="ACTION_717_pause_9"),
	ShiftSouthwestSteps(2),
	Jmp(["ACTION_717_jmp_if_random_above_128_17"]),
	JmpIfRandom1of2(["ACTION_717_pause_14"], identifier="ACTION_717_jmp_if_random_above_128_12"),
	Pause(30),
	Pause(30, identifier="ACTION_717_pause_14"),
	ShiftSouthwestSteps(2),
	Jmp(["ACTION_717_jmp_if_random_above_66_3"]),
	JmpIfRandom1of2(["ACTION_717_pause_19"], identifier="ACTION_717_jmp_if_random_above_128_17"),
	Pause(30),
	Pause(30, identifier="ACTION_717_pause_19"),
	ShiftNortheastSteps(2),
	Jmp(["ACTION_717_jmp_if_random_above_66_3"])
])
