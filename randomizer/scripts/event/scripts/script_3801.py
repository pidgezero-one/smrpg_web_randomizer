# E3801_ENDING_CREDITS_RED_STAR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(8),
	RunEventSequence(scene=SC13_RUN_STAR_PIECE_END_SEQUENCE, value=5),
	Pause(8),
	JmpToEvent(E2295_ENDING_CREDITS_WEDDING_LOGIC)
])
