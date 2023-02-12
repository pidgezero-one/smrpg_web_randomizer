# E2519_STAR_HILL_2ND_ROOM_CENTRAL_RIGHT_FLOWER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_4, ["EVENT_2519_ret_12"]),
	SetBit(TEMP_7043_4),
	PlaySound(sound=SO081_STAR, channel=6),
	Store01To0248(),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R157_STAR_HILL_AREA_03, mod_id=7),
	Pause(1),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R157_STAR_HILL_AREA_03, mod_id=8),
	Inc(TEMP_70AE),
	JmpIfVarEqualsConst(TEMP_70AE, 6, ["EVENT_2522_pause_0"]),
	Store00To0248(),
	Return(identifier="EVENT_2519_ret_12")
])
