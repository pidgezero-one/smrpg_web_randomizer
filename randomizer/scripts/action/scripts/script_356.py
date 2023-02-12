#A0356_PLAYER_IN_FOREST_TRUNK_ROOM_RIGHTMOST_TRUNK

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpToSubroutine(["ACTION_355_shadow_off_3"]),
	WalkToXYCoords(x=16, y=92),
	Jmp(["ACTION_355_set_animation_speed_10"])
])
