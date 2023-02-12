# E3889_MUSHROOM_KINGDOM_STAR_PIECE_SIGNAL

from randomizer.scripts.event.script_imports import *

script = EventScript([
	ClearBit(SIGNAL_RING_BIT),
	Return(),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	ClearBit(SIGNAL_RING_BIT),
	Return()
])
