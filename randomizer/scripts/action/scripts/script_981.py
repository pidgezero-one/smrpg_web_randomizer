#A0981_NIMBUS_CASTLE_CAGED_BIRD

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(),
	SetPriority(3),
	SetWalkingSpeed(SLOW),
	TransferXYZFPixels(x=251, y=254, z=0, direction=EAST),
	JmpIfRandom1of2(["ACTION_979_set_sprite_sequence_4"]),
	Jmp(["ACTION_980_pause_4"])
])
