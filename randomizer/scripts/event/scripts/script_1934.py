# pylint: disable=C0301

"""E1934_BELOME_FORTUNE_PRIZE_CHEST_4"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_9,
            R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            ["EVENT_1934_jmp_to_event_7"],
        ),
        RunBackgroundEvent(
            event_id=E1767_TEMPLE_FORTUNE_RESULTS_ROOM_GATE_OPENS,
            return_on_level_exit=True,
        ),
        JmpToEvent(E0175_CHEST_4_CONTAINER, identifier="EVENT_1934_jmp_to_event_7"),
    ]
)
