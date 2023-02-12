#A0932_STUMPET

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	TransferXYZFPixels(x=0, y=0, z=0, direction=EAST, identifier="ACTION_932_transfer_xyzf_pixels_0"),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	Pause(2, identifier="ACTION_932_pause_2"),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_932_pause_2"]),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	Pause(60),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	Pause(8),
	Jmp(["ACTION_932_transfer_xyzf_pixels_0"])
])
