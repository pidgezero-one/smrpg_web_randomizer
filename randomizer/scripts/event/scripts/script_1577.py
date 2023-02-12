# E1577_MIDAS_RIVER_BARREL_SUBROUTINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1577_ret_4"]),
	ClearBit(TEMP_7043_2),
	SetBit(TEMP_7043_3),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 4, ["EVENT_1577_db_5"]),
	Return(identifier="EVENT_1577_ret_4"),
	Db(bytearray(b'\xfd\x8d'), identifier="EVENT_1577_db_5"),
	ApplyTileModToLevel(use_alternate=True, room_id=R068_MIDAS_RIVER_BARREL_JUMPING_RIVER, mod_id=0),
	SetBit(UNKNOWN_MIDAS_RIVER_7078_2),
	Return()
])
