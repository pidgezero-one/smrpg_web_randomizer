#A0357_PLAYER_IN_FOREST_TRUNK_ROOM_LOWEST_TRUNK

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpToSubroutine(["ACTION_355_shadow_off_3"]),
	WalkToXYCoords(x=13, y=98),
	Jmp(["ACTION_355_set_animation_speed_10"])
])
