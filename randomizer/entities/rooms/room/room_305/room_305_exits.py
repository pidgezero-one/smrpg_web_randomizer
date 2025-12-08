"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=4,
        y=50,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
        show_message=False,
        dst_x=18,
        dst_y=62,
        dst_z=1,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=3,
        y=41,
        z=1,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=1,
        nw_se_edge_active=True,
        ne_sw_edge_active=True,
        byte_2_bit_2=False,
        destination=R306_SEASIDE_TOWN_INN_2F,
        show_message=False,
        dst_x=1,
        dst_y=75,
        dst_z=1,
        dst_z_half=True,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
