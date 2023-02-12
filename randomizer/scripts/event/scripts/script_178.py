# E0178_NPC_QUEST_1_CONTAINER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpToEvent(E0253_NPC_QUEST_1_GRANT)
])
