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
	JmpIfVarEqualsConst(CURRENT_OVERWORLD_MARKER_ID, 50, ["ACTION_727_set_animation_speed_11"], identifier="ACTION_727_jmp_if_var_equals_const_0"),
	Pause(40, identifier="ACTION_727_pause_1"),
	JmpIfRandom1of2(["ACTION_727_pause_1"]),
	SetSequenceSpeed(speed=VERY_FAST),
	SetWalkingSpeed(speed=SLOW),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_727_pause_1"]),
	Walk1StepFDirection(),
	FaceMario(),
	Walk1StepFDirection(),
	FaceMario(),
	Jmp(["ACTION_727_pause_1"]),
	SetSequenceSpeed(speed=FASTEST, identifier="ACTION_727_set_animation_speed_11"),
	SetWalkingSpeed(speed=NORMAL),
	Walk1StepFDirection(),
	JumpToHeight(height=0, silent=True),
	FaceMario(),
	JmpIfRandom2of3(['ACTION_727_turn_clockwise_45_degrees_n_times_18', 'ACTION_727_turn_clockwise_45_degrees_n_times_20']),
	Jmp(["ACTION_727_pause_1"]),
	TurnClockwise45DegreesNTimes(1, identifier="ACTION_727_turn_clockwise_45_degrees_n_times_18"),
	Jmp(["ACTION_727_pause_1"]),
	TurnClockwise45DegreesNTimes(7, identifier="ACTION_727_turn_clockwise_45_degrees_n_times_20"),
	Jmp(["ACTION_727_pause_1"])
])
