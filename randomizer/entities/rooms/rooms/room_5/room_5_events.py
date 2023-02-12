from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E0601_MARRYMORE_BACK_DOOR_ENTER_CHAPEL,
        x=20,
        y=65,
        z=6,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
    Event(
        event=E0672_MARRYMORE_OCCUPIED_EXTERIOR_CHAPEL_FRONT_ENTRANCE,
        x=18,
        y=63,
        z=6,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
]
