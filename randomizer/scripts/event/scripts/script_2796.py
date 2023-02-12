# E2796_STAR_HILL_MARRYMORE_EXIT_FLOWER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2796_ret_13"]),
	SetBit(TEMP_7043_0),
	PlaySound(sound=SO081_STAR, channel=6),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R145_STAR_HILL_AREA_01, mod_id=6),
	Pause(1),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R145_STAR_HILL_AREA_01, mod_id=8),
	Pause(24),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R145_STAR_HILL_AREA_01, mod_id=4),
	ApplySolidityModToLevel(permanent=True, room_id=R145_STAR_HILL_AREA_01, mod_id=1),
	PlaySound(sound=SO126_EMERGE_DEEP_WATER, channel=6),
	Return(identifier="EVENT_2796_ret_13")
])
