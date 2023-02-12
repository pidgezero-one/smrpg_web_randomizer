# E3867_WORLD_MAP_BOOSTER_HILL

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(BOOSTER_HILL_CLEARED, ["EVENT_3867_enter_area_3"]),
	EnterArea(room_id=R054_BOOSTER_HILL_____DUMMY, face_direction=NORTHWEST, x=7, y=57, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R014_BOOSTER_HILL, face_direction=NORTHWEST, x=7, y=57, z=0, run_entrance_event=True, identifier="EVENT_3867_enter_area_3"),
	Return()
])
