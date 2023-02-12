# E3514_NIMBUS_CASTLE_EGG_ROOM_EXIT_TO_PREVIOUS_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3514_enter_area_1"]),
	EnterArea(room_id=R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA, face_direction=SOUTHWEST, x=26, y=109, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, face_direction=SOUTHWEST, x=26, y=109, z=0, run_entrance_event=True, identifier="EVENT_3514_enter_area_1"),
	Return()
])
