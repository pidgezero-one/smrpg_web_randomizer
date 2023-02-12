# E1966_KEEP_ENTER_QUIZ_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R464_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1A_QUIZ, face_direction=NORTHEAST, x=3, y=106, z=0),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER)
])
