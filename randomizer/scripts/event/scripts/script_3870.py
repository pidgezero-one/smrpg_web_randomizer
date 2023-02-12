# E3870_WORLD_MAP_GRATE_GUYS_CASINO

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	EnterArea(room_id=R106_GRATE_GUYS_CASINO_OUTSIDE, face_direction=NORTHEAST, x=3, y=94, z=0, run_entrance_event=True),
	Return()
])
