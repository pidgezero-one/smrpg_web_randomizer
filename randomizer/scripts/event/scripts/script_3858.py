# E3858_WORLD_MAP_SEASIDE_TOWN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	EnterArea(room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, face_direction=NORTHEAST, x=13, y=62, z=1, run_entrance_event=True),
	Return()
])
