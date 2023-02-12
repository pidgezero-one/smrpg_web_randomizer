# E3734_NIMBUS_CASTLE_FINAL_CHEST_HALLWAY_EXIT_TO_FINAL_HALLWAY

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD, face_direction=NORTHEAST, x=1, y=95, z=0, run_entrance_event=True),
	Return()
])
