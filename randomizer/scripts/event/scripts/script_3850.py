# E3850_WORLD_MAP_ROSE_TOWN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	JmpIfBitSet(FOREST_LIBERATED, ["EVENT_3850_enter_area_3"]),
	EnterArea(room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, face_direction=NORTHEAST, x=7, y=53, z=1, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R084_ROSE_TOWN_OUTSIDE, face_direction=NORTHEAST, x=7, y=53, z=1, run_entrance_event=True, identifier="EVENT_3850_enter_area_3"),
	Return()
])
