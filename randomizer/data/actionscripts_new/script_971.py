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
	SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	SetPriority(1),
	VisibilityOn(),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True),
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
	ShiftNorthPixels(5),
	SetWalkingSpeed(speed=SLOW),
	WalkToXYCoords(x=5, y=6),
	ShiftToXYCoords(x=5, y=8),
	SetWalkingSpeed(speed=FASTEST),
	ShiftSouthPixels(15),
	ShiftSouthwestPixels(20),
	SetWalkingSpeed(speed=SLOW),
	SetSpriteSequence(index=0, is_sequence=True),
	ShiftSouthwestSteps(3),
	ShiftSouthwestPixels(8),
	Pause(8),
	Db(bytearray(b' \x05')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00@\x80\x01\x00\x01\x00\x00\x00\x04\x80')),
	Pause(511),
	Return()
])
