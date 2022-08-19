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
	ClearBit(TEMP_7044_3),
	SetSequenceSpeed(speed=FAST),
	SetSpriteSequence(index=10, is_sequence=True),
	Pause(10),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True, identifier="ACTION_571_set_sprite_sequence_4"),
	FixedFCoordOn(),
	SequenceLoopingOn(),
	SetWalkingSpeed(speed=SLOW),
	ShiftWestPixels(1),
	Pause(1),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftNorthwestPixels(1),
	Pause(1),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSoutheastPixels(1),
	Pause(1),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftEastPixels(1),
	Pause(1),
	SetWalkingSpeed(speed=SLOW),
	ShiftEastPixels(1),
	Pause(1),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftNortheastPixels(1),
	Pause(1),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSouthwestPixels(1),
	Pause(1),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftWestPixels(1),
	Pause(1),
	Jmp(["ACTION_571_set_sprite_sequence_4"]),
	Return()
])
