"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E2401_BEGIN_8BIT,
        x=22,
        y=61,
        z=4,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E2401_BEGIN_8BIT,
        x=22,
        y=63,
        z=4,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E2403_8BIT_END_EAST,
        x=26,
        y=66,
        z=4,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E2404_8BIT_END_WEST,
        x=19,
        y=65,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
