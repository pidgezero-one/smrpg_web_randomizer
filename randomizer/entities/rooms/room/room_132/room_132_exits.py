"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=0,
        y=121,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R131_SEA_AREA_04_BUNCH_OF_ZEOSTARS,
        show_message=False,
        dst_x=3,
        dst_y=59,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
    RoomExit(
        x=13,
        y=100,
        z=4,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP,
        show_message=False,
        dst_x=1,
        dst_y=31,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False,
    ),
]
