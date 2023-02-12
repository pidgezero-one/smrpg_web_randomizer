# E3306_SHIP_LOWER_HENCHMAN_ROOM_LOADER_CONTINUED

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 25, ["EVENT_3306_enter_area_4"]),
	EnterArea(room_id=R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER, face_direction=SOUTHWEST, x=30, y=71, z=10, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL, face_direction=SOUTHWEST, x=10, y=112, z=6, z_add_half_unit=True, run_entrance_event=True, identifier="EVENT_3306_enter_area_4"),
	Return()
])
