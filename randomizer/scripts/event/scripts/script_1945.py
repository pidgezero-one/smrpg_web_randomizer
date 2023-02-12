# E1945_KEEP_CANNONBALL_ROOM_EXIT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS, face_direction=NORTHEAST, x=6, y=47, z=1),
	JmpToEvent(E1825_KEEP_ROTATING_ROOM_LOADER)
])
