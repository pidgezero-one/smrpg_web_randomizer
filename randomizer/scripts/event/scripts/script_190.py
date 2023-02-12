# E0190_BOWSER_JOINS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CharacterJoinsParty(BOWSER),
	JmpToEvent(E0209_UNLOCK_SWITCH_MENU_IF_ENOUGH_MEMBERS)
])
