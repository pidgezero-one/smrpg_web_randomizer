# E1942_KEEP_VERTICAL_PLATFORM_ROOM_EXIT_TO_PREVIOUS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, face_direction=NORTHEAST, x=2, y=57, z=0),
	JmpToEvent(E1835_KEEP_CANNONBALL_ROOM_LOADER)
])
