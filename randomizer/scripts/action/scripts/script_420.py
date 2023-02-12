#A0420_GOOMBA_THUMPIN_BONK

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpToSubroutine(["ACTION_420_set_sprite_sequence_2"]),
	Jmp(["ACTION_416_transfer_to_xyzf_47"]),
	SetSpriteSequence(index=1, is_mold=True, looping=True, identifier="ACTION_420_set_sprite_sequence_2"),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	ShiftZDownPixels(4),
	VisibilityOff(),
	ResetProperties(),
	Return()
])
