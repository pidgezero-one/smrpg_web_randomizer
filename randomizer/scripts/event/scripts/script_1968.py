# E1968_KEEP_ENTER_COIN_GAME_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R467_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2A_COIN_COLLECTING, face_direction=NORTHEAST, x=22, y=83, z=0),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER)
])
