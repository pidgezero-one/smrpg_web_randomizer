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
	SequenceLoopingOn(),
	SetPriority(3),
	SetWalkingSpeed(speed=SLOW),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_2_DIRECTION, ["ACTION_643_shift_southeast_steps_24"]),
	Pause(173),
	StartLoopNTimes(4),
	ShiftSoutheastSteps(2),
	ShiftNorthwestSteps(2),
	EndLoop(),
	StartLoopNTimes(3),
	TurnClockwise45DegreesNTimes(6),
	Pause(3),
	EndLoop(),
	ShiftSoutheastSteps(6),
	JumpToHeight(120),
	SetAllSpeeds(speed=FAST),
	FixedFCoordOn(),
	SetSpriteSequence(index=2, is_sequence=True, mirror_sprite=True),
	ShiftNortheastSteps(2),
	Pause(7),
	FloatingOff(),
	SetSpriteSequence(index=3, is_sequence=True, mirror_sprite=True),
	SetBit(TEMP_7043_3),
	Return(),
	ShiftSoutheastSteps(2, identifier="ACTION_643_shift_southeast_steps_24"),
	ShiftNorthwestSteps(2),
	Jmp(["ACTION_643_shift_southeast_steps_24"])
])
