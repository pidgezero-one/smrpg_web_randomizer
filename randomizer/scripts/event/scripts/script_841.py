# E0841_VOLCANO_FINAL_PRE_EXIT_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0842_VOLCANO_FINAL_PRE_EXIT_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER)
])
