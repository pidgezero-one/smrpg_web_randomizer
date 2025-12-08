"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    MapExit(
        x=29,
        y=87,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=True,
        destination=OW09_MUSHROOM_WAY,
        show_message=False,
        byte_2_bit_1=False,
        byte_2_bit_0=False),
    RoomExit(
        x=3,
        y=78,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R204_MUSHROOM_WAY_AREA_02,
        show_message=False,
        dst_x=20,
        dst_y=37,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False),
]
