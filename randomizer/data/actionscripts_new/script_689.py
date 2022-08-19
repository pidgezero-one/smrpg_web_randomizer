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
	Pause(64),
	ClearSolidityBits(cant_walk_through=True),
	SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	ShiftNorthwestPixels(5),
	SetSpriteSequence(index=1, is_sequence=True, mirror_sprite=True),
	VisibilityOn(),
	Db(bytearray(b' \x07')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00 \xf0\x03\x00\x01\x00\x00\x00\x04\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00 \xf0\x03\x00\x01\x00\x00\x00\x04\x80")),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00 \xf0\x03\x00\x01\x00\x00\x00\x08\x80')),
	ShiftZDownSteps(10),
	SetSolidityBits(cant_walk_through=True),
	Return()
])
