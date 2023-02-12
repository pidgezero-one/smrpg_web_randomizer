# E2515_STAR_HILL_1ST_ROOM_OPEN_DOOR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(32, identifier="EVENT_2515_pause_0"),
	Db(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R158_STAR_HILL_AREA_02, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R158_STAR_HILL_AREA_02, mod_id=0),
	PlaySound(sound=SO126_EMERGE_DEEP_WATER, channel=6),
	Store00To0248(),
	Return()
])
