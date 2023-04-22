# pylint: disable=C0301

"""E0764_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ANTECHAMBER_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0763_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ANTECHAMBER_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
    ]
)
