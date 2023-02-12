# E1948_KEEP_TERRA_CORRA_BATTLE_ROOM_EXIT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT, face_direction=NORTHEAST, x=2, y=63, z=0),
	JmpToEvent(E2165_KEEP_ALLEY_RAT_BATTLE_ROOM_LOADER)
])
