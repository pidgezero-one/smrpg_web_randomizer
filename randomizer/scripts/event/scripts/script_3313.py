# E3313_SEWERS_RAT_LINE_ROOM_EXIT_TO_1ST_WATER_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES, face_direction=NORTHEAST, x=3, y=49, z=2),
	Jmp(["EVENT_3315_jmp_if_bit_clear_1"])
])
