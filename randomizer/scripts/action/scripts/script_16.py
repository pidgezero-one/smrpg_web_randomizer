#A0016_INFINITE_WAIT_LOOP

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(1, identifier="ACTION_16_pause_0"),
	Jmp(["ACTION_16_pause_0"])
])
