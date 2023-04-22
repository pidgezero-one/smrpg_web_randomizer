# pylint: disable=C0301

"""E3729_NIMBUS_CASTLE_OCCUPIED_THRONE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0826_NIMBUS_CASTLE_OCCUPIED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
