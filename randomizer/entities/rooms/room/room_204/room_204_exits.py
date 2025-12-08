"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=4,
        y=38,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R203_MUSHROOM_WAY_AREA_01,
        show_message=False,
        dst_x=12,
        dst_y=10,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=20,
        y=39,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R205_MUSHROOM_WAY_AREA_03,
        show_message=False,
        dst_x=4,
        dst_y=78,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
