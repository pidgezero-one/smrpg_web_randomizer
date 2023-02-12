# E3278_SHIP_OPEN_DOOR_TO_FINAL_BOSS_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3278_ret_4"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM, mod_id=0),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	SetBit(TEMP_7043_0),
	Return(identifier="EVENT_3278_ret_4")
])
