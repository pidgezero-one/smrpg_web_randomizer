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
	ShadowOn(),
	SetPriority(3),
	SetSpriteSequence(index=6, is_sequence=True),
	ShiftEastPixels(8),
	FaceSouthwest(),
	StartLoopNTimes(2),
	Pause(15),
	SetWalkingSpeed(speed=FAST),
	SetBit(TEMP_7043_1),
	ShiftZUpPixels(10),
	ShiftZDownPixels(10),
	Pause(20),
	EndLoop(),
	Pause(30),
	SetBit(TEMP_7043_4),
	SetSpriteSequence(index=3, looping_off=True),
	Pause(60),
	SetAllSpeeds(speed=NORMAL),
	FixedFCoordOn(),
	ShiftWestSteps(4),
	SetAllSpeeds(speed=FAST),
	ShiftNorthwestSteps(6),
	ShiftNorthSteps(2),
	SetBit(TEMP_7043_4),
	SetSpriteSequence(index=3, looping_off=True),
	Return()
])
