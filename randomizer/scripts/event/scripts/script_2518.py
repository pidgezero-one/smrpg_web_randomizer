# E2518_STAR_HILL_2ND_ROOM_CENTRAL_LEFT_FLOWER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_3, ["EVENT_2518_ret_12"]),
	SetBit(TEMP_7043_3),
	PlaySound(sound=SO081_STAR, channel=6),
	Store01To0248(),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R157_STAR_HILL_AREA_03, mod_id=5),
	Pause(1),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R157_STAR_HILL_AREA_03, mod_id=6),
	Inc(TEMP_70AE),
	JmpIfVarEqualsConst(TEMP_70AE, 6, ["EVENT_2522_pause_0"]),
	Store00To0248(),
	Return(identifier="EVENT_2518_ret_12")
])
