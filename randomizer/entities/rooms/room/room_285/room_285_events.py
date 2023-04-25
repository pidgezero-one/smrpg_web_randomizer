"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3160_MINES_LONG_TRACK_ROOM_LOWER_BACKWARD_EXIT,
        x=2,
        y=124,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E3161_MINES_CHECK_IF_SHYGUY_MOVED,
        x=15,
        y=97,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
