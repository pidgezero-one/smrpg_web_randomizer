# E0559_ROSE_TOWN_COUPLES_HOUSE_EXIT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(FOREST_LIBERATED, ["EVENT_559_enter_area_3"]),
	EnterArea(room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, face_direction=SOUTHWEST, x=15, y=36, z=1, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R084_ROSE_TOWN_OUTSIDE, face_direction=SOUTHWEST, x=15, y=36, z=1, run_entrance_event=True, identifier="EVENT_559_enter_area_3"),
	Return()
])
