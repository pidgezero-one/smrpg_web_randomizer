# E2503_STAR_HILL_3RD_ROOM_TOP_LEFT_FLOWER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_1, ["EVENT_2503_ret_12"]),
	SetBit(TEMP_7043_1),
	PlaySound(sound=SO081_STAR, channel=6),
	Store01To0248(),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R159_STAR_HILL_AREA_04, mod_id=1),
	Pause(1),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R159_STAR_HILL_AREA_04, mod_id=2),
	Inc(TEMP_70AE),
	JmpIfVarEqualsConst(TEMP_70AE, 6, ["EVENT_2509_pause_0"]),
	Store00To0248(),
	Return(identifier="EVENT_2503_ret_12")
])
