# E1949_KEEP_ALLEY_RAT_BATTLE_ROOM_EXIT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB, face_direction=NORTHEAST, x=2, y=63, z=0),
	JmpToEvent(E2170_KEEP_BOBOMB_BATTLE_ROOM_LOADER)
])
