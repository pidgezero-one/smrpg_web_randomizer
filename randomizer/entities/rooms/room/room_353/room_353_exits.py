"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=1,
        y=62,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP,
        show_message=False,
        dst_x=13,
        dst_y=103,
        dst_z=6,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
    RoomExit(
        x=6,
        y=72,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R387_VOLCANO_AREA_19_FROM_HINO_MART_WSAVE_POINT,
        show_message=False,
        dst_x=3,
        dst_y=18,
        dst_z=3,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
]
