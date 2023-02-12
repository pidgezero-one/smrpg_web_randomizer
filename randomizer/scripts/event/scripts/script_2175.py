# E2175_KEEP_GOOMBA_BATTLE_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	ClearBit(TEMP_7043_3),
	ClearBit(TEMP_7043_4),
	RunEventAsSubroutine(E0852_KEEP_BATTLE_DOOR_2A_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return()
])
