"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3276_SHIP_BIG_WATER_ROOM_OPEN_UPPER_DOOR,
        x=31,
        y=70,
        z=10,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=4,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E3277_SHIP_BIG_WATER_ROOM_OPEN_HIDDEN_DOOR,
        x=23,
        y=70,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=4,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E3118_WATER_STATE,
        x=28,
        y=73,
        z=10,
        f=EdgeDirection.SOUTHWEST,
        length=4,
        height=4,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
