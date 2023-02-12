from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E0517_ROSE_TOWN_OCCUPIED_EXIT,
        x=1,
        y=19,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
    Event(
        event=E0518_ROSE_TOWN_OCCUPIED_STAIRWAY,
        x=6,
        y=13,
        z=1,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=2,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
]
