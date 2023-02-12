# E2569_BOOSTER_PASS_SECRET_EXIT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R100_BOOSTER_PASS_AREA_01, face_direction=SOUTHWEST, x=2, y=17, z=0, run_entrance_event=True),
	Return()
])
