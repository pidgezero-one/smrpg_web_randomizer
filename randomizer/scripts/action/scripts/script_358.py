#A0358_PLAYER_IN_FOREST_TRUNK_ROOM_MIDDLE_RIGHT_TRUNK

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpToSubroutine(["ACTION_355_shadow_off_3"]),
	WalkToXYCoords(x=12, y=86),
	Jmp(["ACTION_355_set_animation_speed_10"])
])
