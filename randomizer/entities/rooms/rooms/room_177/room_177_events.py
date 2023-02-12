from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3214_SHIP_1ST_BOSS,
        x=16,
        y=41,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
    Event(
        event=E3262_SHIP_PASSWORD_ROOM_OPEN_DOOR_TO_BOSS,
        x=16,
        y=42,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=4,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
]
