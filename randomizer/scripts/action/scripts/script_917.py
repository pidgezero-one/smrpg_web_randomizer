#A0917_SEQ_0_FALLING

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	Pause(2, identifier="ACTION_917_pause_2"),
	SetPriority(3),
	VisibilityOn(),
	FloatingOn(),
	SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	JumpToHeight(height=0, silent=True),
	Pause(1, identifier="ACTION_917_pause_8"),
	Jmp(["ACTION_917_pause_8"])
])
