#A0903_COIN_SHOWER_NE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceNortheast(),
	JumpToHeight(height=112, silent=True, identifier="ACTION_903_jump_to_height_silent_1"),
	ShadowOff(),
	SetVRAMPriority(PRIORITY_3),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	ShiftFDirectionSteps(2),
	VisibilityOff(),
	Return()
])
