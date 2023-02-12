# E0674_MARRYMORE_UNOCCUPIED_EXTERIOR_OPEN_FRONT_CHAPEL_ENTRANCE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_0, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7043_0),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R064_MARRYMORE_OUTSIDE, mod_id=0),
	Return()
])
