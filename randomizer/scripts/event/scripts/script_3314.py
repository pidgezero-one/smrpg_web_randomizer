# pylint: disable=C0301

"""E3314_SEWERS_RAT_LINE_ROOM_EXIT_TO_3RD_WATER_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER,
            face_direction=SOUTHWEST,
            x=12,
            y=101,
            z=3),
        Jmp(["EVENT_3315_jmp_if_bit_clear_1"]),
    ]
)
