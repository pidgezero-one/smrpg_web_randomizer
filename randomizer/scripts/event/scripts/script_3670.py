# E3670_NIMBUS_CASTLE_MAIN_HALL_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 49),
	RunEventAsSubroutine(E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return()
])
