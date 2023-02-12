# E0320_MUSHROOM_KINGDOM_MAIN_HALL_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set0158Bit7Offset(),
	Set0158Bit7Offset(),
	ClearBit(TEMP_7042_7),
	ApplySolidityModToLevel(permanent=True, room_id=R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL, mod_id=0),
	FadeInFromBlack(sync=False),
	Return()
])
