"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=2,
        y=125,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER,
        show_message=False,
        dst_x=30,
        dst_y=71,
        dst_z=10,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=10,
        y=111,
        z=7,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=1,
        nw_se_edge_active=True,
        ne_sw_edge_active=True,
        byte_2_bit_2=False,
        destination=R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM,
        show_message=False,
        dst_x=14,
        dst_y=121,
        dst_z=1,
        dst_z_half=True,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
