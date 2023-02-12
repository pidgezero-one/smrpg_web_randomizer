# E3312_SEWERS_1ST_WATER_ROOM_EXIT_TO_RAT_LINE_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE, face_direction=SOUTHWEST, x=26, y=29, z=2),
	Jmp(["EVENT_3315_jmp_if_bit_clear_1"])
])
