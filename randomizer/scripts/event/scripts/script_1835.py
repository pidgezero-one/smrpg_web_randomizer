# E1835_KEEP_CANNONBALL_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	ClearBit(TEMP_7095_4),
	JmpToEvent(E1829_KEEP_DISPLAY_REMAINING_TRIES)
])
