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
	SetWalkingSpeed(speed=FASTEST),
	Walk1StepNorthwest(),
	Walk1StepNortheast(),
	StartLoopNTimes(5),
	SetSpriteSequence(index=4, sprite_offset=2, looping_off=True),
	Pause(46),
	EndLoop(),
	SetSpriteSequence(index=13, sprite_offset=2, is_mold=True, is_sequence=True),
	Pause(32),
	SetSpriteSequence(index=18, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(56),
	ResetProperties(),
	SetWalkingSpeed(speed=FAST),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftSouthwestSteps(2),
	ShiftSouthwestPixels(8),
	Walk1StepNorthwest(),
	Pause(64),
	SetSequenceSpeed(speed=NORMAL),
	SetSpriteSequence(index=5, is_sequence=True),
	Return()
])
