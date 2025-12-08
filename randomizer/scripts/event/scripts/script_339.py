# pylint: disable=C0301

"""E0339_MUSHROOM_KINGDOM_OCCUPIED_RAZ_RAINI_HOUSE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_3,
            R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
            ["EVENT_339_jmp_to_event_2"]),
        RunBackgroundEvent(
            event_id=E0340_MUSHROOM_KINGDOM_OCCUPIED_RAZ_RAINI_HOUSE_SHAKE,
            return_on_level_exit=True),
        JmpToEvent(
            E0344_MUSHROOM_KINGDOM_RAZ_RAINI_HOUSE_LOADER,
            identifier="EVENT_339_jmp_to_event_2"),
    ]
)
