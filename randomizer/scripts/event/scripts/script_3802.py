# E3802_ENDING_CREDITS_YELLOW_STAR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(8),
	RunEventSequence(scene=SC13_RUN_STAR_PIECE_END_SEQUENCE, value=6),
	RunEndingCredits()
])
