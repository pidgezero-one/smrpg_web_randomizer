# E1964_KEEP_ENTER_GOOMBA_BATTLE_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA, face_direction=NORTHEAST, x=2, y=63, z=0),
	JmpToEvent(E2175_KEEP_GOOMBA_BATTLE_ROOM_LOADER)
])
