# E1944_KEEP_CHEWY_BATTLE_ROOM_EXIT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY, face_direction=NORTHEAST, x=2, y=63, z=0),
	JmpToEvent(E2185_KEEP_SPARKY_BATTLE_ROOM_LOADER)
])
