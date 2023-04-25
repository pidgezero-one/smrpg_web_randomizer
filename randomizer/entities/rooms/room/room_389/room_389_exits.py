"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=15,
        y=95,
        z=2,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
        show_message=False,
        dst_x=1,
        dst_y=39,
        dst_z=3,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False,
    ),
    RoomExit(
        x=2,
        y=122,
        z=2,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R387_VOLCANO_AREA_19_FROM_HINO_MART_WSAVE_POINT,
        show_message=False,
        dst_x=7,
        dst_y=22,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
]
