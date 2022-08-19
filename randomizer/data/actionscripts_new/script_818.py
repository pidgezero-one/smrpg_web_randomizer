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
	VisibilityOn(),
	SetAllSpeeds(speed=FAST),
	PlaySound(sound=S030_SURPRISED_MONSTER, channel=4),
	JumpToHeight(128),
	Walk1StepFDirection(),
	SetSolidityBits(cant_pass_walls=True),
	Pause(1, identifier="ACTION_818_pause_6"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_818_pause_6"]),
	Set700CToPressedButton(),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_818_set_solidity_bits_11"]),
	SetBit(TEMP_7044_7),
	SetSolidityBits(cant_walk_under=True, identifier="ACTION_818_set_solidity_bits_11"),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetPriority(3),
	JmpIfRandom1of2(["ACTION_818_set_animation_speed_19"], identifier="ACTION_818_jmp_if_random_above_128_14"),
	SetWalkingSpeed(speed=NORMAL, identifier="ACTION_818_set_animation_speed_15"),
	FaceMario(),
	Walk1StepFDirection(),
	Jmp(["ACTION_818_jmp_if_random_above_128_14"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_818_set_animation_speed_19"),
	TurnRandomDirection(),
	Walk1StepFDirection(),
	Jmp(["ACTION_818_set_animation_speed_15"])
])
