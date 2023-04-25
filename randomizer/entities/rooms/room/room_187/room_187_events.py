"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3272_SHIP_1ST_WATER_ROOM_OPEN_UPPER_DOOR,
        x=7,
        y=20,
        z=5,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=4,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E3273_SHIP_1ST_WATER_ROOM_OPEN_UNDERWATER_DOOR,
        x=13,
        y=24,
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
        x=5,
        y=28,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=5,
        height=2,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
