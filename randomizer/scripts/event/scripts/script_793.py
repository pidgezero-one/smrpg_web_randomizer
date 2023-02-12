# E0793_TOWER_FIRST_BOBOMB_STAIRCASE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0792_TOWER_FIRST_BOBOMB_STAIRCASE_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER)
])
