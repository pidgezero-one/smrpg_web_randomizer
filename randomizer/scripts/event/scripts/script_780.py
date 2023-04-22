# pylint: disable=C0301

"""E0780_MINES_TINY_ROOM_2_LEFT_OF_TRAMPOLINE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E0781_MINES_TINY_ROOM_2_LEFT_OF_TRAMPOLINE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
    ]
)
