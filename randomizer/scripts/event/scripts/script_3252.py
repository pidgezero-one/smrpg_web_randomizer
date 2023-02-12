# E3252_SHIP_PUZZLE_HUB_ROOM_OPEN_UPPER_EXIT_DOOR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3252_ret_4"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, mod_id=0),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	SetBit(TEMP_7043_0),
	Return(identifier="EVENT_3252_ret_4")
])
