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
	SetSolidityBits(cant_pass_walls=True, identifier="ACTION_882_set_solidity_bits_0"),
	SetSolidityBits(cant_pass_npcs=True, bit_7=True),
	SetWalkingSpeed(speed=FAST, identifier="ACTION_882_set_animation_speed_2"),
	SetSequenceSpeed(speed=VERY_FAST),
	StartLoopNTimes(1),
	FaceMario(),
	ShiftFDirectionSteps(1),
	JmpIfRandom1of2(["ACTION_882_set_animation_speed_9"]),
	Pause(30),
	SetWalkingSpeed(speed=NORMAL, identifier="ACTION_882_set_animation_speed_9"),
	SetSequenceSpeed(speed=NORMAL),
	EndLoop(),
	Jmp(["ACTION_882_set_animation_speed_2"])
])
