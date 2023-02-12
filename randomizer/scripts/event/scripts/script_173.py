# E0173_CHEST_2_CONTAINER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpToEvent(E0246_CHEST_2_GRANT)
])
