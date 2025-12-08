"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=24,
        y=67,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
        show_message=False,
        dst_x=3,
        dst_y=47,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
    RoomExit(
        x=15,
        y=55,
        z=2,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
        show_message=False,
        dst_x=6,
        dst_y=123,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False),
]
