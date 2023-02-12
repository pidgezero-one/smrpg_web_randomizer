# E0174_CHEST_3_CONTAINER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpToEvent(E0245_CHEST_3_GRANT)
])
