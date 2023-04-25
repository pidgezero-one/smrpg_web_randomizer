"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3514_NIMBUS_CASTLE_EGG_ROOM_EXIT_TO_PREVIOUS_ROOM,
        x=15,
        y=60,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E3515_NIMBUS_CASTLE_EGG_ROOM_EXIT_TO_NEXT_ROOM,
        x=21,
        y=47,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
