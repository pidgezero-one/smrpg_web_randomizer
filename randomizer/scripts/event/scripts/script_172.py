# E0172_CHEST_1_CONTAINER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpToEvent(E0247_CHEST_1_GRANT)
])
