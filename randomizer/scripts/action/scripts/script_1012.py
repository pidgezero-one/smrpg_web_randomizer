#A1012_MUSHROOM_WAY_1_RECRUITABLE_CHARACTER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceMario(identifier="ACTION_1012_face_mario_0"),
	JumpToHeight(height=64, silent=True),
	Pause(16),
	Jmp(["ACTION_1012_face_mario_0"])
])
