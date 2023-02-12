# E3690_NIMBUS_CASTLE_MAIN_HALL_EXIT_TO_EXTERIOR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3690_enter_area_3"]),
	EnterArea(room_id=R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA, face_direction=SOUTHWEST, x=19, y=38, z=2, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA, face_direction=SOUTHWEST, x=19, y=38, z=2, run_entrance_event=True, identifier="EVENT_3690_enter_area_3"),
	Return()
])
