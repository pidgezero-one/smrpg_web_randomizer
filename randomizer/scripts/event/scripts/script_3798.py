# E3798_ENDING_CREDITS_ORANGE_STAR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(8),
	RunEventSequence(scene=SC13_RUN_STAR_PIECE_END_SEQUENCE, value=2),
	Pause(8),
	JmpToEvent(E2628_ENDING_CREDITS_SUNSET_OPENER)
])
