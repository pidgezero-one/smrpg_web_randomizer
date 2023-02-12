#A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceNorthwest(),
	SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True),
	SetPriority(3),
	Db(bytearray(b' \x07')),
	Db(bytearray(b'$\x00\xfe\x00\xff')),
	Db(bytearray(b'%\x00\x0f\x80\xff')),
	Pause(46),
	BPL262728(),
	PlaySound(sound=SO058_INSERT, channel=4),
	OverwriteSolidity(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Return()
])
