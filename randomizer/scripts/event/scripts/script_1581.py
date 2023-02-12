# E1581_MIDAS_RIVER_BARREL_SUBROUTINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_7, ["EVENT_1581_ret_3"]),
	SetBit(TEMP_7043_7),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 4, ["EVENT_1581_db_4"]),
	Return(identifier="EVENT_1581_ret_3"),
	Db(bytearray(b'\xfd\x8d'), identifier="EVENT_1581_db_4"),
	ApplyTileModToLevel(use_alternate=True, room_id=R068_MIDAS_RIVER_BARREL_JUMPING_RIVER, mod_id=3),
	Return()
])
