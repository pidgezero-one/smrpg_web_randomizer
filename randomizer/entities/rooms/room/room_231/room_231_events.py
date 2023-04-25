"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E2438_FOREST_SECRET_TRUNK,
        x=19,
        y=74,
        z=2,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E2439_FOREST_SECRET_AREA_EXIT,
        x=21,
        y=79,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=3,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
