"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3137_SEWERS_1ST_WATER_ROOM_PIPE_TO_TUTORIAL_ROOM,
        x=12,
        y=26,
        z=9,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E3138_SEWERS_1ST_WATER_ROOM_PIPE_TO_3RD_WATER_ROOM,
        x=2,
        y=46,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E3140_1ST_WATER_TOOM_PIPE_TO_SEWERS_4_RAT_ROOM,
        x=14,
        y=30,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E3312_SEWERS_1ST_WATER_ROOM_EXIT_TO_RAT_LINE_ROOM,
        x=3,
        y=50,
        z=2,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
