# E3852_WORLD_MAP_YOSTER_ISLE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	EnterArea(room_id=R034_YOSTER_ISLE, face_direction=NORTHEAST, x=8, y=87, z=0, run_entrance_event=True),
	Return()
])
