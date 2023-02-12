# E2112_NIMBUS_CASTLE_STATUE_GAME_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0819_NIMBUS_CASTLE_STATUE_POLISHING_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return()
])
