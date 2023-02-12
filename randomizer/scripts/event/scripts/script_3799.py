# E3799_ENDING_CREDITS_PURPLE_STAR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(8),
	RunEventSequence(scene=SC13_RUN_STAR_PIECE_END_SEQUENCE, value=3),
	Pause(8),
	JmpToEvent(E3807_ENDING_CREDITS_RACE_LOADER)
])
