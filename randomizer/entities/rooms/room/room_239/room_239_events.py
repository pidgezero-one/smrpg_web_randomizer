"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E2380_ABYSS_BOLT_NEAR_SIDE,
        x=28,
        y=36,
        z=10,
        f=EdgeDirection.SOUTHWEST,
        length=4,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E2597_ABYSS_PRE_FIRST_BOSS_BOLT,
        x=28,
        y=36,
        z=10,
        f=EdgeDirection.SOUTHWEST,
        length=3,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E2597_ABYSS_PRE_FIRST_BOSS_BOLT,
        x=21,
        y=49,
        z=7,
        f=EdgeDirection.SOUTHWEST,
        length=4,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
