# pylint: disable=C0301

"""E3818_WORLD_MAP_MUSHROOM_WAY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        JmpIfVarEqualsConst(
            LAST_OVERWORLD_MARKER_ID, 10, ["EVENT_3818_jmp_if_bit_clear_8"]
        ),
        EnterArea(
            room_id=R203_MUSHROOM_WAY_AREA_01,
            face_direction=SOUTHEAST,
            x=3,
            y=28,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_3818_enter_area_6"),
        Return(),
        JmpIfBitClear(
            TOAD_IN_MUSHROOM_WAY_3,
            ["EVENT_3818_enter_area_6"],
            identifier="EVENT_3818_jmp_if_bit_clear_8"),
        EnterArea(
            room_id=R205_MUSHROOM_WAY_AREA_03,
            face_direction=SOUTHWEST,
            x=28,
            y=89,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
