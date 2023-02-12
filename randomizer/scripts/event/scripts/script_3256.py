# E3256_SHIP_PUZZLE_HUB_ROOM_OPEN_LOWER_EXIT_DOOR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E1605_TOWER_EXTERIOR_CANCEL_EXP_STAR),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_3256_ret_4"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, mod_id=4),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	SetBit(TEMP_7043_4),
	Return(identifier="EVENT_3256_ret_4")
])
