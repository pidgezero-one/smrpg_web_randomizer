#A0379_MARRYMORE_LIBERATED_EXTERIOR_PHOTO_KID

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceSouthwest(identifier="ACTION_379_face_southwest_0"),
	JumpToHeight(height=64, silent=True),
	Pause(1, identifier="ACTION_379_pause_2"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_379_pause_2"]),
	JmpIfBitSet(TEMP_7043_1, ["ACTION_379_face_southeast_6"]),
	Jmp(["ACTION_379_face_southwest_0"]),
	FaceSoutheast(identifier="ACTION_379_face_southeast_6"),
	Pause(1, identifier="ACTION_379_pause_7"),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_379_face_southwest_0"]),
	Jmp(["ACTION_379_pause_7"])
])
