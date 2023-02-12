#A0515_MARIO_DURING_SONGS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceSouthwest7D(identifier="ACTION_515_face_southwest_7D_0"),
	Pause(2),
	Jmp(["ACTION_515_face_southwest_7D_0"])
])
