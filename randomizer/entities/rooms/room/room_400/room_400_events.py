"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E2225_KEEP_2ND_BOSS,
        x=11,
        y=48,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=3,
        height=6,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E2149_KEEP_RESUMMON_ENEMIES_ON_EXIT,
        x=13,
        y=43,
        z=1,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
