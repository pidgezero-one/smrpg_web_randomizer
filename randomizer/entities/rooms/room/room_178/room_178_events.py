"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3266_SHIP_LOWER_RAT_STAIRWAY_OPEN_UPPER_DOOR,
        x=14,
        y=83,
        z=6,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=4,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E3267_SHIP_LOWER_RAT_STAIRWAY_OPEN_LOWER_DOOR,
        x=9,
        y=91,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=4,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
