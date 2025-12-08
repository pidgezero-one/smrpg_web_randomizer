"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3690_NIMBUS_CASTLE_MAIN_HALL_EXIT_TO_EXTERIOR,
        x=1,
        y=36,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False),
    Event(
        event=E3768_NIMBUS_CASTLE_MAIN_HALL_EXIT_TO_4_WAY_PATH,
        x=11,
        y=15,
        z=2,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False),
]
