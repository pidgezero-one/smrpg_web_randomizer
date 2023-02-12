# E3863_WORLD_MAP_BEAN_VALLEY

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	EnterArea(room_id=R252_BEAN_VALLEY_MAIN_AREA, face_direction=NORTHEAST, x=4, y=115, z=0, run_entrance_event=True),
	Return()
])
