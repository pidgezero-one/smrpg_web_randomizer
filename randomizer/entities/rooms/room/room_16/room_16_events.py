"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E1406_MARIOS_PAD_OPEN_DOOR,
        x=12,
        y=34,
        z=1,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=6,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E1407_MARIOS_PAD_CLOSE_DOOR,
        x=11,
        y=34,
        z=1,
        f=EdgeDirection.SOUTHWEST,
        length=3,
        height=6,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E1407_MARIOS_PAD_CLOSE_DOOR,
        x=11,
        y=33,
        z=1,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=6,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E1407_MARIOS_PAD_CLOSE_DOOR,
        x=12,
        y=35,
        z=1,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=6,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
