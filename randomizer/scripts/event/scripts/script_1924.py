# pylint: disable=C0301

"""E1924_WORLD_MAP_INNER_FACTORY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        JmpIfBitClear(FAST_TRAVEL_ENABLED, ["EVENT_1924_jmp_if_bit_set_0"]),
        SetBit(MAP_INNER_FACTORY),
        JmpIfBitSet(
            INNER_FACTORY_ROOM_1_COMPLETED,
            ["EVENT_1924_enter_area_3"],
            identifier="EVENT_1924_jmp_if_bit_set_0"),
        EnterArea(
            room_id=R469_FACTORY_GROUNDS_AREA_01,
            face_direction=NORTHWEST,
            x=15,
            y=55,
            z=5,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
            face_direction=NORTHWEST,
            x=15,
            y=55,
            z=5,
            run_entrance_event=True,
            identifier="EVENT_1924_enter_area_3"),
        Return(),
    ]
)
