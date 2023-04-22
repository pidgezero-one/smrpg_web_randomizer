# pylint: disable=C0301

"""E1932_BELOME_FORTUNE_PRIZE_CHEST_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_7,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_1932_jmp_to_event_7"],
        ),
        RunBackgroundEvent(
            event_id=E1767_TEMPLE_FORTUNE_RESULTS_ROOM_GATE_OPENS,
            return_on_level_exit=True,
        ),
        JmpToEvent(E0173_CHEST_2_CONTAINER, identifier="EVENT_1932_jmp_to_event_7"),
    ]
)
