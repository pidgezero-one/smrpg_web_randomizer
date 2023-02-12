from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3191_ACTIVATE_POST_MINES_BOSS_FIRST_MINECART_SESSION,
        x=7,
        y=61,
        z=3,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=7,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
    Event(
        event=E3202_MINECART_ROOM_EXIT_TO_BOSS_ROOM,
        x=2,
        y=60,
        z=2,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
]
