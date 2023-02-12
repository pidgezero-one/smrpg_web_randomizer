#A0338_SHIP_TRAMPOLINE_PUZZLE_SCROLL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FloatingOff(),
	VisibilityOff(),
	Pause(6),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	SetSpriteSequence(index=1, is_sequence=True, looping=False),
	IncPaletteRowBy(2),
	VisibilityOn(),
	FloatingOn(),
	JumpToHeight(height=0, silent=True),
	SetSolidityBits(cant_pass_walls=True, cant_jump_through=True, bit_4=True, cant_walk_through=True),
	SetVRAMPriority(NORMAL_PRIORITY),
	Pause(1),
	Return()
])
