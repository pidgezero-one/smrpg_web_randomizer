"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E2407_STAR_HILL_FINAL_EXIT,
        x=26,
        y=109,
        z=2,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E2475_STAR_HILL_3RD_ROOM_SUMMON_SACKIT,
        x=19,
        y=123,
        z=2,
        f=EdgeDirection.SOUTHWEST,
        length=3,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E0998_SET_STAR_HILL_AS_CHECKED,
        x=24,
        y=82,
        z=2,
        f=EdgeDirection.SOUTHWEST,
        length=8,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E0998_SET_STAR_HILL_AS_CHECKED,
        x=24,
        y=81,
        z=2,
        f=EdgeDirection.SOUTHWEST,
        length=8,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
