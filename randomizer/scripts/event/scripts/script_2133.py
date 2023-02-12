# E2133_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_FIGHT_ROOM_EXIT_TO_4WAY_PATH

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_2133_enter_area_3"]),
	EnterArea(room_id=R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA, face_direction=NORTHWEST, x=31, y=20, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA, face_direction=NORTHWEST, x=31, y=20, z=0, run_entrance_event=True, identifier="EVENT_2133_enter_area_3"),
	Return()
])
