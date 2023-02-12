# E2608_FACTORY_1ST_ROOM_EXIT_TO_2ND_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R471_FACTORY_GROUNDS_AREA_02, face_direction=NORTHWEST, x=14, y=55, z=5, run_entrance_event=True),
	Return()
])
