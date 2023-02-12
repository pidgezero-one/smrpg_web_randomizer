# E3292_LOWER_SHIP_GENERIC_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER)
])
