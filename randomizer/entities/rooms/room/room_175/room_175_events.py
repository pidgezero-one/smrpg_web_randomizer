"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3268_SHIP_OUTER_CLONE_ROOM_OPEN_LEFT_DOOR,
        x=1,
        y=120,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=4,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E3269_SHIP_OUTER_CLONE_ROOM_OPEN_RIGHT_DOOR,
        x=4,
        y=113,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=4,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
