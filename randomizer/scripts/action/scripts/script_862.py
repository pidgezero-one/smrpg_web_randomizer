#A0862_ABYSS_1ST_BOSS_FIGHT_CAMERA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(FASTER, identifier="ACTION_862_set_animation_speed_0"),
	ShiftEastPixels(4),
	ShiftWestPixels(8),
	ShiftEastPixels(4),
	Jmp(["ACTION_862_set_animation_speed_0"])
])
