# pylint: disable=C0301

"""E1808_BELOME_FORTUNE_PRIZE_CHEST_1_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_1808_jmp_to_event_7"],
        ),
        RunBackgroundEvent(
            event_id=E1767_TEMPLE_FORTUNE_RESULTS_ROOM_GATE_OPENS,
            return_on_level_exit=True,
        ),
        JmpToEvent(E0172_CHEST_1_CONTAINER, identifier="EVENT_1808_jmp_to_event_7"),
    ]
)
