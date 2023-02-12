#A0359_PLAYER_IN_FOREST_TRUNK_ROOM_MIDDLE_LEFT_TRUNK

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpToSubroutine(["ACTION_355_shadow_off_3"]),
	WalkToXYCoords(x=9, y=92),
	Jmp(["ACTION_355_set_animation_speed_10"])
])
