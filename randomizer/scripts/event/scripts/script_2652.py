# E2652_SEASIDE_EXIT_TO_BEACH

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(SEASIDE_LIBERATED, ["EVENT_2652_enter_area_43"]),
	EnterArea(room_id=R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH, face_direction=NORTHWEST, x=12, y=38, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R316_SEASIDE_TOWN_BEACH, face_direction=NORTHWEST, x=12, y=38, z=0, run_entrance_event=True, identifier="EVENT_2652_enter_area_43"),
	Return()
])
