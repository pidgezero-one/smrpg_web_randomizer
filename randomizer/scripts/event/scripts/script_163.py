# E0163_CHEST_GRANT_STAR_PIECE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E3094_STAR_PIECE_CHEST_ANIMATION),
	JmpToEvent(E3092_STAR_PIECE_GRANT),
	Return()
])
