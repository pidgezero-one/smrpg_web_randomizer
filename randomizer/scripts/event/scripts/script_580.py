# E0580_ROSE_TOWN_OCCUPIED_TREASURE_HOUSE_1F_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0281_CLEAR_EXP_STAR_BITS),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER)
])
