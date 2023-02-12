from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3248_SHIP_ENTRANCE_OPEN_RIGHT_DOOR,
        x=7,
        y=14,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=4,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
    Event(
        event=E3249_SHIP_ENTRANCE_OPEN_LEFT_DOOR,
        x=1,
        y=13,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=4,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
]
