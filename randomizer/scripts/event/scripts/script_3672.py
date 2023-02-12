# E3672_NIMBUS_CASTLE_BACK_EXIT_FALL

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R371_NIMBUS_LAND_FALL_FROM_PLATFORM_1ST, face_direction=NORTHEAST, x=27, y=29, z=6),
	JmpToEvent(E3745_NIMBUS_BACK_EXIT_INITIATE_FALLING_SEQUENCE)
])
