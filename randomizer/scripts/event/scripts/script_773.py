# pylint: disable=C0301

"""E0773_KERO_SEWERS_BELOME_ROOM_LOADER_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0772_KERO_SEWERS_BELOME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpToEvent(E3135_SEWERS_GENERIC_LOADER),
    ]
)
