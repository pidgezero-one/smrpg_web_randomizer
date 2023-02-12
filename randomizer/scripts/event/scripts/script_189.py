# E0189_GENO_JOINS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CharacterJoinsParty(GENO),
	JmpToEvent(E0209_UNLOCK_SWITCH_MENU_IF_ENOUGH_MEMBERS)
])
