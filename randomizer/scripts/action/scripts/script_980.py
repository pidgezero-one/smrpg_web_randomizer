#A0980_NIMBUS_CASTLE_CAGED_BIRD

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(),
	SetPriority(3),
	SetWalkingSpeed(SLOW),
	TransferXYZFPixels(x=251, y=254, z=5, direction=EAST),
	Pause(30, identifier="ACTION_980_pause_4"),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	ShiftZUpPixels(8),
	ShiftZDownPixels(8),
	SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
	JmpIfRandom1of2(["ACTION_980_pause_11"]),
	Pause(60),
	Pause(60, identifier="ACTION_980_pause_11"),
	JmpIfRandom1of2(["ACTION_979_set_sprite_sequence_4"]),
	Jmp(["ACTION_980_pause_4"])
])
