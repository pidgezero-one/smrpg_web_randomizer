"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E2442_FOREST_INITIATE_MAZE,
        x=16,
        y=15,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E2444_FOREST_PREMAZE_SAVE_ROOM_TRUNK,
        x=6,
        y=40,
        z=2,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
