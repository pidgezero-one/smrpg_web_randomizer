# pylint: disable=C0301

"""E0879_SHIP_TRAMPOLINE_LOADER_OVERRIDE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [SummonObjectToCurrentLevel(NPC_0), JmpToEvent(E0015_STANDARD_ROOM_LOADER)]
)
