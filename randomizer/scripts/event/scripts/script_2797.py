# E2797_STAR_HILL_PROGRESS_FLOWER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_1, ["EVENT_2797_ret_13"]),
	SetBit(TEMP_7043_1),
	PlaySound(sound=SO081_STAR, channel=6),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R145_STAR_HILL_AREA_01, mod_id=5),
	Pause(1),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R145_STAR_HILL_AREA_01, mod_id=7),
	Pause(24),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R145_STAR_HILL_AREA_01, mod_id=2),
	ApplySolidityModToLevel(permanent=True, room_id=R145_STAR_HILL_AREA_01, mod_id=0),
	PlaySound(sound=SO126_EMERGE_DEEP_WATER, channel=6),
	Return(identifier="EVENT_2797_ret_13"),
	Return()
])
