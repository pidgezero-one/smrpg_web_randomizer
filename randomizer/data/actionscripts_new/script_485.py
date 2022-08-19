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
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, mirror_sprite=True),
	ShiftToXYCoords(x=3, y=74),
	SetWalkingSpeed(speed=FASTEST),
	ShiftSoutheastPixels(4),
	ShiftNorthPixels(8),
	SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, identifier="ACTION_485_set_sprite_sequence_6"),
	Pause(10),
	SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(10),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_485_pause_12"]),
	Jmp(["ACTION_485_set_sprite_sequence_6"]),
	Pause(3, identifier="ACTION_485_pause_12"),
	ShiftSoutheastPixels(4),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\x00\x0f\x80\xff')),
	Pause(48),
	BPL262728(),
	Return()
])
