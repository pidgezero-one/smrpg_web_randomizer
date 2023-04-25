"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E0595_MINES_BOSS_ROOM_EXIT,
        x=9,
        y=12,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=4,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E0599_MINES_BOSS_ROOM_ENTRANCE_REVERSE,
        x=1,
        y=30,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
