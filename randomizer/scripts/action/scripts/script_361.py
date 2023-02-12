#A0361_PLAYER_IN_FOREST_TRUNK_ROOM_UPPER_RIGHT_TRUNK

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpToSubroutine(["ACTION_355_shadow_off_3"]),
	WalkToXYCoords(x=6, y=84),
	Jmp(["ACTION_355_set_animation_speed_10"])
])
