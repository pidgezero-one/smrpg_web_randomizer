"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=3,
        y=102,
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
        dst_y=27,
        dst_z=5,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
    RoomExit(
        x=6,
        y=97,
        z=1,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=1,
        nw_se_edge_active=True,
        ne_sw_edge_active=True,
        byte_2_bit_2=False,
        destination=R308_SEASIDE_TOWN_ELDERS_HOUSE_2F,
        show_message=False,
        dst_x=17,
        dst_y=21,
        dst_z=1,
        dst_z_half=True,
        dst_f=NORTHWEST,
        x_bit_7=False,
    ),
]
