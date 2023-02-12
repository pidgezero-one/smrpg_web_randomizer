#A0946_WIGGLER_ASLEEP

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_946_set_sprite_sequence_0"),
	Pause(128, identifier="ACTION_946_pause_1"),
	JmpIfRandom1of2(["ACTION_946_start_loop_n_times_9"]),
	StartLoopNTimes(2),
	ShiftNortheastPixels(1),
	ShiftSouthwestPixels(1),
	EndLoop(),
	Pause(128),
	Jmp(["ACTION_946_set_sprite_sequence_0"]),
	StartLoopNTimes(2, identifier="ACTION_946_start_loop_n_times_9"),
	ShiftSoutheastPixels(1),
	ShiftNorthwestPixels(1),
	EndLoop(),
	Pause(128),
	Jmp(["ACTION_946_pause_1"])
])
