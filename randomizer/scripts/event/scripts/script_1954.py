# E1954_KEEP_ENTER_BARREL_COUNT_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R463_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1B_BARRELCOUNTING, face_direction=NORTHEAST, x=2, y=55, z=0),
	JmpToEvent(E3354_KEEP_BARREL_COUNT_LOADER)
])
