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
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 117, ["ACTION_890_pause_23"]),
	Pause(1, identifier="ACTION_890_pause_2"),
	JmpIfBitSet(TEMP_7043_2, ["ACTION_890_pause_5"]),
	Jmp(["ACTION_890_pause_2"]),
	Pause(90, identifier="ACTION_890_pause_5"),
	FaceSouthwest(),
	SetSpriteSequence(index=5, is_sequence=True),
	JmpIfRandom1of2(["ACTION_890_set_animation_speed_11"], identifier="ACTION_890_jmp_if_random_above_128_8"),
	SetWalkingSpeed(speed=NORMAL),
	Jmp(["ACTION_890_walk_1_step_south_12"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_890_set_animation_speed_11"),
	Walk1StepSouth(identifier="ACTION_890_walk_1_step_south_12"),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSouthwestPixels(8),
	JmpIfRandom1of2(["ACTION_890_set_animation_speed_18"]),
	SetWalkingSpeed(speed=NORMAL),
	Jmp(["ACTION_890_walk_1_step_west_19"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_890_set_animation_speed_18"),
	Walk1StepWest(identifier="ACTION_890_walk_1_step_west_19"),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSouthwestPixels(8),
	Jmp(["ACTION_890_jmp_if_random_above_128_8"]),
	Pause(1, identifier="ACTION_890_pause_23"),
	JmpIfBitSet(TEMP_7043_2, ["ACTION_890_pause_26"]),
	Jmp(["ACTION_890_pause_23"]),
	Pause(90, identifier="ACTION_890_pause_26"),
	FaceSouthwest(),
	SetSpriteSequence(index=5, is_sequence=True),
	JmpIfRandom1of2(["ACTION_890_set_animation_speed_32"], identifier="ACTION_890_jmp_if_random_above_128_29"),
	SetWalkingSpeed(speed=NORMAL),
	Jmp(["ACTION_890_walk_1_step_south_33"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_890_set_animation_speed_32"),
	Walk1StepSouth(identifier="ACTION_890_walk_1_step_south_33"),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSouthwestPixels(8),
	JmpIfRandom1of2(["ACTION_890_set_animation_speed_39"]),
	SetWalkingSpeed(speed=NORMAL),
	Jmp(["ACTION_890_walk_1_step_west_40"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_890_set_animation_speed_39"),
	Walk1StepWest(identifier="ACTION_890_walk_1_step_west_40"),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSouthwestPixels(8),
	Jmp(["ACTION_890_jmp_if_random_above_128_29"])
])
