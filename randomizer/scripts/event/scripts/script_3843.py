# pylint: disable=C0301

"""E3843_WORLD_MAP_MUSHROOM_KINGDOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        JmpIfBitSet(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_3843_jmp_if_bit_set_6"]),
        JmpIfVarEqualsConst(
            LAST_OVERWORLD_MARKER_ID,
            9,
            ["EVENT_3843_enter_area_4"],
            identifier="EVENT_3843_jmp_if_var_equals_const_1"),
        EnterArea(
            room_id=R191_MUSHROOM_KINGDOM_OUTSIDE,
            face_direction=NORTHWEST,
            x=21,
            y=122,
            z=2,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R191_MUSHROOM_KINGDOM_OUTSIDE,
            face_direction=NORTHEAST,
            x=2,
            y=102,
            z=2,
            run_entrance_event=True,
            identifier="EVENT_3843_enter_area_4"),
        Return(),
        JmpIfBitSet(
            MUSHROOM_KINGDOM_LIBERATED,
            ["EVENT_3843_jmp_if_var_equals_const_1"],
            identifier="EVENT_3843_jmp_if_bit_set_6"),
        JmpIfVarEqualsConst(LAST_OVERWORLD_MARKER_ID, 9, ["EVENT_3843_enter_area_10"]),
        EnterArea(
            room_id=R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
            face_direction=NORTHWEST,
            x=21,
            y=122,
            z=2,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
            face_direction=NORTHEAST,
            x=2,
            y=102,
            z=2,
            run_entrance_event=True,
            identifier="EVENT_3843_enter_area_10"),
        Return(),
    ]
)
