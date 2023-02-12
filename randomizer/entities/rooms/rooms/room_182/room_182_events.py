from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3270_SHIP_ROOM_WITH_BOX_WALL_OPEN_RIGHT_DOOR,
        x=25,
        y=90,
        z=2,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=4,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
    Event(
        event=E3239_SHIP_OPEN_DOOR_TO_ROOM_BEHIND_BOX_WALL,
        x=20,
        y=91,
        z=2,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
]
