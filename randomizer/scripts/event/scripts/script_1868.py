# E1868_LANDS_END_FLOWER_ROOM_EXIT_TO_SKY_BRIDGE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(FLOWER_TOWER_ASCENDED),
	EnterArea(room_id=R142_LANDS_END_AREA_05_SKY_BRIDGE, face_direction=NORTHEAST, x=19, y=105, z=13, run_entrance_event=True),
	Return()
])
