# E0188_MALLOW_JOINS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CharacterJoinsParty(MALLOW),
	JmpToEvent(E0209_UNLOCK_SWITCH_MENU_IF_ENOUGH_MEMBERS)
])
