"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E1945_KEEP_CANNONBALL_ROOM_EXIT,
        x=18,
        y=27,
        z=3,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False),
    Event(
        event=E1878_KEEP_CANNONBALL_ROOM_EXIT_TO_PREVIOUS,
        x=2,
        y=58,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False),
]
