#A0527_SEASIDE_BOSS_TRANSFORM

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(identifier="ACTION_527_visibility_off_0"),
	Pause(5),
	VisibilityOn(),
	Pause(3),
	Jmp(["ACTION_527_visibility_off_0"])
])
