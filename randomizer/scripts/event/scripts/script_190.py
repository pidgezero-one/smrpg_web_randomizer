# pylint: disable=C0301

"""E0190_BOWSER_JOINS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CharacterJoinsParty(Bowser),
        JmpToEvent(E0209_UNLOCK_SWITCH_MENU_IF_ENOUGH_MEMBERS),
    ]
)
