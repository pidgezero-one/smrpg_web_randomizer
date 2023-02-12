# E2557_BEAN_VALLEY_WATERS_BOSS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(192),
	SetSyncActionScript(NPC_1, A0845_ACTIVATE_PIRANHA_PLANT_IN_PIPE),
	Return()
])
