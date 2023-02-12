# E3250_SHIP_1ST_GREAPER_ROOM_OPEN_UPPER_DOOR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3250_ret_6"]),
	Store02To0248(),
	ApplyTileModToLevel(use_alternate=True, room_id=R161_SUNKEN_SHIP_AREA_03_GREAPERS, mod_id=32),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	SetBit(TEMP_7043_0),
	Store00To0248(),
	Return(identifier="EVENT_3250_ret_6")
])
