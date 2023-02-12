# E1797_LANDS_END_SKY_BRIDGE_ROOM_EXIT_TO_DESERT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R317_LANDS_END_DESERT_AREA_01, face_direction=SOUTH, x=3, y=21, z=9, run_entrance_event=True),
	SetBit(DIRECTIONAL_7049_0),
	EnableControls([]),
	Return()
])
