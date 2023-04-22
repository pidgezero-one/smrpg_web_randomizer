# pylint: disable=C0301

"""E0833_NIMBUS_CASTLE_LIBERATED_INNER_CELLAR_HALLWAY_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0834_NIMBUS_CASTLE_LIBERATED_INNER_CELLAR_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
    ]
)
