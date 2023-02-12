# E3800_ENDING_CREDITS_INDIGO_STAR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(8),
	RunEventSequence(scene=SC13_RUN_STAR_PIECE_END_SEQUENCE, value=4),
	Pause(8),
	JmpToEvent(E2292_ENDING_CREDITS_TOADOFSKY)
])
