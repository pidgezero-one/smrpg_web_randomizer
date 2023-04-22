# pylint: disable=C0301

"""E0191_TOADSTOOL_JOINS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CharacterJoinsParty(TOADSTOOL),
        JmpToEvent(E0209_UNLOCK_SWITCH_MENU_IF_ENOUGH_MEMBERS),
    ]
)
