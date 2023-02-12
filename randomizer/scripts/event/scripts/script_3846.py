# E3846_WORLD_MAP_MIDAS_RIVER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	EnterArea(room_id=R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA, face_direction=NORTHWEST, x=22, y=35, z=0, run_entrance_event=True),
	Return()
])
