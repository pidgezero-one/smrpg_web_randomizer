# E0517_ROSE_TOWN_OCCUPIED_EXIT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, face_direction=SOUTHWEST, x=4, y=38, z=1, run_entrance_event=True),
	Return()
])
