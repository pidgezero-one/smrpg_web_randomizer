#A1006_DOJO_PERMA_JUMP

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JumpToHeight(height=64, silent=True, identifier="ACTION_1006_jump_to_height_silent_0"),
	Pause(20),
	Jmp(["ACTION_1006_jump_to_height_silent_0"])
])
