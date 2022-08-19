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
	ClearBit(DIRECTIONAL_7047_0),
	Pause(32),
	OverwriteSolidity(),
	SetPriority(3),
	ShadowOff(),
	FaceSouth(),
	JmpIfBitSet(UNKNOWN_7047_4, ["ACTION_482_clear_bit_18"]),
	SetSpriteSequence(index=0, sprite_offset=1, is_mold=True, is_sequence=True),
	VisibilityOn(),
	Db(bytearray(b' \x07')),
	Db(bytearray(b'$\x00\x00\xb0\x00')),
	Db(bytearray(b'%\x80\t\x80\xff')),
	Pause(16),
	ShadowOn(),
	Pause(24),
	BPL262728(),
	Db(bytearray(b'\xfd\x9c:')),
	Return(),
	ClearBit(UNKNOWN_7047_4, identifier="ACTION_482_clear_bit_18"),
	FaceSouthwest(),
	SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True),
	VisibilityOn(),
	Db(bytearray(b' \x07')),
	Db(bytearray(b'$\x00\x00\xb0\x00')),
	Db(bytearray(b'%\x80\t\x80\xff')),
	Pause(16),
	ShadowOn(),
	Pause(24),
	PlaySound(sound=S022_CLOSE_DOOR, channel=4),
	Db(bytearray(b'$\x00\x00\x00\x00')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	PlaySound(sound=S022_CLOSE_DOOR, channel=4),
	Pause(30),
	PlaySound(sound=S022_CLOSE_DOOR, channel=4),
	Db(bytearray(b'%\x80\x04\x80\xff')),
	Pause(20),
	PlaySound(sound=S022_CLOSE_DOOR, channel=4),
	Db(bytearray(b'%@\x02\x80\xff')),
	Pause(10),
	PlaySound(sound=S022_CLOSE_DOOR, channel=4),
	BPL262728(),
	Pause(16),
	Jmp(["ACTION_384_sequence_looping_on_0"])
])
