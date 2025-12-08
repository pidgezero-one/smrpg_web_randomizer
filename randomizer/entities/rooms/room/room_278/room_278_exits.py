"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=11,
        y=90,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R276_MOLEVILLE_MINES_AREA_01_ENTRANCE,
        show_message=False,
        dst_x=20,
        dst_y=25,
        dst_z=4,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=19,
        y=95,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R274_MOLEVILLE_MINES_AREA_02,
        show_message=False,
        dst_x=3,
        dst_y=87,
        dst_z=4,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
