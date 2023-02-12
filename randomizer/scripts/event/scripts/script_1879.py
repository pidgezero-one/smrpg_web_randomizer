# E1879_KEEP_LINEAR_PLATFORM_ROOM_EXIT_TO_PREVIOUS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, face_direction=SOUTHWEST, x=26, y=88, z=2),
	SetBit(TEMP_7044_6),
	JmpToEvent(E1826_KEEP_INVISIBLE_FLOOR_ROOM_LOADER)
])
