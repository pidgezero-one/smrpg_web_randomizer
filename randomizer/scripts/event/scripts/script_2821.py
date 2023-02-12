# E2821_ASYNC_NO_ANIMATION_STAR_PIECE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO081_STAR, channel=6),
	JmpToEvent(E3092_STAR_PIECE_GRANT)
])
