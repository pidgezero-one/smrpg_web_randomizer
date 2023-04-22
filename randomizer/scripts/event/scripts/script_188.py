# pylint: disable=C0301

"""E0188_MALLOW_JOINS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CharacterJoinsParty(Mallow),
        JmpToEvent(E0209_UNLOCK_SWITCH_MENU_IF_ENOUGH_MEMBERS),
    ]
)
