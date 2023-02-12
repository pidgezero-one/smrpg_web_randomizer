# E0175_CHEST_4_CONTAINER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpToEvent(E0244_CHEST_4_GRANT)
])
