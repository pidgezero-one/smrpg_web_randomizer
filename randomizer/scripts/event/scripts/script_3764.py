# E3764_NIMBUS_FIRST_FALL_ROOM_LOAD_2ND_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnterArea(room_id=R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND, face_direction=SOUTH, x=27, y=67, z=4),
	RunEventAsSubroutine(E3763_NIMBUS_BACK_EXIT_MARIO_FALL_ANIMATION),
	Return()
])
