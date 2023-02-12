# E0837_NIMBUS_CASTLE_LIBERATED_4WAY_PATH_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0836_NIMBUS_CASTLE_LIBERATED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER)
])
