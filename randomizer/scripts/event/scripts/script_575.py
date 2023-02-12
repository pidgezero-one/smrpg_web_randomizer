# E0575_ROSE_TOWN_LIBERATED_COUPLES_HOUSE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0281_CLEAR_EXP_STAR_BITS),
	JmpToEvent(E0261_FADE_MUSIC_ROOM_LOADER)
])
