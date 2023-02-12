#A0715_FOREVER_PAUSE_LOOP

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(1, identifier="ACTION_715_pause_0"),
	Jmp(["ACTION_715_pause_0"])
])
