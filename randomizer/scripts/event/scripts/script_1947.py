# E1947_KEEP_LINEAR_PLATFORM_ROOM_EXIT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS, face_direction=NORTHEAST, x=22, y=123, z=0),
	JmpToEvent(E1836_KEEP_DONKEY_ROOM_LOADER)
])
