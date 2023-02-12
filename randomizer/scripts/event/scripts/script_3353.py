# E3353_KEEP_ENTER_BALL_SOLITAIRE_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R468_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2C_BALL_SOLITAIRE, face_direction=NORTHEAST, x=22, y=123, z=0),
	JmpToEvent(E3778_BALL_SOLITAIRE_SET_PUZZLE)
])
