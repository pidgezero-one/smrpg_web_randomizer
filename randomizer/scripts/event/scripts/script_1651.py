# E1651_MARIO_CRASH_THRU_MOLEVILLE_ROOF

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R108_MOLEVILLE_OUTSIDE, face_direction=SOUTHWEST, x=30, y=43, z=2, run_entrance_event=True),
	Return()
])
