"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3169_SEWERS_STAIR_ROOM_PIPE_TO_THIRD_WATER_ROOM,
        x=2,
        y=42,
        z=1,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E3171_SEWERS_STAIR_ROOM_PIPE_TO_FOUR_RAT_ROOM,
        x=11,
        y=54,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E3177_SEWERS_STAIR_ROOM_PIPE_TO_FOUR_RAT_ROOM,
        x=16,
        y=46,
        z=14,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
