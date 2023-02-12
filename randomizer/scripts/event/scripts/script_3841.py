# E3841_WORLD_MAP_MARIOS_PAD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	EnterArea(room_id=R016_MARIOS_PAD, face_direction=NORTHWEST, x=9, y=49, z=0, run_entrance_event=True),
	Return()
])
