"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=23,
        y=121,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM,
        show_message=False,
        dst_x=16,
        dst_y=117,
        dst_z=2,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
    RoomExit(
        x=30,
        y=115,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R186_SUNKEN_SHIP_POSTKC_AREA_18_WARP_ROOM_FROM_JOHNNYS_ROOM,
        show_message=False,
        dst_x=29,
        dst_y=70,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False,
    ),
]
