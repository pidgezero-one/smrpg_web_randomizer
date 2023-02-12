from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E2798_STAR_HILL_EXIT_TO_WORLD_MAP,
        x=12,
        y=20,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=7,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
    Event(
        event=E2799_STAR_HILL_ENTRANCE_TO_1ST_ROOM,
        x=4,
        y=12,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=7,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
]
