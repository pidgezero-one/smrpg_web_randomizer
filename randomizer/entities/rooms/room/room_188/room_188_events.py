"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3274_SHIP_UPPER_WHIRLPOOL_ROOM_OPEN_UNDERWATER_DOOR,
        x=9,
        y=74,
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
        x=2,
        y=84,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=7,
        height=4,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
