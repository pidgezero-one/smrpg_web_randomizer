# E3866_WORLD_MAP_VISTA_HILL

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R015_VISTA_HILL, face_direction=NORTHWEST, x=4, y=16, z=0, run_entrance_event=True),
	Return()
])
