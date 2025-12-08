# pylint: disable=C0301

"""E3315_SEWERS_3RD_WATER_ROOM_EXIT_TO_RAT_LINE_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE,
            face_direction=NORTHEAST,
            x=20,
            y=42,
            z=2),
        JmpIfBitClear(
            SEWER_WATER_LEVEL,
            ["EVENT_3315_jmp_to_event_3"],
            identifier="EVENT_3315_jmp_if_bit_clear_1"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=0, silent=True),
                ASPause(
                    1, identifier="EVENT_3315_action_queue_async_2_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3315_action_queue_async_2_SUBSCRIPT_pause_1"]
                ),
            ]),
        JmpToEvent(E3135_SEWERS_GENERIC_LOADER, identifier="EVENT_3315_jmp_to_event_3"),
    ]
)
