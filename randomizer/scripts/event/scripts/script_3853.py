# E3853_WORLD_MAP_MOLEVILLE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
	JmpIfBitSet(MINECART_CLEARED, ["EVENT_3853_enter_area_3"]),
	EnterArea(room_id=R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES, face_direction=NORTHEAST, x=13, y=91, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R108_MOLEVILLE_OUTSIDE, face_direction=NORTHEAST, x=13, y=91, z=0, run_entrance_event=True, identifier="EVENT_3853_enter_area_3"),
	Return()
])
