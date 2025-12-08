"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3163_SEWERS_TUTORIAL_ROOM_EXIT_TO_EXTERIOR,
        x=5,
        y=90,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False),
    Event(
        event=E3164_SEWERS_TUTORIAL_ROOM_PIPE_TO_FIRST_WATER_ROOM,
        x=14,
        y=90,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False),
]
