# E3265_SHIP_LOWER_FIRST_DRYBONES_ROOM_OPEN_LOWER_DOOR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_1, ["EVENT_3265_ret_4"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R180_SUNKEN_SHIP_POSTKC_AREA_02_SMALL_2LEVEL_ROOM, mod_id=1),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	SetBit(TEMP_7043_1),
	Return(identifier="EVENT_3265_ret_4")
])
