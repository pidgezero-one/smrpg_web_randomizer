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
	SetSequenceSpeed(speed=NORMAL),
	SequenceLoopingOn(),
	JmpIfRandom2of3(['ACTION_404_jmp_if_random_above_128_10', 'ACTION_404_jmp_if_random_above_128_10'], identifier="ACTION_404_jmp_if_random_above_66_2"),
	FaceMario(identifier="ACTION_404_face_mario_3"),
	SetWalkingSpeed(speed=NORMAL),
	Pause(8),
	SetVarToRandom(PRIMARY_TEMP_700C, 2),
	Inc(PRIMARY_TEMP_700C),
	ShiftZ20Steps(),
	Jmp(["ACTION_404_jmp_if_random_above_66_2"]),
	JmpIfRandom1of2(["ACTION_404_set_animation_speed_13"], identifier="ACTION_404_jmp_if_random_above_128_10"),
	TurnRandomDirection(),
	Pause(8),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_404_set_animation_speed_13"),
	SetVarToRandom(PRIMARY_TEMP_700C, 2),
	Inc(PRIMARY_TEMP_700C),
	ShiftZ20Steps(),
	Jmp(["ACTION_404_jmp_if_random_above_66_2"])
])
